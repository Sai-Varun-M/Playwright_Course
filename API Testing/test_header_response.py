from playwright.sync_api import Playwright

def test_header_in_response(playwright:Playwright):
    request_context = playwright.request.new_context()

    response = request_context.get("https://www.google.com/")

    assert response.status_text == "OK"
    assert response.status == 200

    #Extract all header
    headers = response.headers
    for key, value in headers.items():
        print(f"{key}==>{value}")

    #Validate specific headers
    print("The value of Content Type: ",headers.get("content-type"))

    assert "text/html" in headers.get("content-type")
    assert headers.get("content-encoding") == "gzip"

    assert "server" in headers
    assert "set-cookie" in headers
    