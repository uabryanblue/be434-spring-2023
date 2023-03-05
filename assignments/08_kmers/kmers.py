#!/usr/bin/env python
"""
Author : lazuline <lazuline@localhost>
Date   : 2023-03-05
Purpose: Finding Common K-mers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    parser.add_argument('positional',
                        help='Input file 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'))

    parser.add_argument('positional',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'))

    args = parser.parse_args()

    # only kmer > 0 and of type integer are allowed 
    if not args.kmer > 0:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return parser.parse_args()



# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    print(f'{type(args.kmer)}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
