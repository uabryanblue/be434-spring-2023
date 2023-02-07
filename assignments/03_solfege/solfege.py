#!/usr/bin/env python
"""
Author : lazuline <lazuline@localhost>
Date   : 2023-02-05
Purpose: Assignment 03, BE534
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Rock the Casbah",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("str", metavar="str", nargs="+", help="Solfege")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Dictionary Assignment"""

    # parse command line
    args = get_args()
    str_arg = args.str

    # configure solfege dictionary
    syllables = dict(
        {
            "Do": "A deer, a female deer",
            "Re": "A drop of golden sun",
            "Mi": "A name I call myself",
            "Fa": "A long long way to run",
            "Sol": "A needle pulling thread",
            "La": "A note to follow sol",
            "Ti": "A drink with jam and bread",
        }
    )

    # print(f'syllables = "{syllables}"')
    # process each string passed to program
    for syll in str_arg:
        # if we have a match, output appropriate song phrase
        if syll in syllables:
            print(f"{syll}, {syllables[syll]}")
        # if not found, generate an error message
        else:
            print(f'I don\'t know "{syll}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
