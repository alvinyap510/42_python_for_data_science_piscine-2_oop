'''
This exercise implements static method.
'''


class calculator:
    '''
    Calculator that has static functions
    '''

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''
        Produce the dot product of 2 vectors
        '''
        print(
            "Dot product is: " +
            f"{sum([float(n1 * n2) for n1, n2 in zip(V1, V2)])}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add 2 vectors together and print the result.
        """
        print(f"Add Vector is : {[float(n1 + n2) for n1, n2 in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract second vector from first vector and print the result.
        """
        print(f"Sous Vector is: {[float(n1 - n2) for n1, n2 in zip(V1, V2)]}")
