
# We have to import abstract method from the abc module
from abc import ABC, abstractmethod

# Create a parent class with an abstract method
class book(ABC):
    def checkOut(self, date):
        print("Your check-out date: ", date)
# This function is telling us to pass in an argument, but we won't tell you how
# or what kind of data it will be
    @abstractmethod
    def bookCheckOut(self, date):
        pass

# Create child class
class CheckOutOnline(book):
# Here we define how to implement the bookCheckOut function from its parent
# checkOut class
    def bookCheckOut(self, date):
        print("Your book is due back in 30 days from {}".format(date))


obj = CheckOutOnline()
obj.checkOut("August 15, 2021")
obj.bookCheckOut("August 15, 2021")
