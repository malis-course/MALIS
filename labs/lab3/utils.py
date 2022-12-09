import random
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, cos, pi
import pandas as pd

class Dataset:
    '''
    A class representing a dataset built reading the file whose name is stored in 'datafile'. The first layer of an instance of the SVM class should be a Dataset object.
    
    self.input : is a numpy array containing the inputs. Size is NxD, N number of samples, D dimensions
    self.output : is a numpy array containing the target corresponding at each input. Size is N
    self.input_size : is the number of dimensions D
    self.len : is the number of samples N
    self.indices : is a list containing the different indices of the samples: from 0 to N-1
    '''
    def __init__(self, datafile=None, input_size=0, length=0):
        '''
        Initializing function to build the Dataset.
        
        INPUT:
        - datafile : a path with the name of the file containing the data to be stored in the dataset
        - input_size : D, the bumber of dimensions of each input
        - length : N , the number if input samples
        '''
        
        self.input=[]
        self.output=[]
        
        if datafile:
            datas=pd.read_csv(datafile,delimiter=' ')
            self.input = datas.drop(['y'],axis=1).values
            self.output = datas['y'].values
            self.input_size = self.input.shape[1] # Number of input dimensions
            self.len = self.input.shape[0] # Number of samples in the dataset (accessible through len(dataset))
            self.indices = list(range(self.len)) # List of indices used to pick samples in a random order
        else :
            self.input_size = input_size # Number of input dimensions
            self.len = length # Number of samples in the dataset (accessible through len(dataset))
            self.indices = list(range(self.len)) # List of indices used to pick samples in a random order
class SVM:
    '''
    A class representing a Support Vector Machine (SVM) used to build SVM models
    '''
    def __init__(self, train_dataset, test_dataset):
        # infile: SVM description file, dataset: Dataset object
        self.dataset = train_dataset # Current dataset
        self.train_dataset = train_dataset # Training dataset
        self.test_dataset = test_dataset # Testing dataset
        self.train_plot = list() # You can use this to make plots
        self.test_plot = list() # Plot for test dataset
        input_dimensions=self.dataset.input_size
        self.w = np.random.rand(input_dimensions+1)-0.5 # self.w[-1] is actually b
        self.print_step=None


    def train(self, n_iterations, lambda_w, print_every_k=None,verbose=False):
        '''
        Train function (with specified number of epochs, lambda and decay)
        '''
        pass


    def setmode(self, mode):
        '''
        Function used to change between training set and testing set
        '''
        if mode == "train":
            self.dataset = self.train_dataset
        elif mode == "test":
            self.dataset = self.test_dataset
        else:
            print("Unknown mode!")

    def print_accuracy(self):
        '''
        Print accuracy of neural network on current dataset
        '''
        print("Accuracy:", 100*self.compute_accuracy(), "%")

    def compute_accuracy(self):
        '''
        Compute accuracy of neural network on train and test dataset and return accuracy on test dataset
        '''
        # Compute accuracy on training set
        self.setmode("train")
        x=np.concatenate((self.dataset.input,np.ones((self.dataset.len,1))),axis=1)
        accuracy=np.mean(np.sign(x @ self.w.T) == self.dataset.output.T)
        self.train_plot.append(accuracy)

        # Compute accuracy on testing set
        self.setmode("test")
        x=np.concatenate((self.dataset.input,np.ones((self.dataset.len,1))),axis=1)
        self.test_plot.append(np.mean(np.sign(x @ self.w.T) == self.dataset.output.T))

        # Do not forget to go back to the training set!
        self.setmode("train")

        return accuracy

    def reset_plot(self):
        '''
        Reset plot
        '''
        self.train_plot = list()
        self.test_plot = list()

    def make_plot(self):
        '''
        Print plot
        '''
        plt.plot([x*self.print_step for x in range(len(self.train_plot))], self.train_plot, 'r-',label='training accuracy')
        plt.plot([x*self.print_step for x in range(len(self.test_plot))], self.test_plot, 'g-', label='test accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch number')
        plt.axis([0, self.print_step*(len(self.train_plot)-1), 0, 1.05])
        plt.legend()
        plt.show()
