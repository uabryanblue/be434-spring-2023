#!/usr/bin/env python
"""
Author : Bryan Blue bryanblue@arizona.edu
Date   : 2023-01-17
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Greetings and salutations",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-g",
        "--greeting",
        help="The greeting",
        metavar="str",
        type=str,
        default="Howdy",
    )

    parser.add_argument(
        "-n",
        "--name",
        help="Whom to greet",
        metavar="str",
        type=str,
        default="Stranger",
    )

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
