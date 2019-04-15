from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    street = Column(String(100))
    state = Column(String(50))
    city = Column(String(50))
    country = Column(String(50))
    zip = Column(String(20))

    # JSON serialization
    @property
    def serialize(self):
        return {
            "id": self.id,
            "street": self.street,
            "state": self.state,
            "city": self.city,
            "country": self.country
        }


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    birthdate = Column(String(10), nullable=False)
    # ForeignKey
    address_id = Column(Integer, ForeignKey("address.id"))
    address = relationship(Address)

    # JSON serialization
    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "birthdate": self.birthdate,
            "address": {
                "id": self.address.id,
                "street": self.address.street,
                "state": self.address.state,
                "city": self.address.city,
                "country": self.address.country
            }
        }


engine = create_engine('postgresql+psycopg2://codechallenge:secret_password@localhost:5432/codechallenge')  # nopep8

Base.metadata.create_all(engine)
