from typing import List
from fastapi import APIRouter, status, HTTPException
from fastapi.encoders import jsonable_encoder
from addressbook.schemas.schema import AddressBookSchema, AddressBookCreate
from geopy import distance
from addressbook.helpers.helper import *

app_router = APIRouter()


@app_router.post(
    "/addressBook", response_model=AddressBookSchema, status_code=status.HTTP_201_CREATED
)
def create_addressBook(addressBook: AddressBookCreate):

    if not ((-90 <= addressBook.lat <= 90) and (-180 <= addressBook.long <= 180)):
        raise HTTPException(
            status_code=404,
            detail=f"Co-ordinate {addressBook.lat,addressBook.long} not in range",
        )

    addressBook_db = create_new_addressBook(addressBook=addressBook)
    return addressBook_db


@app_router.get("/addressBook/{id}", response_model=AddressBookSchema)
def read_addressBook(id: int):

    # get the addressBook item with the given id
    addressBook = get_model_by_id(id)

    # check if addressBook item with given id exists. If not, raise exception and return 404 not found response
    if not addressBook:
        raise HTTPException(
            status_code=404, detail=f"addressBook item with id {id} not found"
        )
    # print(addressBook.long)
    return addressBook


@app_router.put("/addressBook/{id}", response_model=AddressBookSchema)
def update_addressBook(
    id: int,
    addressbook_request: AddressBookCreate,
):

    # get the addressBook item with the given id
    addressBook = get_model_by_id(id)
    if not addressBook:
        raise HTTPException(
            status_code=404, detail=f"addressBook item with id {id} not found"
        )

    if not (
        (-90 <= addressbook_request.lat <= 90)
        and (-180 <= addressbook_request.long <= 180)
    ):
        raise HTTPException(
            status_code=404,
            detail=f"Co-ordinate {addressbook_request.lat,addressbook_request.long} not in range",
        )

    update_item = jsonable_encoder(addressbook_request)
    update_address_book(update_item)


@app_router.delete("/addressBook/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_addressBook(id: int):

    # get the addressBook item with the given id
    addressBook = get_model_by_id(id)

    # if addressBook item with given id exists, delete it from the database. Otherwise raise 404 error
    if not addressBook:
        raise HTTPException(
            status_code=404, detail=f"addressBook item with id {id} not found"
        )
    delete_address_book(id)

    return None


@app_router.get("/addressBook", response_model=List[AddressBookSchema])
def read_addressBook_list():
    addressBook_list = get_all_address_book()
    return addressBook_list


@app_router.get("/neighbors", response_model=List[AddressBookSchema])
def get_address_by_coordinate(dist: float, lat: float, long: float):

    if not ((-90 <= lat <= 90) and (-180 <= long <= 180)):
        raise HTTPException(
            status_code=404,
            detail=f"Co-ordinate {lat,long} not in range",
        )

    center_point_tuple = (lat, long)
    address = []
    addressBook_list = get_all_address_book()

    for data in addressBook_list:
        dis = distance.distance(center_point_tuple, (data.lat, data.long)).km
        if dis <= dist:
            address.append(data)
    return address
