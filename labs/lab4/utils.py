class Dataset:
    '''
    Class representing a set of samples.
    '''
    def __init__(self, data):
        self.data = data # a set of Sample objects
        self.len = len(data)
        if self.len:
            self.entropy = self.compute_entropy()
            self.p_positive = len([x for x in self.data if x.is_positive == True])/self.len # Proportion of positive (edible) samples in the dataset
        else:
            self.entropy = 0.
            self.p_positive = 0.

    def __len__(self):
        return len(self.data)

    def compute_entropy(self):
        return 0.

    def split(self, attribute, value, function):
        return set(), set(), 0.


class Sample:
    '''
    Class representing a sample
    
    If a sample is edible, self.is_positive is True
    '''
    def __init__(self, is_positive, attributes_list, values):
        self.attributes = dict()
        self.hash = hash(tuple([is_positive]+values))
        for i in range(len(attributes_list)):
            self.attributes[attributes_list[i]] = values[i]
        self.is_positive = is_positive # True when edible, False when poisonous

    def __str__(self):
        return str(self.attributes)

    def __hash__(self):
        return self.hash

class Tree:
    '''
    Class Tree
    '''
    def __init__(self, questions_set, train_dataset, max_level, parent=None):
        self.train_dataset = train_dataset # Train set
        self.parent = parent # Parent tree
        self.entropy_before = train_dataset.entropy # Entropy before splitting
        if parent: # If tree has a parent...
            self.level = parent.level + 1 # then its level is the parent level + 1 
        else:
            self.level = 0 # else level = 0
        if max_level == self.level: # If we reached the maximum level
            self.question = (None, None, None) # then no question
            self.entropy_after = self.entropy_before # and the entropy does not change
        else: # Otherwise
            self.question, self.entropy_after = self.make_question(questions_set, max_level) # we try to find the best question to ask
        self.is_leaf = self.entropy_after == self.entropy_before # If the entropy does not move, then it is a leaf
        if self.is_leaf: # If it is a leaf, then we say whether mushrooms should be edible or not when they arrive here
            if self.train_dataset.p_positive > 0.5:
                self.is_positive = 1
            else:
                self.is_positive = -1

    def __str__(self, level=0):
        '''
        String representation of the computed decision tree
        '''
        if self.is_leaf:
            p_positive = int(10000*self.train_dataset.p_positive)/100
            question = "---> " + str(self.is_positive==1) + " (p_positive = " + str(p_positive) + " %)"
        else:
            entropy_gain = int(100*(self.entropy_before - self.entropy_after))/100
            question = "(" + self.question[0] + " " + self.question[2].__name__ + " " + self.question[1] + "? Entropy gain = " + str(entropy_gain) +")"
        ret = "\t"*level + question + "\n"
        if not self.is_leaf:
            ret += self.pos_tree.__str__(level=level+1) # First line is the node corresponding to a POSITIVE answer to the question
            ret += self.neg_tree.__str__(level=level+1) # Second line is the node corresponding to a NEGATIVE answer to the question
        return ret

    def __call__(self, mushroom):
        '''
        Return 1 is edible and -1 if not
        '''
        if self.is_leaf:
            return self.is_positive
        else:
            attribute, value, function = self.question
            if function(mushroom.attributes[attribute], value):
                return self.pos_tree(mushroom)
            else:
                return self.neg_tree(mushroom)

    def get_size(self):
        '''
        Returns the depth of the tree
        '''
        if self.is_leaf:
            return self.level
        else:
            return max(self.pos_tree.get_size(), self.neg_tree.get_size())

    def make_question(self, questions_set, max_level):
        '''
        Find the best question for a node. If no entropy improvement is possible, then (None, None, None), self.entropy_before is returned.
        '''
        best_entropy = self.entropy_before
        pos_set = set()
        neg_set = set()
        best_question = (None, None, None)
        for attribute, value, function in questions_set:
            new_pos_set, new_neg_set, new_entropy = self.train_dataset.split(attribute, value, function) # Split dataset according to question (attribute, value, function)
            if new_entropy < best_entropy: # If entropy improves
                best_entropy = new_entropy
                pos_set = new_pos_set
                neg_set = new_neg_set
                best_question = (attribute, value, function)
        if best_question[0]: # If at least one question improves entropy
            if len(pos_set) and len(neg_set): # If none of both sets are empty
                new_questions_set = questions_set - set([best_question])
                self.pos_tree = Tree(new_questions_set, pos_set, max_level, parent=self)# Where to go if the answer to the best question is positive
                self.neg_tree = Tree(new_questions_set, neg_set, max_level, parent=self)# Where to go if the answer to the best question is negative
            else: # It can happen that entropy decreases due to floating-point errors...
                return best_question, self.entropy_before # If one of the sets if empty, then we return the previous entropy
                                                          # and it means that the current node is actually a leaf
        return best_question, best_entropy

def equals(a, b):
    return a == b

def import_data():
    '''
    Import data. Returns a set of training samples, a set of test samples and a set of questions.
    Questions are in the form (attribute, value, function) and if x is a sample, then the question
    in English is "is function(x.attributes[attribute], value) true?".
    
    For instance if function = equals, the question is "does x.attributes[attribute] equal value ?"
    '''
    edible = {"e": True, "p": False}

    train_set = set()
    with open("mushrooms_train.csv") as f:
        attributes_list = f.readline().strip().split(",")[1:]
        questions_dict = dict()
        for x in attributes_list:
            questions_dict[x] = set()
        for line in f:
            sample = line.strip().split(",")
            is_edible, values = edible[sample[0]], sample[1:]
            for i in range(len(values)):
                questions_dict[attributes_list[i]].add(values[i])
            mushroom = Sample(is_edible, attributes_list, values)
            train_set.add(mushroom)

    test_set = set()
    with open("mushrooms_test.csv") as f:
        f.readline()
        for line in f:
            sample = line.strip().split(",")
            is_edible, values = edible[sample[0]], sample[1:]
            for i in range(len(values)):
                questions_dict[attributes_list[i]].add(values[i])
            mushroom = Sample(is_edible, attributes_list, values)
            test_set.add(mushroom)

    questions_set = set()

    for x in questions_dict:
        for y in questions_dict[x]:
            questions_set.add((x, y, equals))

    return train_set, test_set, questions_set

def accuracy(tree, test_set):
    '''
    Compute the accuracy of tree on test_set
    '''
    accuracy = 0
    for m in test_set:
        is_positive = tree(m)
        if is_positive == 1 and m.is_positive:
            accuracy += 1/len(test_set)
        elif is_positive == -1 and not m.is_positive:
            accuracy += 1/len(test_set)
    return accuracy
