class Book():
	def __init__(self, title, author, quantity, price):
		self.title = title
		self.author = author
		self.quantity = quantity
		self.__price = price
		self.__discount = None   #encapsulation, private attribute, cannot be printed

	def set_discount(self, discount):
	        self.__discount = discount
	
	def getPrice(self):
		if self.__discount:
			return self.__price * (1- self.__discount)
		return self.__price

class Novel(Book):  
	def __init__(self, title, author, quantity, price, pages):
		super().__init__(title, author, quantity, price)
		self.pages = pages
class Academic(Book):
	def __init__(self, title, author, quantity, price, branch):
		super().__init__(title, author, quantity, price)
		self.branch = branch

Kitabu = Book("Vitendawili", "Mrono", 45, 5000)
Kitabu.set_discount(0.20)
Novel1 = Novel("Kuzo", "Kuzo", 345, 4500, 45)
Novel1.set_discount(0.20)
print(f"{Novel1.title} novel was written by {Novel1.author} quantity {Novel1.quantity} going for Ksh. {Novel1.getPrice()} and it has {Novel1.pages} pages")
print("{} book was written by {} quantity {} going for Ksh. {}".format(Kitabu.title, Kitabu.author, Kitabu.quantity, Kitabu.getPrice()))

#print(Kitabu.__discount)


#getters and setters are used to access private attributes



