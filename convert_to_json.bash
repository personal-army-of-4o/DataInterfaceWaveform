#!/bin/bash
sed -i -e 's/U/x/g' $1.vcd
python3 convert_to_json.py $1 $2
