#!/usr/bin/env python
"""
Author : Homework 06 <bryanblue@arizona.edu>
Date   : 2023-02-28
Purpose: Homework 06
"""

import argparse
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
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=str)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    SEQ = args.SEQ
    fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    filename = fh.name
    # print(f'FILE: {fh.name}')

    # create dictionary of IUPAC -> Base code translations
    codes = {}
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

# use for loops as a solution
    # # may have more than one DNA sequence passed in
    # for dna in SEQ:
    #     text = dna + ' '
    #     # look at each character in the DNA string
    #     # for possible replacement using the codes dictionary
    #      # default to itself if no lookup found
    #     for dna_char in dna:
    #         text += codes.get(dna_char, dna_char)
    #     fh.write(text)
    #     fh.write('\n')

# use list comprehension for inner loop as a solution
    # may have more than one DNA sequence passed in
    for dna in SEQ:
        text = [dna]
        text.append(' ')
        # look at each character in the DNA string
        # for possible replacement using the codes dictionary
        # default to itself if no lookup found
        text += [codes.get(dna_char, dna_char) for dna_char in dna]
        fh.write(''.join(text))
        fh.write('\n')


    # output a filename message if the output is not stdout
    if filename != '<stdout>':
        print(f'Done, see output in "{filename}"')

    fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
