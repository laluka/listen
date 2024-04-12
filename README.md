# listen

> A simple linux piping tool to listen your pdf/site/doc/blogposts instead of reading them! ^.^

## Setup for User

```bash
# Get your key at https://platform.openai.com/api-keys
export OPENAI_TOKEN=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
sudo apt update && sudo apt install -y wget git
python3 -m pip install --user pipx --upgrade
python3 -m pipx ensurepath
python3 -m pipx install trafilatura  # Website Content Cleanup
python3 -m pipx install pdfminer     # Pdf Content Cleanup
python3 -m pipx install git+https://github.com/laluka/listen

# Generate mp3 file
echo 'Life is beautiful meand "la vie est belle !"' | listen

# Listen live
echo 'Life is beautiful meand "la vie est belle !"' | listen | vlc /dev/stdin

# Website To Voice
trafilatura -u https://www.lesswrong.com/tag/crockers-rules | head  -n 1 | listen

# Pdf To Voice
wget https://www.africau.edu/images/default/sample.pdf -O /tmp/pdf.pdf && pdf2txt.py /tmp/pdf.pdf | head -n 3 | listen
```

---

## Setup for Developer

```bash
git clone git@github.com:laluka/listen.git
mise install
pdm install
export OPENAI_TOKEN=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Generate mp3 file
echo 'Life is beautiful meand "la vie est belle !"' | pdm run listen
# Listen live
echo 'Life is beautiful meand "la vie est belle !"' | pdm run listen

# Before pushing changes, remember to
pipx run black src --line-length 999
```

## Help

```text
Listen by Jonathan & @TheLaluka

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
```

## Potential Improvements

- Multithread text cleanup and TTS process
- Add a cost estimation + y/n prompt
- Fine tune text cleanup prompt
- OCR on images for automated audio-description
- Package the tool & publish on pypi
