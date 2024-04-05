class EmptyBoardException(Exception):
    pass


class FullBoardException(Exception):
    pass


class NoSuchDominoException(Exception):
    pass


class InvalidNumberException(Exception):

    def __init__(self, text):
        """
        A constructor that initializes the field text
        :param text: (string)
        """
        self.text = text

    def __str__(self):
        """
        returns the exception with the word 'ERROR' in the beginning
        :return: the exception with the word 'ERROR' in the beginning
        """
        return "ERROR" + " " + self.text
