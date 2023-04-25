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
def map_char(inchar, CipherChar, Decode):
    """translate inchar with its cipher character
    using base 26"""

    # if the character is not in A-Z just return inchar
    # return a 0 => do not increment to next cipher character
    if inchar not in string.ascii_uppercase:
        return inchar, 0

    # calculate the input character position in A-Z, 0 based
    InValue = ord(inchar) - 65
    CipherValue = ord(CipherChar) - 65

    # the ordinal position of 'A' is 65 and used for clarity
    if Decode:
        FinalChar = chr(((InValue - CipherValue) % 26) + 65)
    else:
        FinalChar = chr(((InValue + CipherValue) % 26) + 65)

    # return a 1 => increment to next cipher character
    return FinalChar, 1


# --------------------------------------------------
def main():
    """Vigenere Ciphers
    Traverse every line, word, and character of a file
    Ignore any non A-Z when encode/decode using cipher"""

    args = get_args()

    # read a line from the file
    for line in args.infile:
        line = line.upper()  # not all input is in uppercase
        LineCipher = ""
        CPos = 0
        # split into words that also include non-alpha chars
        for word in re.split(r"(\W+)", line):
            # enumerate throug the word
            for c in word:
                # pick the correct keyword character
                CipherChar = args.keyword[CPos % len(args.keyword)]
                mapped, Inc = map_char(c.upper(), CipherChar, args.decode)
                CPos += Inc
                LineCipher = LineCipher + mapped
        args.outfile.write(LineCipher)


# --------------------------------------------------
if __name__ == "__main__":
    main()
