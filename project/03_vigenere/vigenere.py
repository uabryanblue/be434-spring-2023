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
def test_shift():
#     """test the common cases of error"""

    assert map_char("T", 0, 'TEST') == 'M'
    assert map_char("H", 1, 'TEST') == 'L'
    assert map_char("E", 2, 'TEST') == 'W'
    assert map_char("Q", 3, 'TEST') == 'J'
    assert map_char("U", 4, 'TEST') == 'N'
    assert map_char("I", 5, 'TEST') == 'M'
    assert map_char("G", 35, 'TEST') == 'Z'
    
#     # Don't worry, spiders,
#     # FWC'A AFTZN, ZTZFMGZ, 
    assert map_char("D", 0, 'CIPHER') == 'F'
    assert map_char("S", 13, 'CIPHER') == 'Z'  # should be A ? 18 + 8 = 26, 
    assert map_char(",", 11, 'CIPHER') == ','


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
def map_char(inchar, index, keyword, CipherChar):
    """translate inchar with its index and keyword index
        using base 26"""

    # if the character is not in A-Z just return inchar
    if inchar not in string.ascii_uppercase:
        # print(f"FOUND NON ALPHA:{inchar}:{index}")
        return inchar, 0

    # the ordinal position of 'A' is 65 use this in calculations
    # calculate the input character position in A-Z, 0 based
    # InValue = ord(inchar) - 65
    InValue = get_alpha_number(inchar)
    # print(f"--inchar: {inchar}, Index: {index} InOrd: {InValue}")
    
    # KeyLen = len(keyword)
    # HashIndex = index % KeyLen
    # HashIndex = (index + 1) % KeyLen
    
    # KeyValue = get_alpha_number(keyword[HashIndex])
    KeyValue = get_alpha_number(CipherChar)
    # KeyValue = ord(keyword[HashIndex]) - 65
    # print(f"keyvalue: {KeyValue} HashCar:{keyword[HashIndex]}")

    # FinalOrd = (InValue + KeyValue) % 26 + 65
    FinalOrd = ((InValue + KeyValue) % 26) + 65
    # tmp = InValue + KeyValue
    # if tmp > 25: tmp = tmp - 26 # 0 based, 0 -> 25, but 26 values
    # print(f"Inchar: {inchar}, InVal: {InValue}, KeyLen: {KeyLen}, HashIndex: {HashIndex}:{keyword[HashIndex]}, KeyValue: {KeyValue}, tmp: {tmp}")

    # FinalOrd = tmp + 65
    # print(f"Inchar: {inchar}, InVal: {InValue:2}, KeyLen: {KeyLen:2}, HashIndex: {HashIndex:2}:{keyword[HashIndex]}, KeyValue: {KeyValue:2}, tmp: {tmp:2}, finalord {FinalOrd:2}:{chr(FinalOrd)}")
    # print(f"Inchar: {inchar}, AlphaVal: {InValue:2}, HashIndex:KeyChar: {HashIndex:2}:{keyword[HashIndex]}, AlphaHashVal: {KeyValue:2}, sum: {InValue + KeyValue}, SumCorrected: {tmp:2}, MappedChar {FinalOrd:2}:{chr(FinalOrd)}")
    # print(f"Inchar: {inchar}, AlphaVal: {InValue:2}, KeyChar: {CipherChar:2}, AlphaHashVal: {KeyValue:2}, sum: {InValue + KeyValue}, MappedChar {FinalOrd:2}:{chr(FinalOrd)}")

    # FinalOrd = ((InValue + KeyValue) - 26) + 65
    # print(f"InValue: {InValue}; KeyValue: {KeyValue}")
    # print(f"FinalOrd: {FinalOrd} finalchar: {chr(FinalOrd)}")

    return chr(FinalOrd), 1


# --------------------------------------------------
def main():
    """Vigenere Ciphers"""

    args = get_args()

    # alpha_test()
    # exit()

    for line in args.infile:
        lmap = ''
        # line = ''.join(line.split()) #### debug
        line = line.upper()
        CPos = 0
        for word in re.split(r'(\W+)', line):
            for i,c in enumerate(word):
                CipherChar = args.keyword[CPos % len(args.keyword)]
                # print(f"i {i}, c {c}, CipherChar {CipherChar}, CPos {CPos}")
                # CPos =+ 1
                mapped, Inc = map_char(c.upper(), i, args.keyword, CipherChar)
                CPos += Inc
                # print("mapped")
                # print(c, i, mapped, ord(c), ord(mapped))
                # args.outfile.write(f"::{c.upper()}:{i}:{mapped}")
                lmap = lmap + mapped
                # args.outfile.write(mapped)
        args.outfile.write(lmap) # debug

# --------------------------------------------------
if __name__ == "__main__":
    main()
