#!/bin/bash


GREEN='\033[0;32m'
NC='\033[0m'

if [ ! -d ".venv" ]; then
	python3 -m venv .venv
fi

echo -e "${GREEN}Activating Virtual Environment...${NC}"
source .ven/bin/activate

pip install --upgrade pip


echo -e "${GREEN}Installing requirements...${NC}"
pip install -r requirements.txt


echo -e "${GREEN}Installing requirements...${NC}"
streamlit run app.py