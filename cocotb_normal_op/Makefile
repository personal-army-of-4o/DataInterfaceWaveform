TOPLEVEL_LANG ?= vhdl
SIM ?= ghdl
SIM_ARGS ?= --wave=waveform.ghw --vcd=waveform.vcd

PWD=$(shell pwd)

ifeq ($(TOPLEVEL_LANG),vhdl)
    VHDL_SOURCES = $(PWD)/../hdl/src/uut.vhd
else
    $(error "A valid value (verilog or vhdl) was not provided for TOPLEVEL_LANG=$(TOPLEVEL_LANG)")
endif

TOPLEVEL := uut
MODULE   := $(TOPLEVEL)_cocotb

include $(shell cocotb-config --makefiles)/Makefile.sim
