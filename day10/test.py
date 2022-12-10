from pathlib import Path
import unittest
import lib


with open(Path(__file__).parent.joinpath("data/test_input.txt"), 'r', encoding="utf-8") as f:
    test_input_lines = f.read().split("\n")
with open(Path(__file__).parent.joinpath("data/test_input2.txt"), 'r', encoding="utf-8") as f:
    test_input_lines2 = f.read().split("\n")


tc = unittest.TestCase()
