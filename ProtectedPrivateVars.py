
class Protected:
    def __init__(self):
        self._protectedVar = ''

obj = Protected()
obj._protectedVar = 'Hello'
print(obj._protectedVar)


class Private:
    def __init__(self):
        self.__privateVar = 'Hello'

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Private()
obj.getPrivate()
obj.setPrivate('Goodbye')
obj.getPrivate()
