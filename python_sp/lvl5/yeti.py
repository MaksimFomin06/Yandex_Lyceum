from functools import total_ordering


@total_ordering
class Human:
    def __init__(self, name, friends=None, dishes=None):
        self.name = name
        self.friends = friends if friends is not None else []
        self.dishes = dishes if dishes is not None else []

    def __iadd__(self, friend):
        self.friends.append(friend)
        return self

    def __add__(self, dish):
        self.dishes.append(dish)
        return self

    def __call__(self):
        return f"{self.name} to the rescue!"

    def __lt__(self, other):
        if len(self.friends) != len(other.friends):
            return len(self.friends) < len(other.friends)
        if len(self.dishes) != len(other.dishes):
            return len(self.dishes) < len(other.dishes)
        return self.name < other.name

    def __eq__(self, other):
        return (len(self.friends) == len(other.friends)) and \
               len(self.dishes) == len(other.dishes) and \
               self.name == other.name

    def __repr__(self):
        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"friends={self.friends}, dishes={self.dishes})")


class Elf:
    def __init__(self, name):
        self.name = name

    def build(self):
        return f"{self.__class__.__name__} {self.name} built a house."

    def save(self, animal):
        return f"{self.__class__.__name__} {self.name} saved the {animal}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"


class Yeti(Elf, Human):
    def __init__(self, name, friends=None, dishes=None, mountains="Himalayas"):
        Elf.__init__(self, name)
        Human.__init__(self, name, friends or [], dishes or [])
        self.mountains = mountains

    def hide(self):
        return f"{self.name} hid in the {self.mountains}."

    def __repr__(self):
        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"friends={self.friends}, dishes={self.dishes}, "
                f"mountains='{self.mountains}')")