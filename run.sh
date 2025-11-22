#!/bin/bash
set -e

GREEN='\033[0;32m'
NC='\033[0m'

if [ ! -d ".venv" ]; then
	python3 -m venv .venv
fi

echo -e "${GREEN}Activating Virtual Environment...${NC}"
source .venv/bin/activate

python3 -m pip install --upgrade pip


echo -e "${GREEN}Installing requirements...${NC}"
python3 -m pip install -r requirements.txt


echo -e "${GREEN}Installing requirements...${NC}"
streamlit run app.py