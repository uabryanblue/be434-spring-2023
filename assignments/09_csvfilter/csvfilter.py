#!/usr/bin/env python
"""
Author : lazuline <lazuline@localhost>
Date   : 2023-03-30
Purpose: Rock the Casbah
"""

import argparse
import csv
import re
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
    infh = args.file
    
    # read the file into a dictionary for all other processing
    # first line assumed to be a header record
    headers = infh.readline().rstrip().split(',')
    # print(f"headers: {headers}")
    # create a dictionary of header field name, value pairs
    records = [dict(zip(headers, line.rstrip().split(','))) for line in infh]
    # print(f"records: {records}")
    
    # if we could not read any data, exit
    if not records:
        sys.exit(f'No usable data in --file "{args.file.name}"')

    if args.col and (args.col not in headers):
        sys.exit(f'--col "{args.col}" not a valid column!')
    
    # open the supplied filename, or default out.csv for writing
    ofh = open(args.outfile, 'wt', encoding='UTF-8')
    # always place a header record in the output file
    ofh.write(f"{','.join(headers)}\n")
        
    # a column to search was specified, only search within it
    if args.col:
        foundCount = find_in_col(records, args.col, args.val, ofh)   
        
    print(f'Done, wrote {foundCount} to "{ofh.name}".')         
 
    infh.close()
    ofh.close()
# --------------------------------------------------

def find_in_col(records, column, value, ofh):
    count = 0
    # call upper() once, not in loop
    upper_val = value.upper()
    # print(f"column to search is: {column}")
    for rec in records:
        colVal = rec.get(column)
        # print(f"{colVal.upper()} : {upper_val}")
        if colVal.upper() == upper_val:
            count += 1
            ofh.write(f'{",".join(rec.values())}\n') 
    return count


# def read_csv(infh):
#     """Read the CSV input"""

#     exercises = []
#     for row in csv.DictReader(fh, delimiter=','):
#         name, reps = row.get('exercise'), row.get('reps')
#         if name and reps:
#             match = re.match(r'(\d+)-(\d+)', reps)
#             if match:
#                 low, high = map(int, match.groups())
#                 exercises.append((name, low, high))

#     return exercises
# --------------------------------------------------
if __name__ == '__main__':
    main()
