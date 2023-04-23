#!/usr/bin/env python
"""
Author : Bryan Blue bryanblue@arizona.edu
Date   : 2023-04-23
Purpose: Vigenere Ciphers
"""

import argparse
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
# def test_shift():
#     """test the common cases of error"""

#     assert map_char("T", 0, 'TEST') == 'M'
#     assert map_char("H", 1, 'TEST') == 'L'
#     assert map_char("E", 2, 'TEST') == 'W'
#     assert map_char("Q", 3, 'TEST') == 'J'
#     assert map_char("U", 4, 'TEST') == 'N'
#     assert map_char("I", 5, 'TEST') == 'M'
#     # assert map_char("S", 34, 'TEST') == 'G'  
#     # assert map_char("G", 35, 'TEST') == 'Z'
    
#     # Don't worry, spiders,
#     # FWC'A AFTZN, ZTZFMGZ,
#     assert map_char("D", 0, 'TEST') == 'F'
#     assert map_char("S", 13, 'TEST') == 'Z'  
#     assert map_char(",", 20, 'TEST') == ','


# --------------------------------------------------
def get_alpha_number(inchar):
    out = ord(inchar) - 65
    return out
    
def alpha_test():
    for i, c in enumerate(string.ascii_uppercase):
        alphpos = get_alpha_number(c)
        print(f"i:{i}; chr:{c}; alphabet pos; {alphpos}")
    return
# --------------------------------------------------
def map_char(inchar, index, keyword):
    """translate inchar with its index and keyword index
        using base 26"""

    # if the character is not in A-Z just return inchar
    if inchar not in string.ascii_uppercase:
        # print(f"FOUND NON ALPHA:{inchar}:")
        return inchar

    # the ordinal position of 'A' is 65 use this in calculations
    # calculate the input character position in A-Z, 0 based
    InValue = ord(inchar) - 65
    # print(f"--inchar: {inchar}, Index: {index} InOrd: {InValue}")
    
    KeyLen = len(keyword)
    HashIndex = index % KeyLen
    # HashIndex = (index + 1) % KeyLen
    # print(f"KeyLen: {KeyLen}, HashIndex: {HashIndex}")
    
    KeyValue = ord(keyword[HashIndex]) - 65
    # print(f"keyvalue: {KeyValue} HashCar:{keyword[HashIndex]}")

    FinalOrd = (InValue + KeyValue) % 26 + 65
    # print(f"FinalOrd: {FinalOrd} finalchar: {chr(FinalOrd)}")

    return chr(FinalOrd)


# --------------------------------------------------
def main():
    """Vigenere Ciphers"""

    args = get_args()

    alpha_test()
    exit()

    for line in args.infile:

        line = line.upper() # ''.join(line.upper().split())
        print(line, args.keyword)
        # print(str.upper(line))
        # assert map_char("D", 0, 'TEST') == 'F'
        # assert map_char("S", 13, 'TEST') == 'Z' 
        for i,c in enumerate(line):
            mapped = map_char(c.upper(), i, args.keyword)
            # print("mapped")
            # print(c, i, mapped, ord(c), ord(mapped))
            args.outfile.write(mapped)
            # print(c, i)
        args.outfile.write('\n')
        # print(line)
        # for c in line:
        # # args.outfile.write(''.join([shift_forward(c.upper(), Shift).upper()
        #                             for c in line]))


# --------------------------------------------------
if __name__ == "__main__":
    main()
