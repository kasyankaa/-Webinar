from abc import ABC, abstractmethod


class AbstractParent(ABC):
    
     @abstractmethod
    def bring_up_question(self):
        raise NotImplementedError

    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError


class Mum(AbstractParent):

    def __init__(self, age):
        self.age = age
        print("mum creating")

    def do_work(self):
        print("i`m working")

    def do_house_work(self):
        print("listening music")


class Dad(AbstractParent):

    def __init__(self):
        print("dad creating")

    def play_guitar(self):
        print("dad is plaing guitar")

    def do_house_work(self):
        print("sitting on the sofa and drinking beer")


class Daughter(Mum, Dad):

    def bring_up_question(self):
        print("May i go?")

    def hello_friend(self):
        print("hello")

    def __init__(self, age=0):
        Dad.__init__(self)
        Mum.__init__(self, age=age)

    def do_work(self):
        print("i`m working hard")


class Friend:
    pass


def greet_mother(mother: Mum):
    print("Hello mum")
    mother.do_work()


def greet_father(father: Dad):
    print("daddy")
    father.play_guitar()


if __name__ == "__main__":
    daughter = Daughter()
    daughter.hello_friend()
    daughter.bring_up_question()
    daughter.do_house_work()
    # change parents
    for x in [daughter]:
        x.do_house_work()

    y_1 = [1, 2, 3, 'sdg']  # list a collection which is ordered and changeable. Allows duplicate members.
    y_2 = ("cvv", 1, 12)  # tuple a collection which is ordered and unchangeable. Allows duplicate members.
    у_3 = {34, 243, "56"}  # set a collection which is unordered and unindexed. No duplicate members.
    another_set = frozenset(["do", "re", "mi"])  # frozen_set
    y_4 = {  # dictionary a collection which is unordered, changeable and indexed. No duplicate members.
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
