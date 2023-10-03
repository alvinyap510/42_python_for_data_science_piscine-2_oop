'''
This exercise is about learning operator overloading.
'''


class calculator:
    '''
    Calculator class that has its mathematic operators implementation
    overriden.
    '''

    def __init__(self, num_array: list[float]):
        '''
        Constructor function of calculator class.
        '''
        self.num_array = num_array

    def __add__(self, object) -> None:
        '''
        Overriding the build in __add__, and called when "+" operator
        is used.
        '''
        assert isinstance(object, (int, float)
                          ), "Operator must followed by int or float"
        self.num_array = [n + object for n in self.num_array]
        print(self.num_array)

    def __mul__(self, object) -> None:
        '''
        Overriding the build in __mul__, and called when "*" operator
        is used.
        '''
        assert isinstance(object, (int, float)
                          ), "Operator must followed by int or float"
        self.num_array = [n * object for n in self.num_array]
        print(self.num_array)

    def __sub__(self, object) -> None:
        '''
        Overriding the build in __sub__, and called when "-" operator
        is used.
        '''
        assert isinstance(object, (int, float)
                          ), "Operator must followed by int or float"
        self.num_array = [n - object for n in self.num_array]
        print(self.num_array)

    def __truediv__(self, object) -> None:
        '''
        Overriding the build in __truediv__, and called when "/" operator
        is used.
        '''
        assert isinstance(object, (int, float)
                          ), "Operator must followed by int or float"
        self.num_array = [n / object for n in self.num_array]
        print(self.num_array)
