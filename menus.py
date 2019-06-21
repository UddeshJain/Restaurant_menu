from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# session.commit(). If you're not happy about the changes, you can
session = DBSession()

# Create dummy user
User1 = User(name="admin", email="uddesh.jain88@gmail.com")
session.add(User1)
session.commit()

# Menu for Rajula's Kitchen
restaurant1 = Restaurant(name="Alfanzo", user_id="1")

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Cheese Pasta",
                     description="Pasta with lots of cheese"
                     "Cheese and butter",
                     price="$3.99", restaurant=restaurant1, user_id=1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Veg Soup",
                     description="Healthy Soup with"
                     "lots of vegetables",
                     price="$2.99",  restaurant=restaurant1, user_id=1)

session.add(menuItem2)
session.commit()


menuItem3 = MenuItem(name="Garlic Bread",
                     description="Soft and crispy bread"
                     "with garlic paste on it",
                     price="$5.50", restaurant=restaurant1, user_id=1)

session.add(menuItem3)
session.commit()


# Menu for Biryani Pot
restaurant2 = Restaurant(name="Buzztime")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="French fries",
                     description="Soft and crispy fries made with potato",
                     price="$4.99", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Veg Burger",
                     description="Soft and big burger"
                     "with green vegetables",
                     price="$5.99",  restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Oreo Shake",
                     description="Tasty milk share"
                     "made with Oreo.",
                     price="$5.99", restaurant=restaurant2)

session.add(menuItem3)
session.commit()


print("Added menu items!")
