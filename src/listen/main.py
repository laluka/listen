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

from docopt import docopt

def main():
    print("main")

if __name__ == "__main__":
    main()
