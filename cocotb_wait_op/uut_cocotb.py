import random
import cocotb
import itertools

from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Edge, ClockCycles, Timer, Join

import sys
from DataInterface import DataInterface

SIM_UNDERFLOW_READ=True

def init_dut(dut):
    dut.iData <= 0
    dut.iValid <= 0
    dut.iAck <= 0


@cocotb.test()
def timeout_test(dut):

    writer = DataInterface(dut.iClk, dut.iValid, dut.iData, dut.oAck)
    reader = DataInterface(dut.iClk, dut.oValid, dut.oData, dut.iAck)
    clock = Clock(dut.iClk, 10, units="ns") # create a 10 us period clock
    clock = cocotb.fork(clock.start()) # start the clock

    yield FallingEdge(dut.iClk)
    init_dut(dut)

    yield ClockCycles(dut.iClk, 1)

    length = 5
    seed = 0
    prng1 = random.Random(seed)
    prng2 = random.Random(seed)
    pkg1 = (prng1.randint(0, 127) for _ in range (length))
    pkg2 = (prng2.randint(0, 127) for _ in range (length))

    t1 = cocotb.fork(writer.Write(pkg1))
    t2 = cocotb.fork(reader.Read(pkg2, length/2))
    yield Join(t2)
    yield FallingEdge(dut.iClk)
    t2 = cocotb.fork(reader.Read(pkg2))    

    yield ClockCycles(dut.iClk, length)
    clock.kill()
    t1.kill()
    t2.kill()

    assert True

