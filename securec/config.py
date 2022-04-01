import os
import sys

cwpath = None
firmwarepath = None
for cwpath in (
    [
        "~/chipwhisperer",
        "~/work/chipwhisperer",
    ]
    + list(
        os.path.join(os.path.dirname(__file__), p)
        for p in (
            "../..",
            "../../chipwhisperer",
            "../../../chipwhisperer",
        )
    )
    + [r"C:\cw\cw\home\portable\chipwhisperer"]
):
    firmwarepath = os.path.abspath(
        os.path.join(os.path.expanduser(cwpath), "hardware/victims/firmware")
    )
    if os.path.exists(firmwarepath):
        break

if not os.path.exists(firmwarepath):
    raise ValueError("FIRMWAREPATH not found")

if "win" in sys.platform:
    os.environ["PATH"] += ";" + ";".join(
        (
            r"C:\cw\cw\usr\bin",
            r"C:\cw\cw\home\portable\armgcc\gcc-arm-none-eabi-10-2020-q4-major\bin",
            r"C:\cw\cw\home\portable\avrgcc\avr-gcc-10.1.0-x64-windows\bin",
        )
    )


print_output = True
"""Print output instead of returning. Looks better in Notebook."""

debug = False
"""Print debug output."""

scope = None
"""ChipWhisperer scope."""

target = None
"""ChipWhisperer target."""

platform = None
"""ChipWhisperer platform."""
