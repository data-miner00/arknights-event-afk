import logging
from arknights import (
    locate_image_position_and_click,
    wait_for_seconds,
    wait_until_operation_completed,
)
from arknights.screens.initialize_screen import START_INDICATOR
from arknights.screens.login_screen_2 import ENTER_GAME_BUTTON
from arknights.screens.home_screen import (
    RECEIVE_REWARD_BUTTON,
    DAILY_REWARD_EXIT_BUTTON,
)


def from_login_to_lobby():
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(START_INDICATOR)
    )
    wait_for_seconds(3)
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(ENTER_GAME_BUTTON)
    )
    logging.info("Done login to lobby.")


def close_calendar():
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(RECEIVE_REWARD_BUTTON)
    )
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(DAILY_REWARD_EXIT_BUTTON)
    )
    logging.info("Closed calendar.")
