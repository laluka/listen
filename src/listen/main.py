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
    listen http://foo.bar/baz
    listen some_text.txt
    listen some_doc.pdf
"""

import logging
from docopt import docopt
from json import dumps
logger = logging.getLogger(__name__)
VERSION = "0.1.0"

def main():
    logger.setLevel(logging.DEBUG)
    logger.info("[+]Starting")
    arguments = docopt(__doc__, version=f"listen {VERSION}")
    logger.debug(f"Config: {dumps(arguments)}")
    logger.info("Letzgooo")

if __name__ == "__main__":
    main()
