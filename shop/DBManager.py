from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import product

Base = declarative_base()

class Producer(Base):
    __tablename__ = 'producers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Category(Base):
    __tablename__ ='categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Size(Base):
    __tablename__ = 'sizes'
    id = Column(Integer, primary_key=True)
    size = Column(Integer, nullable=False)

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    producer_id = Column(Integer, ForeignKey('producers.id'))
    producer = relationship(Producer, foreign_keys = [producer_id])
    country_id = Column(Integer, ForeignKey('countries.id'))
    country = relationship(Country, foreign_keys=[country_id])
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship(Category, foreign_keys=[category_id])
    size_id = Column(Integer, ForeignKey('sizes.id'))
    size = relationship(Size, foreign_keys=[size_id])
    volume = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)

    def __init__(self, name, producer_id, country_id, category_id, size_id, volume, price):
        self.name = name
        self.producer_id = producer_id
        self.country_id = country_id
        self.category_id = category_id
        self.size_id = size_id
        self.volume = volume
        self.price = price

    def __repr__(self):
        return '%s, %s, %s, %s, %s, %s, %s, %s' % (id, self.name, self.producer_id, self.country_id, self.category_id, self.size_id, self.volume, self.price)

def create_session(file_name = 'products.db3'):
    global Base
    engine = create_engine(''.join(('sqlite:///', file_name)))
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

def add_product(product, session):
    '''функция срвнивает категории товаров с существующими и добавляет новые записи в базу данных'''
    name = product.name
    print(name)

    producer_id = session.query(Producer.id).filter(Producer.name == product.producer).first()
    if not producer_id:
        session.add(Producer(name=product.producer))
        session.commit()
        producer_id = session.query(Producer.id).filter(Producer.name == product.producer).first()

    print('producer_id', producer_id)

    country_id = session.query(Country.id).filter(Country.name == product.country).first()
    if not country_id:
        session.add(Country(name=product.country))
        session.commit()
        country_id = session.query(Country.id).filter(Country.name == product.country).first()

    print('country_id', country_id)

    category_id = session.query(Category.id).filter(Category.name == product.category).first()
    if not category_id:
        session.add(Category(name=product.category))
        session.commit()
        category_id = session.query(Category.id).filter(Category.name == product.category).first()

    print('category_id', category_id)

    size_id = session.query(Size.id).filter(Size.size == product.size).first()
    if not size_id:
        session.add(Size(size=product.size))
        session.commit()
        size_id = session.query(Size.id).filter(Size.size == product.size).first()

    print('size_id', size_id)

    volume = product.volume
    print('volume', volume)
    price = product.price
    print('price', price)

    mod_product = Product(name, producer_id[0], country_id[0], category_id[0], size_id[0], volume, price)

    session.add(mod_product)
    session.commit()
    
if __name__ == '__main__':
    session = create_session()
    new_product = product.Product(name = 'shirt', producer = 'adidas', country = 'India', category = 'pants', size = 48, volume = 20, price = 200)
    #session.add(Producer(name = 'adidas'))                              добавление производителя
    # producer = session.query(Producer).filter(Producer.id == 1).one()   #поиск производителя по ид
    # print(producer.name)
    # add_product(new_product, session)
    # d = session.query(Producer.id).filter(Producer.name == 'ass').first()
    # print(d)
    product1 = session.query(Product).filter(Product.id == 2).one()
    print(product1)
    # if ('nike') in session.query(Producer.name):
    #     print('hello')
    # id = session.query(Producer.id).filter(Producer.name == 'nike').first()
    # print(id)
    #producer.name = 'nike'                                              редактирование его
    #session.delete(producer)                                            удалить запись из бд
   # session.commit()                                                     #запись в бд


