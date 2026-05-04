from playwright.sync_api import Page, expect  # pyright: ignore[reportMissingImports]

def test_frames(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frames= page.frames
    print("Number of frames:",len(frames))

    #Frame 1
    frame1 = page.frame_locator("frame[src='frame_1.html']")
    # frame1 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_1.html")
    page.wait_for_timeout(3000)