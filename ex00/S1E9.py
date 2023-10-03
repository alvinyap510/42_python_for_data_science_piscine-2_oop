from abc import ABC, abstractmethod

# This exercise is about learning


class Character(ABC):
    """
    Abstract base class representing a character

    Attributes:
    first_name (str): Name of the character
    is_alive (bool): Whether the character is alive

    Methods:
    die(): Abstract method to be implemented by child
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        '''
        ***
        Constructor of abstract class character

        Parameters:
        first_name (str): Name of the character
        is_alive (bool): Whether the character is alive
        ***
        '''
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        '''
        ***
        Abstract method to be implemented by child
        ***
        '''
        pass


class Stark(Character):
    """
    Stark class that inherits Character abstract base class

    Attributes:
    first_name (str): Name of the character
    is_alive (bool): Whether the character is alive

    Methods:
    die(): Switch is_alive to False
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        '''
        ***
        Constructor of Strack class, calls super's constructor

        Parameters:
        first_name (str): Name of the character
        is_alive (bool): Whether the character is alive
        ***
        '''
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        '''
        ***
        Set self.is_alive to False
        ***
        '''
        self.is_alive = False
