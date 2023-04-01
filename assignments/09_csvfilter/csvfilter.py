#!/usr/bin/env python
"""
Author : lazuline <lazuline@localhost>
Date   : 2023-03-30
Purpose: Rock the Casbah
"""

import argparse
import numpy as np
import pandas as pd
# import csv
# import re
# import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        required=True,
                        # type=str)
                        type=argparse.FileType('rt'))

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        required=True,
                        type=str,
                        default=None)
    
    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='col',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='OUTFILE',
                        type=str,
                        default='out.csv')
    
    parser.add_argument('-d',
                        '--delimiter',
                        help='Input delimiter',
                        metavar='delim',
                        type=str,
                        default=',')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    
    args = get_args()
    print(f'using delimeter:{args.delimiter}')
    
    df = pd.read_csv(args.file.name, sep=args.delimiter, dtype = str) 
    
    # print(df.head())
    print(f'Looking for:{args.val}')
    if args.col:
        outdf = df[df[args.col] == args.val]
    else:
        print(f'no col specified')
        
    outdf.to_csv(args.outfile, header=True, index=False, mode='wt')
    print(f'Done, wrote {outdf.shape[0]} to "{args.outfile}".')
    # print(df['adult_male'].str.contains(args.val, na=False, case=False))

# --------------------------------------------------
if __name__ == '__main__':
    main()
