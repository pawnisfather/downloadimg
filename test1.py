import sys


class Aaa(object):
    def __init__(self):
        self.__money = 100

    @property
    def money(self):
        return self.__money

    @money.setter
    def set_money(self, new_money):
        print("set")
        self.__money = new_money





if __name__ == '__main__':
    print(Aaa().money)
