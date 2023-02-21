#!/usr/bin/env python
"""
Author : Bryan Blue, <bryanblue@arizona.edu,>
Date   : 2023-02-21
Purpose: exercise 5 - translate.py
"""

import argparse
import sys
from pprint import pprint

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-c',
                        '--codons',
                        required=True,
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'))
                        #default=sys.stdin)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        default='out.txt',
                        type=argparse.FileType('wt'))

    parser.add_argument("sequence",
                        metavar="str",
                        help="DNA/RNA sequence")


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    

    args = get_args()
    print('seq =', args.sequence)
    print('codons =', args.codons)
    print('outfile =', args.outfile)

    # read in codons table and create a dictionary
    codon_table = {}
    for line in args.codons:
        codon_table[line.rstrip().split()[0]] = line.rstrip().split()[1]
        #print(line.rstrip().split())
        

    pprint(codon_table) # pretty print
# --------------------------------------------------
if __name__ == '__main__':
    main()
