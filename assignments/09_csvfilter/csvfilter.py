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
import sys

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
    # print(f'using delimeter:{args.delimiter}')
    
    # read the input file in a data frame, make sure all fields are strings
    df = pd.read_csv(args.file.name, sep=args.delimiter, dtype = str, engine='python')
     
    # if the col argument is specified, check that it is in the file column headers     
    if(args.col and (args.col not in df.columns)):
        args.file.close()
        print(f'--col "{args.col}" not a valid column!')
        mylist = ', '.join(df.columns.tolist())
        sys.exit(f'Choose from {mylist}')
    
    # print(df.head())
    # print(f'Looking for:{args.val}')
    # print(f'looking in column:{args.col}')
    if args.col:
        # find all rows that match the input value in a given column, case insensitive
        outdf = df[df[args.col].str.lower() == args.val.lower()]
    else:
        # find all all rows that match any column for a given value, case insensitive
        # print(f'no col specified')
        outdf = df[df.apply(lambda row: row.str.contains(args.val, case=False).any(), axis=1)] 

    # no records found, report it
    if outdf.shape[0] == 0:
        args.file.close()
        sys.exit(f'No usable data in --file "{args.file.name}"')    
    else:
        # write out same structure with the lines that matched
        outdf.to_csv(args.outfile, header=True, index=False, mode='wt')
        print(f'Done, wrote {outdf.shape[0]} to "{args.outfile}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
