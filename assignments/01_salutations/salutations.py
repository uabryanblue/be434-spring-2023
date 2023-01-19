#!/usr/bin/env python3

"""
Author : Bryan Blue bryanblue@arizona.edu
Date   : 2023-01-17
Purpose: Print greeting
University of Arizona, BE534
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Greetings and salutations",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # allow user to specify an alternate greeting
    parser.add_argument(
        "-g",
        "--greeting",
        help="The greeting",
        metavar="str",
        type=str,
        default="Howdy",
    )

    # allow user to specify an alternate name to greet
    parser.add_argument(
        "-n",
        "--name",
        help="Whom to greet",
        metavar="str",
        type=str,
        default="Stranger",
    )

    # control punctuation of a default of a period (.)
    # or override to produce an exclamation point (!)
    parser.add_argument(
        "-e", "--excited",
        help="Include an exclamation point",
        action="store_true"
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """01_salutations"""

    args = get_args()
    str_greeting = args.greeting
    str_name = args.name
    flag_excited = args.excited

    if flag_excited is False:
        print(f"{str_greeting}, {str_name}.")
    else:
        print(f"{str_greeting}, {str_name}!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
