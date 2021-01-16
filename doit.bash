#!/bin/bash

rm $1_done
bash test.bash $1
bash convert_to_json.bash $1 1
nodejs wavedrom -i $1.json > $1.svg
rsvg-convert --format=png --background-color=white $1.svg -o $1.png
if [ `which publish` == "" ]; then
    echo "skipping post-build hook"
else
    publish $1.png
fi
touch $1_done
