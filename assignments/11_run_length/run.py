#!/usr/bin/env python
"""
Author : Bryan Blue bryanblue@arizona.edu
Date   : 2023-04-12
Purpose: run length encoding
"""

import argparse
import os.path
import re


# --------------------------------------------------
def get_args():
    """Run-length encoding/data compression"""

    parser = argparse.ArgumentParser(
        description="Run-length encoding/data compression",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="str", help="DNA text or file")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text, "rt", encoding="UTF-8") as fh:
            args.text = fh.read().strip()

    return args


# --------------------------------------------------
def main():
    """run-length encoding RLE"""

    args = get_args()

    for seq in args.text.splitlines():
        print(rle(seq))

# --------------------------------------------------
def compact(rematch):
    """take the found match and compact it down to
        the first character and the length of the match"""
    if rematch.group() is not None:
        outstr = rematch.group()[0] + str(len(rematch.group()))
    return outstr


# --------------------------------------------------
def rle(seq):
    """Create RLE
    find all 2 or more occurences of any base
    in seq and replace it with the base and number
    of occurences in the group
    """

    base = ["A", "C", "G", "T"]
    for val in base:
        # you don't need the "+" here
        #pattern = r"[" + val + "]{2,}+"
        pattern = r"[" + val + "]{2,}"
        seq = re.sub(pattern, compact, seq)
    return seq

# --------------------------------------------------
def test_rle():
    """Test rle"""

    assert rle("A") == "A"
    assert rle("ACGT") == "ACGT"
    assert rle("AA") == "A2"
    assert rle("AAAAA") == "A5"
    assert rle("ACCGGGTTTT") == "AC2G3T4"


# --------------------------------------------------
if __name__ == "__main__":
    main()
