import sys
import logging
from arknights.chores.login import from_login_to_lobby, close_calendar
from arknights.chores.farm_stage import navigate_to_target_stage, start_farming
from arknights.cli import show_banner, parse_args


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s [%(levelname)s]: %(message)s", level=logging.INFO)

    show_banner()

    args = parse_args()

    skip_login = args.skip_login
    first_login = args.first_login
    login_only = args.login_only

    logging.info(f"Session initiated with skip_login - {skip_login}, first_login - {first_login} and login_only - {login_only}")

    if skip_login and login_only:
        logging.error("Cannot specify skip login and login only at the same time")
        sys.exit()

    if not skip_login:
        from_login_to_lobby()

        if first_login:
            close_calendar()

        if login_only:
            logging.info("Login to lobby only has completed.")
            sys.exit()

    skip_navigation = args.skip_navigation
    if not skip_navigation:
        navigate_to_target_stage(args.stage)

    refill_count = args.refill_count
    start_farming(refill_count)
