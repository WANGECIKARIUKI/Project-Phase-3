from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *


fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///Products.db')
    Session = sessionmaker(bind=engine)
    session = Session()

# create products
products =[Product(name='Send Money'), 
         Product(name='Trading'), 
         Product(name='Loans'), 
         Product(name='Buy Goods'), 
         Product(name='Deposit'),
         Product(name= 'Withdraw'),
         Product(name= 'Transfer Money from Bank to Mpesa')]

session.add(products)
session.commit()

#create one to many r/ship

for product in products:
    customer= [Customer(name=fake.name()) for i in range(20)]

session.add(customer)
session.commit()

#many to many r/ship
for customer in customer:
    number_of_reviews =random.randint(1,4) #assisgn a random number of reviews to each customer

    review_list =[review(title=fake.word()) for i in range(82)]

    for a in range(review_list):
        reviews=Product(customer_id =customer.id)

session.add(reviews)
session.commit()

session.close()
