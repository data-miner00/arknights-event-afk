import pyautogui
import time


def locate_image_position_and_click(image_path: str):
    location = pyautogui.locateCenterOnScreen(image_path, confidence=0.7)
    pyautogui.moveTo(location.x, location.y)
    time.sleep(3)
    pyautogui.leftClick()


def is_enough_sanity() -> bool:
    maybe_enough_sanity = pyautogui.locateCenterOnScreen(
        "images/arkn_start_operation_button.png", confidence=0.7
    )

    if maybe_enough_sanity is not None:
        return True

    maybe_not_enough_sanity = pyautogui.locateCenterOnScreen(
        "images/arkn_not_enuf_sanity_indicator_1.png", confidence=0.7
    )

    return maybe_not_enough_sanity is None


def wait_for_seconds(seconds: int):
    time.sleep(seconds)


def wait_until_operation_completed(callback):
    while True:
        try:
            callback()
            break
        except Exception as e:
            wait_for_seconds(1)
