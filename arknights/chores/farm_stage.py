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
    FARM_CE6_MONEY_BUTTON,
    FARM_LS6_EXP_BUTTON,
    PREPARE_OPERATION_BUTTON,
    FARM_PRB2_SNIPER_CASTER_BUTTON,
    FARM_PRD2_GUARD_SPECIALIST_BUTTON,
    FARM_PRC2_VANGUARD_SUPPORTER_BUTTON,
    FARM_PRA2_DEFENDER_MEDIC_BUTTON,
)
from arknights.screens.team_selection_screen import START_OPERATION_BUTTON
from arknights.screens.completed_operation_screen import COMPLETED_OPERATION_INDICATOR
from arknights.chores.sanity import refill_sanity


stage_map = {
    "ca5": {
        "lobby_icon": FARM_TALENT_BOOK_ENTRY,
        "stage_icon": FARM_CA5_TALENT_BOOK_BUTTON,
    },
    "ce6": {"lobby_icon": FARM_MONEY_ENTRY, "stage_icon": FARM_CE6_MONEY_BUTTON},
    "ls6": {"lobby_icon": FARM_EXP_ENTRY, "stage_icon": FARM_LS6_EXP_BUTTON},
    "prb2": {
        "lobby_icon": FARM_SNIPER_CASTER_ENTRY,
        "stage_icon": FARM_PRB2_SNIPER_CASTER_BUTTON,
    },
    "prd2": {
        "lobby_icon": FARM_GUARD_SPECIALIST_ENTRY,
        "stage_icon": FARM_PRD2_GUARD_SPECIALIST_BUTTON,
    },
    "prc2": {
        "lobby_icon": FARM_VANGUARD_SUPPORTER_ENTRY,
        "stage_icon": FARM_PRC2_VANGUARD_SUPPORTER_BUTTON,
    },
    "pra2": {
        "lobby_icon": FARM_MEDIC_DEFENDER_ENTRY,
        "stage_icon": FARM_PRA2_DEFENDER_MEDIC_BUTTON,
    },
}


def navigate_to_target_stage(stage: str):
    stage_ui = stage_map[stage]

    wait_until_operation_completed(
        lambda: locate_image_position_and_click(BATTLE_BUTTON)
    )
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(SELECT_FARM_LOBBY_BUTTON)
    )
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(stage_ui["lobby_icon"])
    )
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(stage_ui["stage_icon"])
    )


def start_farming(refill_count=0):
    round = 1

    while True:
        wait_for_seconds(2)
        wait_until_operation_completed(
            lambda: locate_image_position_and_click(PREPARE_OPERATION_BUTTON)
        )
        wait_for_seconds(3)

        if not is_enough_sanity():
            if refill_count > 0:
                refill_sanity()
                refill_count -= 1
                print(f"Refill left: {str(refill_count)}")

                wait_until_operation_completed(
                    lambda: locate_image_position_and_click(PREPARE_OPERATION_BUTTON)
                )
            else:
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
