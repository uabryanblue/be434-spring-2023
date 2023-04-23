#!/usr/bin/env python
"""
Author : Bryan Blue bryanblue@arizona.edu
Date   : 2023-04-23
Purpose: Substitution Cipher
"""

import argparse
import random
import string
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Substitution Cipher",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "infile",
        help="Input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default=None,
    )

    parser.add_argument(
        "-s", "--seed",
        help="A random seed",
        metavar="SEED",
        type=int,
        default=3
    )

    parser.add_argument(
        "-d", "--decode",
        help="A boolean flag",
        action="store_true",
        default=False
    )

    parser.add_argument(
        "-o", "--outfile",
        help="Output file",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )

    return parser.parse_args()


# --------------------------------------------------
def build_dictionary():
    """create a dictionary mapping A-Z to a random list of A-Z vlaues"""

    substitution = {}
    alpha = []

    alpha = list(string.ascii_uppercase)
    substitution = dict(zip(list(alpha), random.sample(alpha, 26)))

    return substitution


# --------------------------------------------------
def sub_cypher(inchar, SubDict, decode):
    """convert character to substituted value
    if decode is True return the decoded value"""

    # if the character is not in A-Z just return inchar
    if inchar not in string.ascii_uppercase:
        return inchar

    if decode:
        newchar = "".join([key for key, value in SubDict.items()
                           if value == inchar])
    else:
        mychar = SubDict.get(inchar)
        newchar = inchar if mychar is None else mychar

    return newchar


# --------------------------------------------------
def main():
    """Substitution Cipher"""

    args = get_args()
    # make code reproducable
    random.seed(args.seed)
    substitution = build_dictionary()

    # encode or decode every character for every line in input file
    for line in args.infile:
        args.outfile.write(
            "".join([sub_cypher(c.upper(), substitution, args.decode)
                    for c in line])
        )


# --------------------------------------------------
if __name__ == "__main__":
    main()
