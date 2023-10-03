from S1E9 import Character


class Baratheon(Character):
    '''Representing the Baratheon family.'''

    def __init__(self, first_name: str, is_alive: bool = True):
        '''
        ***
        Constructor of Baratheon class, calls super's constructor

        Parameters:
        first_name (str): Name of the character
        is_alive (bool): Whether the character is alive
        ***
        '''
        super().__init__(first_name, is_alive)
        self.familyname = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self) -> None:
        '''
        ***
        Set self.is_alive to False
        ***
        '''
        self.is_alive = False

    def __str__(self):
        """
        ***
        Return the detailed read-friendly description of 
        the class
        ***
        """
        return (f"Class of {__class__.__name__}, with {self.eyes} eyes and \
{self.hairs} hairs")

    def __repr__(self):
        """
        ***
        Returns a vector containing the class name, eye and hair color.
        ***
        """
        tup = (__class__.__name__, self.eyes, self.hairs)
        return (f"Vector: {tup}")


class Lannister(Character):
    '''Representing the Lannister family.'''

    def __init__(self, first_name: str, is_alive: bool = True):
        '''
        ***
        Constructor of Lannister class, calls super's constructor

        Parameters:
        first_name (str): Name of the character
        is_alive (bool): Whether the character is alive
        ***
        '''
        super().__init__(first_name, is_alive)
        self.familyname = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self) -> None:
        '''
        ***
        Set self.is_alive to False
        ***
        '''
        self.is_alive = False

    def __str__(self):
        """
        ***
        Return the detailed read-friendly description of 
        the class
        ***
        """
        return (f"Class of {__class__.__name__}, with {self.eyes} eyes and \
{self.hairs} hairs")

    def __repr__(self):
        """
        ***
        Returns a vector containing the class name, eye and hair color.
        ***
        """
        tup = (__class__.__name__, self.eyes, self.hairs)
        return (f"Vector: {tup}")

    @staticmethod
    def create_lannister(first_name: str, is_alive: bool = True
                         ):
        """
        ***
        Static method that acts like the constructor of the class.

        Return a new Lannister object
        ***
        """
        return Lannister(first_name, is_alive)
