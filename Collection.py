
class Collection:
    def __init__(self, array):
        """
        A constructor that initializes the field array
        :param array: (list[objects])
        """
        self.array = array

    def get_collection(self):
        """
        returns the array filed
        :return: (list) array filed
        """
        return self.array

    def add(self, item, option):
        """
        The methods will be defined later on.
        :param item: object the will be added to the array
        :param option: option to define another variable
        :return: NotImplementedError exception
        """
        raise NotImplementedError("The function is not implemented now")

    def __getitem__(self, i):
        """
        The method will return the object in index i in the field
        :param i: index
        :return: the object in index i in the field
        """
        if 0 <= i < len(self.array):
            return self.array[i]
        return None

    def __eq__(self, other):
        """
        returns whether self and other are equal
        :param other: object which is compared to
        :return: (bool) True if equal, False otherwise.
        """
        if not isinstance(other, Collection):  # checks if self and other are ame type
            return False
        if self.array == other.array:
            return True
        return False

    def __ne__(self, other):
        """
        returns whether self and other are different
        :param other: object which is compared to
        :return: (bool) True if different, False otherwise.
        """
        return not self.__eq__(other)

    def __len__(self):
        """
        returns the number of objects in the array
        :return: (int) number of objects in the array
        """
        return len(self.array)

    def __contains__(self, item):
        """
        returns if the item is in the array
        :param item: an object
        :return: (bool) True if the item is in the array, False otherwise.
        """
        for mem in self.array:
            if item == mem:
                return True
        return False

    def __str__(self):
        """
        returns string representation of the current Collection
        :return: (str) representation of the current Collection
        """
        cur_col = ""
        for mem in self.array:
            mem = str(mem)
            cur_col += mem
        return cur_col

    def __repr__(self):
        """
        returns string representation of the current Collection
        :return: (str) representation of the current Collection
        """
        return self.__str__()
