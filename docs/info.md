<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This is an 8-bit combinational comparator. It compares A on `ui_in` with B on `uio_in`. `uo_out[0]` is high when A is greater than B, `uo_out[1]` when they are equal, and `uo_out[2]` when A is less than B. The remaining `uo_out` bits are low; the bidirectional pins and control signals are unused.

## How to test

From the `test` directory, run `make clean` followed by `make` to run the cocotb tests with Icarus Verilog. The tests check greater-than, equality, less-than, and comparisons involving 0 and 255.

## External hardware

List external hardware used in your project (e.g. PMOD, LED display, etc), if any
