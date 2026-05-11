# Data : Hard coded data inside the test

from playwright.sync_api import Playwright, expect


def test_create_booking(playwright:Playwright):
    base_url = "https://restful-booker.herokuapp.com"

    request_context = playwright.request.new_context()
    request_body = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    #load data from external file
    response = request_context.post(f"{base_url}/booking", data = request_body)

    response_body = response.json()

    # validation
    assert response.ok
    assert response.status == 200
    
    print("Response Body : ", response_body)

    assert "bookingid" in response_body
    assert "booking" in response_body

    booking = response_body["booking"]
    assert booking["firstname"] == request_body["firstname"]