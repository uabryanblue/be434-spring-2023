#!/usr/bin/env python
"""
Author : lazuline <lazuline@localhost>
Date   : 2023-04-19
Purpose: Rock the Casbah
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        help='Search pattern')
    
    parser.add_argument('-i',
                        '--insensitive',
                        help='insensitive search',
                        action='store_true',
                        default=False)
    
    parser.add_argument('FILE',
                        metavar='FILE',
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    print("hi")

# --------------------------------------------------
if __name__ == '__main__':
    main()
