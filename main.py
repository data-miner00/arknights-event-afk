import argparse
from arknights.chores.login import from_login_to_lobby
from arknights.chores.farm_stage import navigate_to_target_stage, start_farming

number_of_rounds = 3
until_sanity_used_up = False
auto_refill_sanity = False
number_of_refills = 0
annihilation_mode = False
farm_stage = ""
skip_login = False
skip_navigation = False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('stage', metavar='stage', type=str, help='the stage to be farmed')
    parser.add_argument('-sl', '--skip-login', action=argparse.BooleanOptionalAction, help='flag to skip the login process from the landing page', default=False)
    parser.add_argument('-sn', '--skip-navigation', action=argparse.BooleanOptionalAction, help='flag to skip the navigation from home page to the destination stage', default=False)

    args = parser.parse_args()

    skip_login = args.skip_login
    if not skip_login:
        from_login_to_lobby()

    skip_navigation = args.skip_navigation
    if not skip_navigation:
        navigate_to_target_stage(args.stage)

    start_farming()
