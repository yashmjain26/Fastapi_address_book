from sqlalchemy import Column, Integer, String, Numeric
from db import Base, session
from fastapi import Depends


class AddressBook(Base):
    __tablename__ = "addressbook"
    id = Column(Integer, primary_key=True)
    address = Column(String(256))
    city = Column(String(256))
    lat = Column(Numeric(9, 6))
    long = Column(Numeric(9, 6))

    def __init__(
        self, id: int, address: str, city: str, lat: float, long: float
    ) -> None:
        self.id = id
        self.place_name = address
        self.city = city
        self.lat = lat
        self.long = long

    def save(self):
        session.add(self)
        session.commit()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def get_address_book(cls, id: int):
        return session.query(cls).get(id)

    @classmethod
    def delete_address_book(cls, id: int):
        session.delete(session.query(cls).get(id))
        session.commit()

    @classmethod
    def update_address_book(cls, address_book):
        addressBook = session.query(cls).get(id)
        addressBook.address = address_book.get("address", addressBook.address)
        addressBook.city = address_book.get("city", addressBook.city)
        addressBook.lat = address_book.get("lat", addressBook.lat)
        addressBook.long = address_book.get("long", addressBook.long)
        session.commit()
