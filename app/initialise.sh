#!/bin/bash

echo "Pulling in data"
curl http://benhumphreys.ca/kdict/kdict_dump.json > resources/json/final_dump.json
pip install -r requirements.txt
python test_setup_server.py
echo "\n\nAll tests passed\n\n"
python setup_server.py
