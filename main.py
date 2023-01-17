from arknights.chores.login import (
    from_login_to_lobby
)
from arknights.chores.farm_stage import (
    navigate_to_target_stage,
    start_farming
)

number_of_rounds = 3
until_sanity_used_up = False
auto_refill_sanity = False
number_of_refills = 0
annihilation_mode = False
farm_stage = ""
skip_login = False

if __name__ == "__main__":
   from_login_to_lobby()
   navigate_to_target_stage("stage")
   start_farming()
