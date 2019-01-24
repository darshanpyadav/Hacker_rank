from . import Carnivorae
from . import Herbivorae


class Mammalia(object):
    extremities = 4

    def feeds(self):
        print("milk")

    def proliferates(self):
        pass


class Marsupialia(Mammalia):
    def proliferates(self):
        print("poach")

    def test_function_change(self, one_more_parm):
        pass


class Placentalia(Mammalia):
    def proliferates(self):
        print("placenta")


class TasmanianDevil(Marsupialia, Carnivorae):
    pass


class Duckbill(Marsupialia, Herbivorae):
    pass


class Cat(Carnivorae, Placentalia):
    pass


class Tiger(Placentalia, Carnivorae):
    pass


class Cow(Placentalia, Herbivorae):
    pass


Cat.feeds()
