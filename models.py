from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///Products.db", echo=True)
Session = sessionmaker(bind=engine)

session = Session()
Base = declarative_base()

Customer = Table(
    'Customer',
    Base.metadata,
    Column('customer_id', ForeignKey('customer.id')),
    Column('product_id', ForeignKey('product.id')),
    extend_existing=True
)

class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer(), primary_key=True)
    fullname = Column(String())
    email = Column(String(), unique=True ,nullable=False)

    reviews = relationship('reviews', back_populates='customers')
    product = relationship('product', back_populates='customers')

    def __repr__(self):
        return f"Customer (id = {self.id}, fullname = {self.username}, email = {self.email})"
    
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer(), primary_key=True)
    book = Column(String(), nullable=False)
    

    reviews = relationship('reviews', back_populates='refs')
    customers = relationship('customers', back_populates='products')

    @classmethod
    def product(cls):
        product_list = [list["name"] for list in product_list]
        print(product_list)
    
    def __repr__(self):
        return f"Product (id = {self.id}, Product_name = {self.list})"

class review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    content = Column(String())

    customer_id = Column(Integer(), ForeignKey('customer.id'))
    product_id = Column(Integer(), ForeignKey('product.id'))

    user = relationship('Customer', back_populates='reviews')
    refs = relationship('Product', back_populates='reviews')


    def __repr__(self):
        return f"reviews (id = {self.id}, title = {self.title})"
    
Base.metadata.create_all(engine)