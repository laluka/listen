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
    cat readme.md | listen
    pdm run trafilatura -u https://www.lesswrong.com/tag/crockers-rules | listen
    wget https://www.africau.edu/images/default/sample.pdf -O /tmp/pdf.pdf; pdm run python -c 'from pdfminer.high_level import extract_text; print(extract_text("/tmp/pdf.pdf"))' | listen
"""

import logging
from docopt import docopt
from json import dumps
logger = logging.getLogger(__name__)
VERSION = "0.1.0"

def main():
    # Configure logger to output to stdout
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Set the logging level
    logger.setLevel(logging.DEBUG)
    logger.info("[+]Starting")
    arguments = docopt(__doc__, version=f"listen {VERSION}")
    logger.debug(f"Config: {dumps(arguments)}")
    logger.info("Letzgooo")

if __name__ == "__main__":
    main()
