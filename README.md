# listen

## Setup & Use

```bash
rtx install
pdm install
cp .env.example .env
# Add your OPENAPI_TOKEN in .env
source .env
# Generate mp3 file
echo coucou | pdm run listen > out.mp3
# Listen live
echo coucou | pdm run listen | vlc /dev/stdin
```

## Help

```text
pdm run listen -h
2023-12-15 16:24:30,717 - listen.main - INFO - [+]Starting
listen by Jonathan & @TheLaluka

Usage:
    listen [--debug]
    listen (-h | --help)
    listen (-v | --version)

Options:
    -h --help                       Show help, you are here :)
    -v --version                    Show version info.
    --debug                         Enable debugging output, to... Tou know... Debug.

Examples:
    cat readme.md | pdm run listen > out.mp3
    pdm run trafilatura -u https://www.lesswrong.com/tag/crockers-rules | pdm run listen > out.mp3
    wget https://www.africau.edu/images/default/sample.pdf -O /tmp/pdf.pdf; pdm run python -c 'from pdfminer.high_level import extract_text; print(extract_text("/tmp/pdf.pdf"))' | pdm run listen > out.mp3
```