class Sivrisinek:

    def __init__(self, name):
        print(id(self))
        print("Sivrisinek doğuyor")
        self._name = name
        self._yas = 0
        self._kanatboyu = 0

    @property
    def kanatboyu(self):
        return self._kanatboyu

    @kanatboyu.setter
    def kanatboyu(self, boy):
        self._kanatboyu = boy

    @property
    def yas(self):
        return self._yas

    @yas.setter
    def yas(self, yas):
        self._yas = yas

    @property
    def name(self):
        return self._name

    def fly1(self, to):
        print("{0} is flying to {1}".format(self._name, to))

    def fly(self, f, to):
        print("{0} is flying from {1} to {2}".format(self._name, f, to))


if __name__ == "__main__":
    a = Sivrisinek("ali")
    b = Sivrisinek("osman")

    print(a.name)
    print(b.name)
    print(id(a))
    print(id(b))
    a.yas = 10
    b.yas = 12
    a.kanatboyu = 2
    b.kanatboyu = 3
    print(a.yas)
    print(b.yas)
    a.fly1("Madrid")
    b.fly("Istanbul", "Barcelona")
    print(a.kanatboyu)
    print(b.kanatboyu)
