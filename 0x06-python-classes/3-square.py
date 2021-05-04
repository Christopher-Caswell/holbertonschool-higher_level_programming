class Square:
    """Tell me about this Square"""
    def __init__(self, size=0):
        """Let's get ahead of the edge cases"""
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """Final declaration of the Square's size"""
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
