from ipile import IPile


class FIFO(IPile):
    """
    La pile FIFO (First In First Out) est une pile dans lesquels
    les premiers éléments empilés seront les premiers dépilés.
    """

    def __init__(self, values):
        self.__pile = values

    def empile(self, value):
        self.__pile.append(value)

    def depile(self):
        if len(self.__pile) > 0:
            del self.__pile[0]

    def __str__(self):
        return f"FIFO({self.__pile})"
