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
        description="find the common k-mers between two files",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-k", "--kmer", help="K-mer size", metavar="int", type=int, default=3
    )

    parser.add_argument(
        "FILE1",
        help="Input file 1",
        metavar="FILE1",
        type=argparse.FileType("rt"),
    )

    parser.add_argument(
        "FILE2",
        help="Input file 2",
        metavar="FILE2",
        type=argparse.FileType("rt"),
    )

    args = parser.parse_args()

    # only kmer > 0 and of type integer are allowed
    if not args.kmer > 0:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """
    find the common k-mers between two files
    using user specified lengths that must be
    greater than 0
    """
    args = get_args()
    fd1 = args.FILE1
    fd2 = args.FILE2

    def find_kmers(seq, k):
        """Find all k-mers in string"""

        n = len(seq) - k + 1
        return [] if n < 1 else [seq[i: i + k] for i in range(n)]

    def test_find_kmers():
        """Unit tests for find_kmers"""

        assert find_kmers("", 1) == []
        assert find_kmers("ACTG", 1) == ["A", "C", "T", "G"]
        assert find_kmers("ACTG", 2) == ["AC", "CT", "TG"]
        assert find_kmers("ACTG", 3) == ["ACT", "CTG"]
        assert find_kmers("ACTG", 4) == ["ACTG"]
        assert find_kmers("ACTG", 5) == []

    def parse_kmers(df, k):
        words1 = {}
        for line in df:
            for word in line.split():
                for kmer in find_kmers(word, k):
                    if words1.get(kmer):
                        words1[kmer] += 1
                    else:
                        words1[kmer] = 1
                    # print(f'found: {kmer}')
                    # increment the count of this "kmer" in "words1"
        return words1

    def match_kmers(f1_kmers, f2_kmers):
        """
        find matching keys
        """

        for key in set(f1_kmers) & set(f2_kmers):
            # print(f'{key} : value is present in both f1_kmers and f2_kmers')
            print(f"{key:10} {f1_kmers[key]:5} {f2_kmers[key]:5}")

    test_find_kmers()
    f1_kmers = parse_kmers(fd1, args.kmer)
    # print(f'kmer1: {f1_kmers}')
    f2_kmers = parse_kmers(fd2, args.kmer)
    # print(f'kmer1: {f2_kmers}')
    match_kmers(f1_kmers, f2_kmers)


# --------------------------------------------------
if __name__ == "__main__":
    main()
