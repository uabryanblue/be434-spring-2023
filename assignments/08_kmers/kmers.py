#!/usr/bin/env python
"""
Author : Bryan BLue
Date   : 2023-03-23
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

    return args



# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    print(f'{type(args.kmer)}')

# --------------------------------------------------
if __name__ == '__main__':
    main()

def find_kmers(seq, k):
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else\
        [seq[i:i + k] for i in range(n)]
        
        
def test_find_kmers():
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []
    
