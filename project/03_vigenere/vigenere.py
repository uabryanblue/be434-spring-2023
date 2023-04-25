#!/usr/bin/env python
"""
Author : Bryan Blue bryanblue@arizona.edu
Date   : 2023-04-23
Purpose: Vigenere Ciphers
"""

import argparse
import re
import string
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Vigenere Ciphers",
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
        "-k",
        "--keyword",
        help="A keyword",
        metavar="KEYWORD",
        type=str,
        default="CIPHER",
    )

    parser.add_argument(
        "-d", "--decode",
        help="A boolean flag",
        action="store_true",
        default=False
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
# def test_shift():
# #     """test the common cases of error"""

# !!!!!!  don't know how to check 2 return values, these are invalid
#     assert map_char("T", 0, 'TEST') == 'M'
#     assert map_char("H", 1, 'TEST') == 'L'
#     assert map_char("E", 2, 'TEST') == 'W'
#     assert map_char("Q", 3, 'TEST') == 'J'
#     assert map_char("U", 4, 'TEST') == 'N'
#     assert map_char("I", 5, 'TEST') == 'M'
#     assert map_char("G", 35, 'TEST') == 'Z'

# #     # Don't worry, spiders,
# #     # FWC'A AFTZN, ZTZFMGZ,
#     assert map_char("D", 0, 'CIPHER') == 'F'
#     assert map_char("S", 13, 'CIPHER') == 'Z'  # should be A ? 18 + 8 = 26,
#     assert map_char(",", 11, 'CIPHER') == ','


# --------------------------------------------------
def get_alpha_number(inchar):
    out = ord(inchar) - 65
    return out


# --------------------------------------------------
def map_char(inchar, CipherChar, Decode):
    """translate inchar with its index and keyword index
    using base 26"""

    # if the character is not in A-Z just return inchar
    if inchar not in string.ascii_uppercase:
        # return a 0 => do not increment to next cipher character
        return inchar, 0

    # calculate the input character position in A-Z, 0 based
    InValue = get_alpha_number(inchar)
    KeyValue = get_alpha_number(CipherChar)

    # the ordinal position of 'A' is 65 use this in calculations
    if Decode:
        FinalOrd = ((InValue - KeyValue) % 26) + 65
    else:
        FinalOrd = ((InValue + KeyValue) % 26) + 65
    # return a 1 => increment to next cipher character
    return chr(FinalOrd), 1


# --------------------------------------------------
def main():
    """Vigenere Ciphers"""

    args = get_args()

    # read a line from the file
    for line in args.infile:
        lmap = ""
        line = line.upper()
        CPos = 0
        # then split into words that also include non-alpha chars
        for word in re.split(r"(\W+)", line):
            # then enumerate throug the word
            for i, c in enumerate(word):
                # pick the correct keyword character, ignoring non-alpha
                CipherChar = args.keyword[CPos % len(args.keyword)]
                # print(CipherChar)
                mapped, Inc = map_char(c.upper(), CipherChar, args.decode)
                CPos += Inc
                lmap = lmap + mapped
        args.outfile.write(lmap)


# --------------------------------------------------
if __name__ == "__main__":
    main()
