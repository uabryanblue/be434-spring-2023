#!/usr/bin/env python
"""
Author : Bryan Blue, <bryanblue@arizona.edu,>
Date   : 2023-02-21
Purpose: exercise 5 - translate.py
"""

import argparse

# from pprint import pprint # only used in debugging dictionary


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Translate DNA/RNA to proteins",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-c",
        "--codons",
        required=True,
        help="A file with codon translations",
        metavar="FILE",
        type=argparse.FileType("rt"),
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename",
        metavar="FILE",
        default="out.txt",
        type=argparse.FileType("wt"),
    )

    parser.add_argument("sequence", metavar="str", help="DNA/RNA sequence")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """exercise 5 - translate.py"""

    args = get_args()
    # print('seq =', args.sequence)
    # print('codons =', args.codons)
    # print('outfile =', args.outfile)

    # read in codons table and create a dictionary
    codon_table = {}
    for line in args.codons:
        codon_table[line.rstrip().split()[0]] = line.rstrip().split()[1]
    # uncomment to output the codon dictionary
    # uncomment the pretty print include for this to work
    # pprint(codon_table) # pretty print

    # convert codons into amino acids
    k = 3
    seq = args.sequence
    for codon in [seq[i: i + k].upper() for i in range(0, len(seq), k)]:
        # print(f"{codon} {codon_table.get(codon)}") # debug output
        if codon_table.get(codon) is None:
            args.outfile.write("-")
        else:
            args.outfile.write(f"{codon_table.get(codon)}")
    args.outfile.write("\n")
    print(f'Output written to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == "__main__":
    main()
