# listen

> A simple linux piping tool to listen your pdf/site/doc/blogposts instead of reading them! ^.^

## Setup for User

```bash
# Get your key at https://platform.openai.com/api-keys
export OPENAI_TOKEN=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
sudo apt update && sudo apt install -y pipx
pipx ensurepath
pipx install git+https://gitlab.com/TheLaluka/listen.git

# Generate mp3 file
echo "Life is beautiful. La vie est belle."  | listen > "listen-$(date +%s).mp3"

# Listen live
echo "Life is beautiful. La vie est belle."  | listen | vlc /dev/stdin
```

---

## Setup for Developer

```bash
rtx install
pdm install
cp .env.example .env
# Add your OPENAPI_TOKEN in .env
source .env
# Generate mp3 file
echo "Life is beautiful. La vie est belle."  | pdm run listen > "listen-$(date +%s).mp3"
# Listen live
echo "Life is beautiful. La vie est belle."  | pdm run listen | vlc /dev/stdin
```

## Help

```text
listen -h
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
    cat readme.md | listen > out.mp3
    pdm run trafilatura -u https://www.lesswrong.com/tag/crockers-rules | listen > out.mp3
    wget https://www.africau.edu/images/default/sample.pdf -O /tmp/pdf.pdf; pdm run python -c 'from pdfminer.high_level import extract_text; print(extract_text("/tmp/pdf.pdf"))' | listen > out.mp3
```
