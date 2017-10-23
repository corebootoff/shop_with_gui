#from BDManager import *
class Product(object):
    def __init__(self, name, producer, country, category, size, volume, price):

        self.name = name
        self.producer = producer
        self.country = country
        self.category = category
        self.size = size
        self.volume = volume
        self.price = price

    def __repr__(self):
        return '%s, %s, %s, %s, %s, %s, %s' % (self.name, self.producer, self.country, self.category, self.size, self.volume, self.price)


    def show_product(self, ID):
        pass

if __name__ == '__main__':
    new_product = Product(name = 'pants', producer = 'nike', country = 'India', category = 'pants', size = 48, volume = 20, price = 200)
    print(new_product)