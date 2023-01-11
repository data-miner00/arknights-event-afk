import pyautogui
import time


def locate_image_position_and_click(image_path: str):
    x, y = pyautogui.locateCenterOnScreen(image_path, confidence=0.7)
    pyautogui.moveTo(x, y)
    time.sleep(3)
    pyautogui.leftClick()


def click_on_prepare_operation_button():
    locate_image_position_and_click("images/arkn_start_operation.png")


def click_on_start_operation_button():
    locate_image_position_and_click("images/arkn_start_operation_button.png")


def click_on_stage_completed_indicator():
    locate_image_position_and_click("images/arkn_stage_completed_indicator_2.png")


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
