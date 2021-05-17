#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

    from models.rectangle import Rectangle

#    if __name__ == "__main__":
#        r1 = Rectangle(10, 2)
#        print(r1.id)
#
#        r2 = Rectangle(2, 10)
#        print(r2.id)
#
#        r3 = Rectangle(10, 2, 0, 0, 12)
#        print(r3.id)

    """ 2-main """
    from models.rectangle import Rectangle

    if __name__ == "__main__":

        try:
            Rectangle(10, "2")
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

        try:
            r = Rectangle(10, 2)
            r.width = -10
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

        try:
            r = Rectangle(10, 2)
            r.x = {}
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

        try:
            Rectangle(10, 2, 3, -1)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
""" 3-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())

""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()

""" 5-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)

""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()
