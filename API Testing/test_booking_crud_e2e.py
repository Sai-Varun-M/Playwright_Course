"""
1) create booking(post) ---> booking id
2) get booking detials (get) - by id, by names, by date
3) create token (post)
4) partial update booking (patch)
5) full update booking (put)
6) delete booking (delete)
"""

import json
from playwright.sync_api import Playwright
import pytest

base_url = "https://restful-booker.herokuapp.com"

def read_json(file_path):
    file = open(file_path,"r")
    return json.load(file)

# Fixture - creates playwright request context
@pytest.fixture(scope="session")
def request_context(playwright:Playwright):
    context = playwright.request.new_context()
    yield context
    context.dispose()
    

# 1) create booking(post) ---> booking id
def test_create_booking(request_context):
    data = read_json("testdata/post_request.json")
    response =request_context.post(f"{base_url}/booking",data = data)
    assert response.ok
    assert response.status == 200
    response_body = response.json()
    print("Create Booking Response:", response_body)
    assert "bookingid" in response_body
    assert "booking" in response_body
    booking = response_body["booking"]
    assert booking["firstname"] == data["firstname"]
    assert booking["lastname"] == data["lastname"]

    global booking_id
    booking_id = response_body["bookingid"]



# 2) get booking detials (get) - by id, by names, by date
def test_get_booking_by_id(request_context):
    response = request_context.get(f"{base_url}/booking/{booking_id}")

    assert response.ok
    assert response.status == 200
    response_body = response.json()
    print(f"Booking details fetched by {booking_id}:",response_body)

    assert "firstname" in response_body
    assert "lastname" in response_body

def test_get_booking_by_name(request_context):
    names_params = {"firstname": "Jim", "lastname": "Brown"}
    response = request_context.get(f"{base_url}/booking",params = names_params)
    assert response.ok
    assert response.status == 200
    response_body = response.json()
    print(f"Booking details fetched by {names_params}:",response_body)

def test_get_booking_by_date(request_context):
    date_params = {"checkin": "2014-03-13", "checkout": "2014-05-21"}
    response = request_context.get(f"{base_url}/booking",params = date_params)
    assert response.ok
    assert response.status == 200
    response_body = response.json()
    print(f"Booking details fetched by {date_params}:",response_body)



# 3) create token (post)
def test_create_token(request_context):
    data = read_json("testdata/token_request_body.json")
    response = request_context.post(f"{base_url}/auth", data= data)
    assert response.ok
    assert response.status == 200
    response_body = response.json()
    print("Token Response:", response_body)

    assert "token" in response_body
    global token 
    token = response_body["token"]
    assert len(token) > 5



# 4) partial update booking (patch)
def test_partial_update(request_context):
    data = read_json("testdata/patch_request_body.json")
    response = request_context.patch(f"{base_url}/booking/{booking_id}",data=data, headers= {"Cookie":f"token={token}"})
    assert response.ok
    assert response.status == 200
    response_body = response.json()
    print(f"Partial Update Reponse for booking id {booking_id}", response_body)
    for key in data.keys():
        assert key in response_body



# Full update booking (put)
def test_full_update(request_context):
    data = read_json("testdata/put_request_body.json")
    response = request_context.patch(f"{base_url}/booking/{booking_id}",data=data, headers= {"Cookie":f"token={token}"})
    assert response.ok
    assert response.status == 200
    response_body = response.json()
    print(f"Partial Update Reponse for booking id {booking_id}", response_body)
    for key in data.keys():
        assert key in response_body
        assert response_body[key] == data[key]
    assert response_body["firstname"] == data["firstname"]
    assert response_body["lastname"] == data["lastname"]


# delete booking (delete)
def test_delete(request_context):
    response = request_context.delete(f"{base_url}/booking/{booking_id}", headers={"Cookie":f"token={token}"})
    assert response.ok
    assert response.status == 201
    print(f"Booking deleted succesfully-->{booking_id}")