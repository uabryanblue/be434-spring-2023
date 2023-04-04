#!/usr/bin/env python
"""
Author : Bryan Blue (bryanblue@arizona.edu)
Date   : 2023-04-04
Purpose: Find Common Words
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1',
                        help='Input file 1')
    
    parser.add_argument('file2',
                    metavar='FILE2',
                    help='Input file 2')

    parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='str',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    ofh = args.outfile
    
    try:
        fh1 = open(args.file1, 'rt')
    except:
        sys.exit(f"No such file or directory: '{args.file1}'")

    try:
        fh2 = open(args.file2, 'rt')
    except:
        sys.exit(f"No such file or directory: '{args.file2}'")

# --------------------------------------------------
    def read_words_into_set(fh):
        """read all white space delimited text into a set from a file"""
        MySet = set()
        for line in fh:
            for word in line.split():
                MySet.add(word)
        return MySet
# --------------------------------------------------

    set1 = set()
    set2 = set()
    
    set1 = read_words_into_set(fh1)
    set2 = read_words_into_set(fh2)
            
    # print(f'set1: {set1}')
    # print(f'set2: {set2}')

    output = '\n'.join(sorted(set1.intersection(set2)))
    ofh.write(output)
    ofh.write('\n') # put a trailing return in for clarity

    fh1.close()
    fh2.close()
    ofh.close()


        
# --------------------------------------------------
if __name__ == '__main__':
    main()
