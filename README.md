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
