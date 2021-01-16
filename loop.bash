#!/bin/bash

export PYTHONPATH=$PYTHONPATH:`pwd`/cocotb_helper
if [ ! -f wavedrom.js ]; then
    wget https://github.com/wavedrom/wavedrom/releases/download/v2.1.2/wavedrom.js
fi

ar=( "normal_op" "wait_op" "underflow_op" )
for i in ${ar[@]}; do
    echo building img for $i
    bash doit.bash $i 2>/dev/null &
done
