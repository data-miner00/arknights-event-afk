import sys
import argparse
import colorama
from colorama import Fore
from arknights.chores.login import from_login_to_lobby, close_calendar
from arknights.chores.farm_stage import navigate_to_target_stage, start_farming

number_of_rounds = 3
until_sanity_used_up = False
number_of_refills = 0
annihilation_mode = False
farm_stage = ""
skip_login = False
skip_navigation = False
first_login = False

colorama.init(autoreset=True)

if __name__ == "__main__":
    print(Fore.RED      + r'   _____         __          .__       .__     __          ')
    print(Fore.YELLOW   + r'  /  _  \_______|  | __ ____ |__| ____ |  |___/  |_  ______')
    print(Fore.GREEN    + r' /  /_\  \_  __ \  |/ //    \|  |/ ___\|  |  \   __\/  ___/')
    print(Fore.BLUE     + r'/    |    \  | \/    <|   |  \  / /_/  >   Y  \  |  \___ \ ')
    print(Fore.CYAN     + r'\____|__  /__|  |__|_ \___|  /__\___  /|___|  /__| /____  >')
    print(Fore.MAGENTA  + r'        \/           \/    \/  /_____/      \/  Tooling \/ ')
    print()

    parser = argparse.ArgumentParser(
        prog="Arknights CLI",
        description="A CLI that helps on automating the farming workflow for Arknights running on a PC emulator.",
        epilog="arkn/arkn 0.1.0",
    )
    parser.add_argument(
        "-stg",
        "--stage",
        help="the stage to be farmed",
        default="ls6",
        choices=["ls6", "ca5", "ce6", "pra2", "prb2", "prc2", "prd2", "sk5"]
    )
    parser.add_argument(
        "-sl",
        "--skip-login",
        action=argparse.BooleanOptionalAction,
        help="flag to skip the login process from the landing page",
        default=False,
    )
    parser.add_argument(
        "-sn",
        "--skip-navigation",
        action=argparse.BooleanOptionalAction,
        help="flag to skip the navigation from home page to the destination stage",
        default=False,
    )
    parser.add_argument(
        "-fl",
        "--first-login",
        action=argparse.BooleanOptionalAction,
        help="first login of the day",
        default=False,
    )
    parser.add_argument(
        "-rc",
        "--refill-count",
        type=int,
        help="refill count to perform when the sanity runs out",
        default=0,
    )
    parser.add_argument(
        "-lo",
        "--login-only",
        action=argparse.BooleanOptionalAction,
        help="flag to just navigate to lobby screen from login",
        default=False
    )

    args = parser.parse_args()

    skip_login = args.skip_login
    first_login = args.first_login
    login_only = args.login_only

    if skip_login and login_only:
        print('Cannot specify skip login and login only at the same time')
        sys.exit()

    if not skip_login:
        from_login_to_lobby()

        if first_login:
            close_calendar()

        if login_only:
            sys.exit("Login completed")

    skip_navigation = args.skip_navigation
    if not skip_navigation:
        navigate_to_target_stage(args.stage)

    refill_count = args.refill_count
    start_farming(refill_count)
