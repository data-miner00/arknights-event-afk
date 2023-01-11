import pyautogui
import time
from arknights import (
    click_on_prepare_operation_button,
    click_on_start_operation_button,
    click_on_stage_completed_indicator,
    is_enough_sanity,
)


if __name__ == "__main__":
    round = 1

    while True:
        time.sleep(2)
        while True:
            try:
                click_on_prepare_operation_button()
                break
            except Exception as e:
                print(e)
                time.sleep(1)

        time.sleep(3)
        if not is_enough_sanity():
            print("Not enough sanity to proceed.")
            break

        while True:
            try:
                click_on_start_operation_button()
                break
            except Exception as e:
                print(e)
                time.sleep(1)

        time.sleep(80)

        while True:
            try:
                click_on_stage_completed_indicator()
                break
            except Exception as e:
                time.sleep(1)

        print(f"Round {round} completed.")
        round += 1
