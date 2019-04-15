from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import Base, User, Address


engine = create_engine('postgresql+psycopg2://codechallenge:secret_password@localhost:5432/codechallenge')  # nopep8
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_users():
    for i in range(1, 11):
        user = User(name=f"user_{i}",
                    email=f"user_{i}@example.com",
                    birthdate=f"12-12-2000",
                    address_id=i)
        session.add(user)

    session.commit()

    return


def add_addresses():
    for i in range(1, 11):
        address = Address(street=f"street_{i}",
                          state=f"state_{i}",
                          city=f"city_{i}",
                          country=f"country_{i}",
                          zip=i+15320)
        session.add(address)

    session.commit()

    return


add_addresses()
add_users()
