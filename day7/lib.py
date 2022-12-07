from dataclasses import dataclass, field
from typing import Dict, Optional, Union, Iterator


@dataclass
class Dir:
    parent: Optional["Dir"]
    dirname: str
    subdirs: Dict[str, "Dir"] = field(default_factory=lambda: {})
    files: Dict[str, int] = field(default_factory=lambda: {})
    files_size: int = 0

    def add_file(self, filename: str, size: int):
        assert filename not in self.files
        self.files[filename] = size
        self.files_size += size
    
    def add_subdir(self, dirname: str) -> "Dir":
        assert dirname not in self.subdirs
        self.subdirs[dirname] = subdir = Dir(self, dirname)
        return subdir

    def calculate_size(self) -> int:
        return sum(d.calculate_size() for d in self.subdirs.values()) + self.files_size
    
    @property
    def is_root(self) -> bool:
        return self.parent is None
    
    @classmethod
    def create_root(cls) -> "Dir":
        return cls(None, "")
    
    def __str__(self) -> str:
        if self.is_root:
            return "/"
        return str(self.parent) + self.dirname + "/"

    def traverse(self) -> Iterator["Dir"]:
        for d in self.subdirs.values():
            yield from d.traverse()
        yield self


@dataclass
class CommandLs:
    pass

@dataclass
class CommandCd:
    path: str

@dataclass
class ListingDir:
    name: str

@dataclass
class ListingFile:
    size: int
    name: str


cmd_t = Union[ListingDir, ListingFile, CommandCd, CommandLs]


@dataclass
class CLI:
    root_dir: Dir = field(default_factory=lambda: Dir.create_root())
    cwd_: Dir = None

    def __post_init__(self):
        self.cwd_ = self.root_dir

    def cd(self, path: str):
        if path == "..":
            assert self.cwd_ is not self.root_dir, "Already at root"
            self.cwd_ = self.cwd_.parent
        else:
            self.cwd_ = self.cwd_.subdirs[path]

    def read_cmd(self, cmd: cmd_t):
        if isinstance(cmd, ListingDir):
            self.cwd_.add_subdir(cmd.name)
        elif isinstance(cmd, ListingFile):
            self.cwd_.add_file(cmd.name, cmd.size)
        elif isinstance(cmd, CommandCd):
            self.cd(cmd.path)
        elif isinstance(cmd, CommandLs):
            return  # Don't care about state here since we only have ls that prints anything
    
    def __str__(self) -> str:
        return str(self.cwd_)
    
    def traverse_dirs(self) -> Iterator[Dir]:
        return self.cwd_.traverse()


def parse_line(line: str) -> cmd_t:
    if line.startswith("$ cd"):
        dirname = line[5:].strip()
        return CommandCd(dirname)
    elif line.startswith("$ ls"):
        return CommandLs()
    elif line.startswith("dir "):
        dirname = line[4:].strip()
        return ListingDir(dirname)
    else:
        filesize, filename = line.split(" ")
        return ListingFile(int(filesize), filename)

    
def part1(root_dir: Dir):
    return sum(d.calculate_size() for d in root_dir.traverse() if d.calculate_size() <= 100000)


def part2(root_dir: Dir):
    total_used_space = root_dir.calculate_size()
    total_disk_space = 70000000
    needed_space = 30000000
    available_space = total_disk_space - total_used_space
    minimum_space_to_free = needed_space - available_space
    return min(d.calculate_size() for d in root_dir.traverse() if d.calculate_size() >= minimum_space_to_free)
