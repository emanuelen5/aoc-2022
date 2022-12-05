from pathlib import Path
import unittest
import lib


with open(Path(__file__).parent.joinpath("data/test_input.txt"), 'r', encoding="utf-8") as f:
    test_input = [line.strip() for line in f.readlines()]


tc = unittest.TestCase()
