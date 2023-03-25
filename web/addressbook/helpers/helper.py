from addressbook.schemas.schema import AddressBookSchema, AddressBookCreate
from addressbook.models.addressbook import AddressBook

def create_new_addressBook(addressBook: AddressBookCreate):
    addressBook_db = AddressBookSchema(
        place_name=addressBook.place_name,
        city=addressBook.city,
        lat=addressBook.lat,
        long=addressBook.long,
    )
    addressBook_db.save()
    return addressBook_db


def get_model_by_id(id: int):
    addressBook_db = AddressBook.get_address_book(id)
    return addressBook_db


def delete_address_book(id: int):
    AddressBook.delete_address_book(id)


def get_all_address_book():
    return AddressBook.get_all()


def update_address_book(address_book_request: AddressBookCreate):
    AddressBookSchema.update_address_book(address_book_request)
