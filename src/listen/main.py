"""listen by Jonathan & @TheLaluka

Usage:
    listen [--debug]
    listen (-h | --help)
    listen (-v | --version)

Options:
    -h --help                       Show help, you are here :)
    -v --version                    Show version info.
    --debug                         Enable debugging output, to... Tou know... Debug.

Examples:
    cat readme.md | listen > out.mp3
    trafilatura -u https://www.lesswrong.com/tag/crockers-rules | head  -n 1 | listen > out.mp3
    wget https://www.africau.edu/images/default/sample.pdf -O /tmp/pdf.pdf && pdf2txt.py /tmp/pdf.pdf | head -n 3 | listen > out.mp3
"""

import logging
from docopt import docopt
from json import dumps
import sys

from listen.clean_text import clean_text
from listen.speech import to_speech

logger = logging.getLogger(__name__)
VERSION = "0.1.0"


def main():
    # Configure logger to output to stdout
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Set the logging level
    logger.setLevel(logging.DEBUG)
    logger.info("[+]Starting")
    arguments = docopt(__doc__, version=f"listen {VERSION}")
    logger.debug(f"Config: {dumps(arguments)}")

    text_raw = sys.stdin.read().strip()
    logger.debug(f"text_raw: {text_raw}")
    text_clean = clean_text(text_raw)
    logger.debug(f"text_clean: {text_clean}")

    to_speech(text_clean)


if __name__ == "__main__":
    main()
