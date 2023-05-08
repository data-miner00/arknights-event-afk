import logging
from arknights import (
    locate_image_position_and_click,
    try_locate_image_on_screen,
    wait_for_seconds,
    wait_until_operation_completed,
)
from arknights.screens import InitializeScreen, LoginScreen1, LoginScreen2, HomeScreen


def from_login_to_lobby():
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(InitializeScreen.START_INDICATOR.value)
    )
    wait_for_seconds(3)

    while True:
        facebook_login_btn = try_locate_image_on_screen(
            LoginScreen1.FACEBOOK_LOGIN_BUTTON.value
        )
        enter_game_btn = try_locate_image_on_screen(
            LoginScreen2.ENTER_GAME_BUTTON.value
        )

        if facebook_login_btn or enter_game_btn:
            break

        wait_for_seconds(3)

    if facebook_login_btn:
        logging.info("Logging in with Facebook.")
        wait_until_operation_completed(
            lambda: locate_image_position_and_click(
                LoginScreen1.FACEBOOK_LOGIN_BUTTON.value
            )
        )
        wait_for_seconds(3)

    wait_until_operation_completed(
        lambda: locate_image_position_and_click(LoginScreen2.ENTER_GAME_BUTTON.value)
    )
    logging.info("Done login to lobby.")


def close_calendar():
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(HomeScreen.RECEIVE_REWARD_BUTTON.value)
    )
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(
            HomeScreen.DAILY_REWARD_EXIT_BUTTON.value
        )
    )
    logging.info("Closed calendar.")
