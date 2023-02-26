import pyautogui
import time
from arknights.screens.not_enough_sanity_screen import NOT_ENOUGH_SANITY_INDICATOR_1
from arknights.screens.team_selection_screen import START_OPERATION_BUTTON


def locate_image_position_and_click(image_path: str, confidence=0.7):
    location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
    pyautogui.moveTo(location.x, location.y)
    time.sleep(3)
    pyautogui.leftClick()


def is_enough_sanity() -> bool:
    maybe_enough_sanity = pyautogui.locateCenterOnScreen(
        START_OPERATION_BUTTON, confidence=0.7
    )

    if maybe_enough_sanity is not None:
        return True

    maybe_not_enough_sanity = pyautogui.locateCenterOnScreen(
        NOT_ENOUGH_SANITY_INDICATOR_1, confidence=0.7
    )

    return maybe_not_enough_sanity is None


def wait_for_seconds(seconds: int):
    time.sleep(seconds)


def wait_until_operation_completed(callback):
    while True:
        try:
            callback()
            break
        except Exception:
            wait_for_seconds(1)


def try_locate_image_on_screen(image_path: str, confidence=0.7) -> bool:
    location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)

    return location is not None
