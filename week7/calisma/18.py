class Node:
    def __init__(self, data):
        self._data = data
        self._nextNode = None

    @property
    def data(self):
        return self._data

    @property
    def nextNode(self):
        return self._nextNode

    @nextNode.setter
    def nextNode(self, v):
        self._nextNode = v


class LinkedList:
    def __init__(self):
        self._rootNode = None

    def insert(self, data):
        tmp = Node(data)
        if self._rootNode == None:
            self._rootNode = tmp
            return

        n = self._rootNode
        while n.nextNode != None:
            n = n.nextNode
        n.nextNode = tmp

    def dump(self):
        tmp = self._rootNode
        while tmp != None:
            print(tmp.data)
            tmp = tmp.nextNode


if __name__ == "__main__":
    a = LinkedList()
    a.insert("Bostanci")
    a.insert("Suadiye")
    a.insert("Erenkoy")
    a.insert("Caddebostan")
    a.dump()
