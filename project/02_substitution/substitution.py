#!/usr/bin/env python
"""
Author : Bryan Blue bryanblue@arizona.edu
Date   : 2023-04-23
Purpose: Substitution Cipher
"""

import argparse
import random
import re
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
        "-s", "--seed", help="A random seed", metavar="SEED", type=int, default=3
    )

    parser.add_argument(
        "-d", "--decode", help="A boolean flag", action="store_true", default=False
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
def build_dictionary():
    """create a mapping from A-Z to a random list of A-Z vlaues"""

    substitution={}
    alpha=[]
    
    alpha = list(string.ascii_uppercase)
    substitution = dict(zip(list(alpha),random.sample(alpha, 26)))
    # print(substitution)
    return substitution
    
    
# --------------------------------------------------
def sub_cypher(inchar, SubDict, decode):
    """convert in character to substituted value"""

    # if the character is not in A-Z, a-z, just return inchar
    pattern = re.compile("[A-Za-z]")
    if pattern.search(inchar) is None:
        return inchar
    
    if decode:
        newchar = ''.join([key for key, value in SubDict.items() if value == inchar])
    else:
        newchar = inchar if SubDict.get(inchar) is None else SubDict.get(inchar)
        # if newchar is None:
        #     newchar = inchar
    return newchar
    
# --------------------------------------------------
def main():
    """Substitution Cipher"""

    args = get_args()
    # make code reproducable
    random.seed(args.seed)
    substitution = build_dictionary()

    for line in args.infile:
        # if args.decode:
        #     # print("decode!")
        args.outfile.write(''.join([sub_cypher(c.upper(), substitution, args.decode) for c in line]))
            # print([key for key, value in substitution.items() if value == c.upper()])
        # else:
        #     # _ = [args.outfile.write(sub_cypher(c.upper(), substitution)) for c in line]
        #     args.outfile.write(''.join([sub_cypher(c.upper(), substitution, args.decode) for c in line]))


# --------------------------------------------------
if __name__ == "__main__":
    main()
