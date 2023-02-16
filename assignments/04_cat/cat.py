#!/usr/bin/env python
"""
Author : Bryan Blue <bryanblue@arizona.edu>
Date   : 2023-02-16
Purpose: Python cat
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Python cat",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # parse file names and attempt to open them read, text
    # if not, fail with an error
    parser.add_argument(
        "file",
        help="Input file(s)",
        metavar="file",
        nargs="*",
        type=argparse.FileType("rt"),
        default=[],
    )

    # option to allow each files lines to have a line number
    parser.add_argument("-n", "--number",
                        help="Number the lines",
                        action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Python cat"""

    args = get_args()
    infd = args.file
    number = args.number

    # print(f'str_arg = "{infd}"')
    # print(f'flag_arg = "{number}"')

    # infd is a list of open file handles, loop through them all
    for fh in infd:
        line_number = 0
        # loop though each line a file
        # optionally prepending a line number
        for line in fh:
            if number:
                line_number += 1
                print(f"{line_number:6}\t{line.strip()}")
            else:
                print(f"{line.strip()}")


# --------------------------------------------------
if __name__ == "__main__":
    main()
