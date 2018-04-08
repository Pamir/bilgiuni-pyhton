class Node:
    def __init__(self, data):
        self._data = data
        self._leftNode = None
        self._rightNode = None

    @property
    def data(self):
        return self._data

    @property
    def leftNode(self):
        return self._leftNode

    @leftNode.setter
    def leftNode(self, v):
        self._leftNode = v

    @property
    def rightNode(self):
        return self._rightNode

    @rightNode.setter
    def rightNode(self, v):
        self._rightNode = v


class BST:
    def __init__(self):
        self._rootNode = None

    def insert(self, data):
        n = Node(data)
        if self._rootNode == None:
            self._rootNode = n
            return

        tmp = self._rootNode

        while True:
            if tmp.data < data:
                if tmp.rightNode == None:
                    tmp.rightNode = n
                    return
                tmp = tmp.rightNode
            else:
                if tmp.leftNode == None:
                    tmp.leftNode = n
                    return

                tmp = tmp.leftNode

    def search(self, data):
        pass

    def dump(self):
        tmp = self._rootNode
        if tmp == None:
            return
        self._dump(tmp)

    def _dump(self, n):
        print(n.data)
        if n.leftNode != None:
            self._dump(n.leftNode)
        if n.rightNode != None:
            self._dump(n.rightNode)


if __name__ == "__main__":
    a = BST()
    a.insert(30)
    a.insert(40)
    a.insert(25)
    a.insert(100)
    a.insert(50)
    a.insert(75)
    a.dump()
