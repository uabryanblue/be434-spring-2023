#!/usr/bin/env python
"""
Author : Bryan Blue bryanblue@arizona.edu
Date   : 2023-04-19
Purpose: Caesar Shift
test using: pytest -xv caesar.py
"""

import argparse
import os
import sys
import re
# --------------------------------------------------
def get_args():
    """Caesar Shift"""

    parser = argparse.ArgumentParser(
        description='Caesar Shift',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('infile',
                    help='Input file',
                    metavar='FILE',
                    type=argparse.FileType('rt'),
                    default=sys.stdin)


    parser.add_argument('-n',
                        '--number',
                        help='A number to shift',
                        metavar='NUMBER',
                        type=int,
                        default=3)

    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action='store_true',
                        default=False)
    
    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)


    return parser.parse_args()

# --------------------------------------------------
def test_shift():
    assert shift_forward('A',3) == 'D'
    assert shift_forward('H',3) == 'K'
    assert shift_forward('K',-3) =='H'
    assert shift_forward('Z',1) == 'A'
    assert shift_forward('Z',3) == 'C'
    
# --------------------------------------------------
def shift_forward(inchar, steps):
    """use a numerical approach using the modulus
       operator to shift using ordinal (ascii) values """
    
    # if the character is not in A-Z, a-z, just return inchar
    pattern = re.compile("[A-Za-z]")
    if pattern.search(inchar) is None:
        return inchar
    
    # print(f" going to process with {inchar}")
    # start at position or upper or lower set based on input   
    if inchar.isupper():
        start = ord('A')
    else:
        start = ord('a')
    
    # take the ordinal value of the character and convert it 
    # to the shifted value in the correct upper/lower range 
    inc = (((ord(inchar)-start)+steps) % 26) + start
    newchar = chr(inc)
    # print(f"ord {inchar}={ord(inchar)}, start={start}, steps={steps}, inc={inc}, new={newchar}")   
    return newchar
    
# --------------------------------------------------
def main():
    """caesar shift basic encryption"""

    args = get_args()
    
    # if decoding, just use negative of the shift value
    ShiftVal = (-1*args.number) if args.decode else args.number
    # this will work for upper and lower case letters
    # the .upper() is added to pass the tests
    for line in args.infile:
        [args.outfile.write(shift_forward(c, ShiftVal).upper()) for c in line]

# --------------------------------------------------
if __name__ == '__main__':
    main()
