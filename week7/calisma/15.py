class Sivrisinek:

    def __init__(self,name):
        print(id(self))
        print("Sivrisinek doğuyor")
        self._name = name
        self._yas = 0
        self._kanatboyu = 0

    def get_kanatboyu(self):
        return self._kanatboyu

    def set_kanatboyu(self,boy):
        self._kanatboyu = boy

    def get_yas(self):
        return self._yas

    def set_yas(self,yas):
        self._yas = yas


    def get_name(self):
        return self._name

if __name__ == "__main__":
    a = Sivrisinek("ali")
    b = Sivrisinek("osman")

    print(a.get_name())
    print(b.get_name())
    print(id(a))
    print(id(b))
    a.set_yas(10)
    b.set_yas(12)
    a.set_kanatboyu(2)
    b.set_kanatboyu(3)
    print(a.get_yas())
    print(b.get_yas())
    print(a.get_kanatboyu())
    print(b.get_kanatboyu())