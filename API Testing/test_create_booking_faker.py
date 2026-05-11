from playwright.sync_api import Playwright, expect
from faker import Faker

def test_create_booking(playwright:Playwright):
    base_url = "https://restful-booker.herokuapp.com"

    faker = Faker()
    first_name = faker.first_name()
    last_name = faker.last_name()
    total_price = faker.random_int(min=100, max=5000)
    deposit_paid = faker.boolean()
    checkin_date = faker.date_between(start_date='-1y', end_date='today').isoformat()
    checkout_date = faker.date_between(start_date='today', end_date='+1y').isoformat()
    additional_needs = faker.word()
    request_context = playwright.request.new_context()
    request_body = {
    "firstname" : first_name,
    "lastname" : last_name,
    "totalprice" : total_price,
    "depositpaid" : deposit_paid,
    "bookingdates" : {
        "checkin" : checkin_date,
        "checkout" : checkout_date
    },
    "additionalneeds" : additional_needs
}

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