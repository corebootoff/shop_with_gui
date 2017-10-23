import product
import DBManager
class Shop(object):
    def __init__(self, name_of_shop, first_cash):
        self.name_of_shop = name_of_shop
        self.cash = first_cash
        self.session = DBManager.create_session()

    # def _add_to_DB(self, product):
    #     self.session

    def add_product(self, name, producer, country, category, size, volume, price):
        '''функция передает все параметры нового продукта в DBManager для дальнейшего сравнения и записи в базе данных'''
        new_product = product.Product(name, producer, country, category, size, volume, price)
        DBManager.add_product(new_product, self.session)
        

    def sale_product(self, ID):
        pass

    def set_discount(self):
        pass

    def show_all(self):
        pass

    def show_ID(self):
        pass

if __name__ == '__main__':

    shop = Shop('Z', 100000)
    shop.add_product('спортивные брюки', 'adidas', 'India', 'm', 'm', 10, 1200)
