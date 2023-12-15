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

from listen.clean_text import clean_text
from listen.speech import to_speech

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

    txt = """What is kong & why we’re relying on it.
    If you’re an occasional reader of the manomano-tech Medium blog, dxjksjdpijpi
    you might already be familiar with Kong API Gateway thanks to previous ....
    articles more dhuen developer-focused like this one: Improve your Kong Plugin Experience (https://medium.com/manomano-tech/improve-your-kong-plugin-experience-2e4bad9d6178?source=friends_link&sk=e362d5926727f4eac35ff76584060048).
    If not, you can either read HD__(W past blog posts as an introduction,
    or consider Kong as a “huge black-box that uses nginx & lua to create a clean approach to reverse-proxying” 🙂"""

    text = clean_text(txt)

    to_speech(text)


if __name__ == "__main__":
    main()
