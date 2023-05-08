from arknights import locate_image_position_and_click, wait_until_operation_completed
from arknights.screens import NotEnoughSanityScreen


def refill_sanity():
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(
            NotEnoughSanityScreen.REFILL_SANITY_CONFIRM_BUTTON.value
        )
    )


def close_refill_popup():
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(
            NotEnoughSanityScreen.REFILL_SANITY_CLOSE_BUTTON.value
        )
    )
