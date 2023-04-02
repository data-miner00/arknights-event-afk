import argparse
import colorama
from colorama import Fore


def show_banner():
    colorama.init(autoreset=True)

    print(Fore.RED      + r'   _____         __          .__       .__     __          ')
    print(Fore.YELLOW   + r'  /  _  \_______|  | __ ____ |__| ____ |  |___/  |_  ______')
    print(Fore.GREEN    + r' /  /_\  \_  __ \  |/ //    \|  |/ ___\|  |  \   __\/  ___/')
    print(Fore.BLUE     + r'/    |    \  | \/    <|   |  \  / /_/  >   Y  \  |  \___ \ ')
    print(Fore.CYAN     + r'\____|__  /__|  |__|_ \___|  /__\___  /|___|  /__| /____  >')
    print(Fore.MAGENTA  + r'        \/           \/    \/  /_____/      \/  Tooling \/ ')
    print()


def parse_args():
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
        choices=["ls6", "ca5", "ce6", "pra1", "pra2", "prb1", "prb2", "prc1", "prc2", "prd1", "prd2", "sk5"],
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
        default=False,
    )

    return parser.parse_args()
