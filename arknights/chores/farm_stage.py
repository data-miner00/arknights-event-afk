import logging
from arknights import (
    locate_image_position_and_click,
    wait_until_operation_completed,
    is_enough_sanity,
    wait_for_seconds,
    try_locate_image_on_screen,
)
from arknights.screens import (
    HomeScreen,
    OperationSelectionScreen,
    FarmItemLobbyScreen,
    StageSelectionScreen,
    TeamSelectionScreen,
    CompletedOperationScreen,
)
from arknights.chores.sanity import refill_sanity


stage_map = {
    "ca5": {
        "lobby_icon": FarmItemLobbyScreen.FARM_TALENT_BOOK_ENTRY.value,
        "stage_icon": StageSelectionScreen.FARM_CA5_TALENT_BOOK_BUTTON.value,
        "cost": 30,
    },
    "ce6": {
        "lobby_icon": FarmItemLobbyScreen.FARM_MONEY_ENTRY.value,
        "stage_icon": StageSelectionScreen.FARM_CE6_MONEY_BUTTON.value,
        "cost": 36,
    },
    "ls6": {
        "lobby_icon": FarmItemLobbyScreen.FARM_EXP_ENTRY.value,
        "stage_icon": StageSelectionScreen.FARM_LS6_EXP_BUTTON.value,
        "cost": 36,
    },
    "prb1": {
        "lobby_icon": FarmItemLobbyScreen.FARM_SNIPER_CASTER_ENTRY.value,
        "stage_icon": StageSelectionScreen.FARM_PRB1_SNIPER_CASTER_BUTTON.value,
        "cost": 18,
    },
    "prb2": {
        "lobby_icon": FarmItemLobbyScreen.FARM_SNIPER_CASTER_ENTRY.value,
        "stage_icon": StageSelectionScreen.FARM_PRB2_SNIPER_CASTER_BUTTON.value,
        "cost": 36,
    },
    "prd1": {
        "lobby_icon": FarmItemLobbyScreen.FARM_GUARD_SPECIALIST_ENTRY.value,
        "stage_icon": StageSelectionScreen.FARM_PRD1_GUARD_SPECIALIST_BUTTON.value,
        "cost": 18,
    },
    "prd2": {
        "lobby_icon": FarmItemLobbyScreen.FARM_GUARD_SPECIALIST_ENTRY.value,
        "stage_icon": StageSelectionScreen.FARM_PRD2_GUARD_SPECIALIST_BUTTON.value,
        "cost": 36,
    },
    "prc1": {
        "lobby_icon": FarmItemLobbyScreen.FARM_VANGUARD_SUPPORTER_ENTRY.value,
        "stage_icon": StageSelectionScreen.FARM_PRC1_VANGUARD_SUPPORTER_BUTTON.value,
        "cost": 18,
    },
    "prc2": {
        "lobby_icon": FarmItemLobbyScreen.FARM_VANGUARD_SUPPORTER_ENTRY.value,
        "stage_icon": StageSelectionScreen.FARM_PRC2_VANGUARD_SUPPORTER_BUTTON.value,
        "cost": 36,
    },
    "pra1": {
        "lobby_icon": FarmItemLobbyScreen.FARM_MEDIC_DEFENDER_ENTRY.value,
        "stage_icon": StageSelectionScreen.FARM_PRA1_DEFENDER_MEDIC_BUTTON.value,
        "cost": 18,
    },
    "pra2": {
        "lobby_icon": FarmItemLobbyScreen.FARM_MEDIC_DEFENDER_ENTRY.value,
        "stage_icon": StageSelectionScreen.FARM_PRA2_DEFENDER_MEDIC_BUTTON.value,
        "cost": 36,
    },
    "sk5": {
        "lobby_icon": FarmItemLobbyScreen.FARM_CARBON_ENTRY.value,
        "stage_icon": StageSelectionScreen.FARM_SK5_CARBON_BUTTON.value,
        "cost": 36,
    },
}


def navigate_to_target_stage(stage: str):
    stage_ui = stage_map[stage]

    wait_until_operation_completed(
        lambda: locate_image_position_and_click(HomeScreen.BATTLE_BUTTON.value)
    )
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(
            OperationSelectionScreen.SELECT_FARM_LOBBY_BUTTON.value
        )
    )
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(stage_ui["lobby_icon"])
    )
    wait_until_operation_completed(
        lambda: locate_image_position_and_click(stage_ui["stage_icon"], confidence=0.98)
    )


def start_farming(refill_count=0):
    round = 1

    while True:
        wait_for_seconds(2)
        wait_until_operation_completed(
            lambda: locate_image_position_and_click(
                StageSelectionScreen.PREPARE_OPERATION_BUTTON.value
            )
        )
        wait_for_seconds(3)

        if not is_enough_sanity():
            if refill_count > 0:
                refill_sanity()
                refill_count -= 1
                logging.info(f"Refill left: {str(refill_count)}")

                wait_until_operation_completed(
                    lambda: locate_image_position_and_click(
                        StageSelectionScreen.PREPARE_OPERATION_BUTTON.value
                    )
                )
            else:
                logging.warning("Not enough sanity to proceed. Program exited.")
                break

        wait_until_operation_completed(
            lambda: locate_image_position_and_click(
                TeamSelectionScreen.START_OPERATION_BUTTON.value
            )
        )

        wait_for_seconds(80)

        while True:
            wait_for_seconds(2)
            levelUp = try_locate_image_on_screen(
                CompletedOperationScreen.LEVEL_UP_INDICATOR.value
            )

            if levelUp:
                logging.warning("Level up detected. Closing the popup...")
                locate_image_position_and_click(
                    CompletedOperationScreen.LEVEL_UP_INDICATOR.value
                )

            completedOperation = try_locate_image_on_screen(
                CompletedOperationScreen.COMPLETED_OPERATION_INDICATOR.value
            )

            if completedOperation:
                break

        wait_until_operation_completed(
            lambda: locate_image_position_and_click(
                CompletedOperationScreen.COMPLETED_OPERATION_INDICATOR.value
            )
        )

        logging.info(f"Round {round} completed.")
        round += 1
