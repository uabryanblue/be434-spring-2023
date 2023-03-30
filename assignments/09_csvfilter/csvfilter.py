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
    print(f"headers: {headers}")
    # create a dictionary of header field name, value pairs
    records = [dict(zip(headers, line.rstrip().split(','))) for line in infh]
    # print(f"records: {records}")
    
    # if we could not read any data, exit
    if not records:
        sys.exit(f'No usable data in --file "{args.file.name}"')

    if args.col and (args.col not in headers):
        sys.exit(f'Column name in -col "{args.col}" not found in header record.')
    
    # open the supplied filename, or default out.csv for writing
    ofh = open(args.outfile, 'wt', encoding='UTF-8')
    # always place a header record in the output file
    ofh.write(f"{','.join(headers)}\n")
    
    # for rec in records:
        
    count = 0
    # a column to search was specified, only search within it
    if args.col:
        print(f"column to search is: {args.col:}")
        for rec in records:
            colVal = rec.get(args.col)
            print(f"{colVal.upper()} : {args.val.upper()}")
            if colVal.upper() == args.val.upper():
                count += 1
                ofh.write(f'{",".join(rec)}\n') 
                
    print(f'Done, wrote {count} to "{ofh.name}".')         
    
#         if name and reps:
#             match = re.match(r'(\d+)-(\d+)', reps)
#             if match:
#                 low, high = map(int, match.groups())
#                 exercises.append((name, low, high))
  
    
 
    infh.close()
    ofh.close()
# --------------------------------------------------
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
