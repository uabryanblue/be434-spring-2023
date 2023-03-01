#!/usr/bin/env python
"""
Author : Homework 06 <bryanblue@arizona.edu>
Date   : 2023-02-28
Purpose: Homework 06
"""

import argparse
import re
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('SEQ',
                        metavar='SEQ',
                        nargs="+",
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--output',
                        help='Output filename',
                        metavar='FILE',
                        default=sys.stdout,
                        type=argparse.FileType("wt"),
                        )


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    SEQ = args.SEQ
    FILE = args.output

    # create dictionary of IUPAC -> Base code translations
    codes ={} 
    codes['A'] = 'A'
    codes['C'] = 'C'
    codes['G'] = 'G'
    codes['T'] = 'T'
    codes['U'] = 'U'
    codes['R'] = '[AG]'
    codes['Y'] = '[CT]'
    codes['S'] = '[GC]'
    codes['W'] = '[AT]'
    codes['K'] = '[GT]'
    codes['M'] = '[AC]'
    codes['B'] = '[CGT]'
    codes['D'] = '[AGT]'
    codes['H'] = '[ACT]'
    codes['V'] = '[ACG]'
    codes['N'] = '[ACGT]' 

    # print(f'str_arg = "{SEQ}"')
    # print('file_arg = "{}"'.format(FILE if FILE else ''))
   
    for dna in SEQ:
        text = dna + ' '
        for dna_char in dna:
            text += codes.get(dna_char,dna_char) #, out_txt, c)        
        FILE.write(text)       
        FILE.write('\n')


# --------------------------------------------------
if __name__ == '__main__':
    main()
