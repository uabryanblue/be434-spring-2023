#!/usr/bin/env python
"""
Author : Bryan Blue (bryanblue@arizona.edu)
Date   : 2023-04-04
Purpose: Find Common Words
"""

import argparse
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Rock the Casbah",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("file1", metavar="FILE1", help="Input file 1")

    parser.add_argument("file2", metavar="FILE2", help="Input file 2")

    parser.add_argument(
        "-i",
        "--int",
        help="A named integer argument",
        metavar="int",
        type=int,
        default=0,
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output file",
        metavar="str",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """
    use sets to output commone words between two input files

    """

    args = get_args()
    ofh = args.outfile

    # try to open both required input files, if it fails,
    # output error message and exit
    try:
        fh1 = open(args.file1, "rt", encoding="utf-8")
    except IOError:
        ofh.close()
        sys.exit(f"No such file or directory: '{args.file1}'")

    try:
        fh2 = open(args.file2, "rt", encoding="utf-8")
    except IOError:
        ofh.close()
        sys.exit(f"No such file or directory: '{args.file2}'")

    # --------------------------------------------------
    def read_words_into_set(fh):
        """read all white space delimited text
        into a set from a file"""

        # only look at alpha characters, no punctuation
        pattern = re.compile("([a-z]|[A-Z][0-9])+", re.IGNORECASE)
        # print(f'pattern:{pattern}:')

        MySet = set()
        for line in fh:
            for word in line.split():
                neword = re.search(pattern, word).group(0)
                # print(f'new:{neword}')
                MySet.add(neword)
        return MySet

    # --------------------------------------------------
    # initializations
    set1 = set()
    set2 = set()

    set1 = read_words_into_set(fh1)
    set2 = read_words_into_set(fh2)

    # print(f'set1: {set1}')
    # print(f'set2: {set2}')

    # output needs to be a sorted, new line delimited
    # intersection of the two sets
    # out = sorted(set1.intersection(set2))
    [ofh.write(f"{item}\n") for item in sorted(set1.intersection(set2))]

    # close out all open file handles
    fh1.close()
    fh2.close()
    ofh.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
