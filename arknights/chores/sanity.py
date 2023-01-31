from arknights import (
    locate_image_position_and_click,
    wait_until_operation_completed
)
from arknights.screens.not_enough_sanity_screen import (
    REFILL_SANITY_CONFIRM_BUTTON,
    REFILL_SANITY_CLOSE_BUTTON
)


def refill_sanity():
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(REFILL_SANITY_CONFIRM_BUTTON)
    )


def close_refill_popup():
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(REFILL_SANITY_CLOSE_BUTTON)
    )
