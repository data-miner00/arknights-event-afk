import logging
import sys
import os
from datetime import datetime


def configureLogger():
    now = datetime.today().strftime("%d-%m-%Y")
    log_filename = now + ".log"

    createFileIfNotExist(log_filename)

    logFormatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")
    rootLogger = logging.getLogger()

    rootLogger.setLevel(logging.INFO)

    fileHandler = logging.FileHandler("logs/" + log_filename)
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

    return rootLogger


def createFileIfNotExist(filename: str):
    filepath = "logs/"

    if not os.path.isdir(filepath):
        os.makedirs(filepath)

    if not os.path.exists(filepath + filename):
        with open(filepath + filename, "w") as f:
            f.write("")
