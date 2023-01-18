from arknights import (
    locate_image_position_and_click,
    wait_until_operation_completed,
    is_enough_sanity,
    wait_for_seconds,
)
from arknights.screens.home_screen import BATTLE_BUTTON
from arknights.screens.operation_selection_screen import SELECT_FARM_LOBBY_BUTTON
from arknights.screens.farm_item_lobby_screen import (
    FARM_EXP_ENTRY,
    FARM_MONEY_ENTRY,
    FARM_TALENT_BOOK_ENTRY,
    FARM_MEDIC_DEFENDER_ENTRY,
    FARM_GUARD_SPECIALIST_ENTRY,
    FARM_VANGUARD_SUPPORTER_ENTRY,
    FARM_SNIPER_CASTER_ENTRY,
)
from arknights.screens.stage_selection_screen import (
    FARM_CA5_TALENT_BOOK_BUTTON,
    FARM_CE5_MONEY_BUTTON,
    FARM_LS5_EXP_BUTTON,
    PREPARE_OPERATION_BUTTON,
)
from arknights.screens.team_selection_screen import START_OPERATION_BUTTON
from arknights.screens.completed_operation_screen import COMPLETED_OPERATION_INDICATOR


def navigate_to_target_stage(stage: str):
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(BATTLE_BUTTON)
    )
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(SELECT_FARM_LOBBY_BUTTON)
    )
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(FARM_EXP_ENTRY)
    )
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(FARM_LS5_EXP_BUTTON)
    )


def start_farming():
    round = 1

    while True:
        wait_for_seconds(2)
        wait_until_operation_completed(
            lambda: locate_image_position_and_click(PREPARE_OPERATION_BUTTON)
        )
        wait_for_seconds(3)

        if not is_enough_sanity():
            print("Not enough sanity to proceed.")
            break

        wait_until_operation_completed(
            lambda: locate_image_position_and_click(START_OPERATION_BUTTON)
        )

        wait_for_seconds(80)
        wait_until_operation_completed(
            lambda: locate_image_position_and_click(COMPLETED_OPERATION_INDICATOR)
        )

        print(f"Round {round} completed.")
        round += 1
