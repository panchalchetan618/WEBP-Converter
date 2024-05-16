# Convert multiple images into `.webp`

Currently it supports `.png`, `.jpg` and `.jpeg` only, more'll be added soon...

> [!NOTE]
> This project is open source, please raise PRs for further improvements

## How it works?
1. It'll ask you for the path to the folder containing Images which needs to be converted
2. Then, it'll try converting all Images one by one and save in the same provided folder

## Requirements
1. Python 3

## How to setup locally
1. Clone this Repo and get into the root directory by these commands
```
git clone https://github.com/panchalchetan618/WEBP-Converter.git
cd WEBP-Converter/
```

2. Create & Activate Virtual Environment using these commands
```
python3 -m venv .venv
source .venv/bin/activate
```

3. Install requirements
```
pip install -r requirements.txt
```

4. Finally, run the main file
```
python main.py
```
