from playwright.sync_api import Playwright

def test_headers_in_response(playwright:Playwright):
    request_context = playwright.request.new_context()

    response = request_context.get("https://www.google.com/")

    assert response.status_text == "OK"
    assert response.status ==200

    cookies = request_context.storage_state()["cookies"]

    for c in cookies:
        print(f"{c['name']}==>{c['value']}==>{c['domain']}")


    for c in cookies:
        if c["name"] == "AEC":
            aec_cookie = c
            break
    assert aec_cookie is not None