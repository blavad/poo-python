from ipile import IPile


class LIFO(IPile):
    """
    La pile LIFO (Last In First Out) est une pile dans lesquels
    les derniers éléments empilés seront les premiers dépilés.
    """

    def __init__(self, values):
        self.__pile = values

    def empile(self, value):
        self.__pile.append(value)

    def depile(self):
        if len(self.__pile) > 0:
            self.__pile.pop()

    def __str__(self):
        return f"LIFO({self.__pile})"
