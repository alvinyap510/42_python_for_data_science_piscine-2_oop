from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''
    A King clas that inherits both Baratheon and Lannister.
    Demonstration of Diamond Problem / Multiple Inherittence.
    '''

    def __init__(self, first_name: str, is_alive: bool = True):
        '''
        ***
        Constructor of King class, calls super's constructor.
        Calls Baratheon as parent first, because Baratheon is
        on the left thus preceeds Lannister.

        Parameters:
        first_name (str): Name of the character
        is_alive (bool): Whether the character is alive
        ***
        '''
        super().__init__(first_name, is_alive)

    def set_eyes(self, eye_color: str):
        '''
        ***
        Set the hair color of the object.
        ***
        '''
        self.eyes = eye_color

    def set_hairs(self, hair_color: str):
        '''
        ***
        Set the eye color of the object.
        ***
        '''
        self.hairs = hair_color

    def get_eyes(self) -> str:
        '''
        ***
        Return the eye color of the object.
        ***
        '''
        return self.eyes

    def get_hairs(self) -> str:
        '''
        ***
        Return the hair color of the object.
        ***
        '''
        return self.hairs
