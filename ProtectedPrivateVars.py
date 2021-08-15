
# Create classes that use encapsulation
# This class makes use of a protected attribute
class Protected:
    def __init__(self):
        self._protectedVar = ''

# This object makes use of the protected attribute
obj = Protected()
obj._protectedVar = 'Hello'
print(obj._protectedVar + ' World')


# This class makes use of a private attribute
class Private:
    def __init__(self):
        self.__privateVar = 'Hello'

    def getPrivate(self):
        print(self.__privateVar + ' World')

    def setPrivate(self, private):
        self.__privateVar = private

# This object makes use of the private attribute
obj = Private()
obj.getPrivate()
obj.setPrivate('Goodbye')  # This sets the private attribute to something different
obj.getPrivate()  # This prints the object created
