from pathlib import Path
import unittest
import lib


with open(Path(__file__).parent.joinpath("data/test_input.txt"), 'r', encoding="utf-8") as f:
    test_input_lines = f.read().split("\n")


tc = unittest.TestCase()

root_dir = lib.Dir.create_root()
tc.assertEqual(0, root_dir.calculate_size())

dir_a = root_dir.add_subdir("a")
dir_b = root_dir.add_subdir("b")
dir_a.add_file("b", 1)
dir_a.add_file("c", 2)
tc.assertEqual(3, root_dir.calculate_size())
dir_b.add_file("b", 1)
dir_b.add_file("c", 2)
tc.assertEqual(6, root_dir.calculate_size())

cwd = lib.CLI(root_dir)
tc.assertEqual(root_dir, cwd.cwd_)
cwd.cd("a")
tc.assertEqual(dir_a, cwd.cwd_)
cwd.cd("..")
tc.assertEqual(root_dir, cwd.cwd_)
cwd.cd("b")
tc.assertEqual(dir_b, cwd.cwd_)


tc.assertEqual(lib.CommandCd("/"), lib.parse_line(test_input_lines[0]))
tc.assertEqual(lib.CommandLs(), lib.parse_line(test_input_lines[1]))
tc.assertEqual(lib.CommandCd("a"), lib.parse_line(test_input_lines[6]))
tc.assertEqual(lib.CommandCd("d"), lib.parse_line(test_input_lines[17]))
tc.assertEqual(lib.ListingDir("d"), lib.parse_line(test_input_lines[5]))
tc.assertEqual(lib.ListingFile(29116, "f"), lib.parse_line(test_input_lines[9]))
tc.assertEqual(lib.ListingFile(4060174, "j"), lib.parse_line(test_input_lines[19]))

cli = lib.CLI()
for line in test_input_lines[1:]:
    cli.read_cmd(lib.parse_line(line))

tc.assertEqual(["e", "a", "d", ""], [d.dirname for d in cli.root_dir.traverse()])
tc.assertEqual({"a", "e"}, set(d.dirname for d in cli.root_dir.traverse() if d.calculate_size() <= 100000))
tc.assertEqual(95437, lib.part1(cli.root_dir))
tc.assertEqual(24933642, lib.part2(cli.root_dir))

