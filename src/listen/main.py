"""Listen by Jonathan & @TheLaluka

Usage:
    listen [--debug]
    listen (-h | --help)
    listen (-v | --version)

Options:
    -h --help                       Show help, you are here :)
    -v --version                    Show version info.
    --debug                         Enable debugging output, to... You know... Debug.

Examples:
    cat readme.md | listen
    trafilatura -u https://www.lesswrong.com/tag/crockers-rules | head  -n 1 | listen
    wget https://www.africau.edu/images/default/sample.pdf -O /tmp/pdf.pdf && pdf2txt.py /tmp/pdf.pdf | head -n 3 | listen
"""

import logging
from docopt import docopt
from json import dumps
import sys

from listen.clean_text import clean_text
from listen.speech import to_speech

logger = logging.getLogger("listen")
VERSION = "0.1.0"


def main():
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # Config parsing
    logger.info("Starting listen")
    arguments = docopt(__doc__, version=f"listen {VERSION}")
    if arguments.get("--debug"):
        logger.setLevel(logging.DEBUG)
    logger.debug(f"Config: {dumps(arguments)}")

    # Text clean-up
    text_raw = sys.stdin.read().strip()
    logger.debug(f"text_raw: {text_raw}")
    text_clean = clean_text(text_raw)
    logger.debug(f"text_clean: {text_clean}")

    # TTS
    to_speech(text_clean)


if __name__ == "__main__":
    main()
