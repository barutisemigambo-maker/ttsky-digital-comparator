# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Start clock
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await ClockCycles(dut.clk, 2)

    dut.rst_n.value = 1

    dut._log.info("Testing 8-bit Digital Comparator")

    # -------------------------------------------------
    # Test 1: A > B
    # A = 20, B = 10
    # Expected:
    # uo_out[0] = 1  (A > B)
    # uo_out[1] = 0  (A = B)
    # uo_out[2] = 0  (A < B)
    # -------------------------------------------------

    dut.ui_in.value = 20
    dut.uio_in.value = 10

    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 1
    dut._log.info("PASS: A > B")


    # -------------------------------------------------
    # Test 2: A = B
    # A = 25, B = 25
    # Expected:
    # uo_out[0] = 0
    # uo_out[1] = 1
    # uo_out[2] = 0
    # -------------------------------------------------

    dut.ui_in.value = 25
    dut.uio_in.value = 25

    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 2
    dut._log.info("PASS: A = B")


    # -------------------------------------------------
    # Test 3: A < B
    # A = 10, B = 20
    # Expected:
    # uo_out[0] = 0
    # uo_out[1] = 0
    # uo_out[2] = 1
    # -------------------------------------------------

    dut.ui_in.value = 10
    dut.uio_in.value = 20

    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 4
    dut._log.info("PASS: A < B")


    # -------------------------------------------------
    # Test 4: Maximum value
    # A = 255, B = 0
    # Expected: A > B
    # -------------------------------------------------

    dut.ui_in.value = 255
    dut.uio_in.value = 0

    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 1
    dut._log.info("PASS: 255 > 0")


    # -------------------------------------------------
    # Test 5: Zero comparison
    # A = 0, B = 255
    # Expected: A < B
    # -------------------------------------------------

    dut.ui_in.value = 0
    dut.uio_in.value = 255

    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 4
    dut._log.info("PASS: 0 < 255")


    dut._log.info("ALL COMPARATOR TESTS PASSED!")