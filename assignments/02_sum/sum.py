#!/usr/bin/env python3
"""
Author : Bryan Blue bryanblue@arizona.edu
Date   : 2023-01-31
Purpose: Sum integer values
University of Arizona, BE534
"""

import argparse


# --------------------------------------------------
def get_args():
    """Add numbers"""

    parser = argparse.ArgumentParser(
        description="Add numbers",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "INT", nargs="+", help="Numbers to add", type=int, metavar="INT"
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Add numbers together"""

    args = get_args()
    # add_argument statement takes care of type checking
    # list of integer values to be added together
    int_args = args.INT

    # pg 400 from Tiny Python Projects
    # advanced for this chapter, but the videos encourges
    # you to review the documentation in the book (old formatting)
    # print("{} = {}".format(" + ".join(map(str, int_args)), sum(int_args)))
    # this is converted to the f string format
    print(f'{" + ".join(map(str, int_args))} = {sum(int_args)}')


# --------------------------------------------------
if __name__ == "__main__":
    main()
