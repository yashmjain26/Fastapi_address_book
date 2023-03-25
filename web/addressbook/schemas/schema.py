from pydantic import BaseModel
from pydantic.types import condecimal

class AddressBookCreate(BaseModel):
    address: str
    city: str
    lat: condecimal(max_digits=9,decimal_places=6)
    long: condecimal(max_digits=9,decimal_places=6)
    

class AddressBookSchema(BaseModel):
    id: int
    address: str
    city: str
    lat: condecimal(max_digits=9,decimal_places=6)
    long: condecimal(max_digits=9,decimal_places=6)
    

    # class Config:
    #     orm_mode = True