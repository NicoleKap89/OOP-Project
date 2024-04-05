from Collection import Collection
from Exceptions import NoSuchDominoException


class Hand(Collection):
    def __init__(self, dominoes):
        """
        A constructor that initializes the field dominoes
        :param dominoes: (list[dominoes]) list of dominoes
        """
        Collection.__init__(self, dominoes)
        self.array = dominoes

    def add(self, domino, index=None):
        """
        adds domino to the array according to the given index. if index is None adds to the end of the array.
        :param domino: domino that is added
        :param index: place in the array to add  the domino to
        """
        if index is None:
            self.array.append(domino)
        else:
            self.array.insert(index, domino)

    def remove_domino(self, domino):
        """
        removes given domino from the array
        :param domino: domino to be removed
        :return: index of the domino that was removed, if it wasn't excited, raise exception
        """
        for do in range(len(self.array)):
            if self.array[do] == domino:
                self.array.remove(self.array[do])
                return do
        raise NoSuchDominoException("The domino is not in the list")

