#!/bin/bash
cd cocotb_$1
make
cp waveform.vcd ../$1.vcd
