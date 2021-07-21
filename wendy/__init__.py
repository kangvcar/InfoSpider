import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

from wendy.__info__ import APP_NAME, APP_VERSION, COMPANY_NAME

"""
Paths
On Windows Vista+, applications should not write files into Program Files. Programs should use APPDATA

The logic below determines if the program is installed in Program Files or not.
It also determines if the program is has been "frozen" with PyInstaller.

It sets the paths accordingly.

ROOT_PATH: The path to the directory where your application is installed
WRITE_PATH: The path to the directory where your application should write files
"""

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
_program_files = os.environ.get('PROGRAMFILES')
if ROOT_PATH.startswith(_program_files):
    ROOT_PATH = os.path.dirname(ROOT_PATH)
    WRITE_PATH = os.environ['APPDATA']
    WRITE_PATH = str(Path(WRITE_PATH, COMPANY_NAME, APP_NAME))
else:
    WRITE_PATH = ROOT_PATH
    if getattr(sys, 'frozen', False):
        ROOT_PATH = os.path.dirname(ROOT_PATH)

_log_path = str(Path(WRITE_PATH, '{}.log'.format(APP_NAME.lower())))


def get_root_path(*args) -> str:
    """
    Return ROOT program path
    Optionally create a new path from ROOT path when *args are given

    :return: ROOT program path
    """

    return str(Path(ROOT_PATH, *args))


def get_write_path(*args) -> str:
    """
    Get path to write files
    Optionally create a new path from WRITE path when *args are given

    :return: Path to write files
    """

    return str(Path(WRITE_PATH, *args))


def _create_write_path():
    """
    Create WRITE_PATH
    """

    path = get_write_path()
    Path(path).mkdir(parents=True, exist_ok=True)


_create_write_path()
# --

# -- Logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s %(name)-6s %(levelname)-8s %(message)s')

# Console logging
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# File logging
handler = RotatingFileHandler(_log_path, mode='a', maxBytes=10 * 1024 * 1024, backupCount=1, encoding='utf-8', delay=0)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

logger.setLevel(logging.DEBUG)
# --

logger.info("{} v{}".format(APP_NAME, APP_VERSION))
logger.debug("_program_files: '{}'".format(_program_files))
logger.debug("log path: '{}'".format(_log_path))
logger.info("ROOT_PATH: '{}'".format(ROOT_PATH))
logger.info("WRITE_PATH: '{}'".format(WRITE_PATH))