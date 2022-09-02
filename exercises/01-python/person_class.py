class Module_Person:
    """
    Class Module_Person
    
    Attributes
    ----------
    name : str
        The Module_Person's name
    age : number
        The Module_Person's age
    """
    def __init__(self, name, age) : # initialize constructor for the object to assign the object its properties
        self.name = name
        self.age = age
    
    def print_info(self) : # method of the object that can be used
        """
        Prints the basic information about a person
        """
        print('My name is ', self.name,' and I am ',self.age)

class Module_Student(Module_Person) :
    """
    Class Module_Student which inherits from class Module_Person
    
    Attributes
    ----------
    name : str
        The Module_Student's name
    age : number
        The Module_Student's age
    graduation_year : number
        The Module_Student's graduation year
    """
    
    def __init__(self, name, age, graduation_year=None) :
        super().__init__(name, age)
        self.gradY = graduation_year
        
    def print_graduation(self, description) :
        """
        Prints the graduation of a student and his/her description
        :param description : str
            A description about the student
        """
        print(self.name, ' is a class ',self.gradY,' student. ',description)