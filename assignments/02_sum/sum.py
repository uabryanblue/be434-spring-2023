#!/usr/bin/env python3
"""
Author : Bryan Blue bryanblue@arizona.edu
Date   : 2023-01-31
Purpose: Assignment 2 BE534, Spring 2023
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
        "-i", "--int", help="Numbers to add", metavar="INT", type=int, default=0
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Add numbers together"""

    args = get_args()
    int_arg = args.int

    print(f'int_arg = "{int_arg}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
