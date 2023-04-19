#!/usr/bin/env python
"""
Author : Bryan Blue bryanblue@arizona.edu
Date   : 2023-04-19
Purpose: Pythong grepm
"""

import argparse
import os
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Python grep",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("pattern", metavar="PATTERN", help="Search pattern")

    parser.add_argument(
        "-i",
        "--insensitive",
        help="insensitive search",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "files", metavar="FILE", type=str, nargs="+", help="Input file(s)"
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output file",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )

    return parser.parse_args()


# --------------------------------------------------
def create_pattern(pattern, ignore_case):
    """create a regular expression using the re module
    which also handles case insensitivity"""

    re_pattern = re.compile(pattern)
    if ignore_case:
        re_pattern = re.compile(pattern, re.IGNORECASE)
    return re_pattern


# --------------------------------------------------
def main():
    """Python grep"""

    args = get_args()
    # print(args)

    # verify all passed in input files exist
    for name in args.files:
        if not os.path.isfile(name):
            sys.exit(f"error: No such file or directory: '{name}'")

    # create a clean regex pattern
    re_pattern = create_pattern(args.pattern, args.insensitive)
    # find all lines that match the pattern in all filenames
    NumFiles = len(args.files)
    for name in args.files:
        with open(name, "rt", encoding="utf8") as fh:
            for line in fh:
                # if found, do not care about where, dump line
                if re.search(re_pattern, line):
                    out = f"{name}: {line}" if NumFiles > 1 else line
                    args.outfile.write(out)


# --------------------------------------------------
if __name__ == "__main__":
    main()
