#!/usr/bin/env python
"""
Author : Homework 06 <bryanblue@arizona.edu>
Date   : 2023-02-28
Purpose: Homework 06
"""

import argparse
import re
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('SEQ',
                        metavar='SEQ',
                        nargs="+",
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--output',
                        help='Output filename',
                        metavar='FILE',
                        default=sys.stdout,
                        type=argparse.FileType("wt"),
                        )


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    SEQ = args.SEQ
    FILE = args.output

    # print(f'str_arg = "{SEQ}"')
    # print('file_arg = "{}"'.format(FILE if FILE else ''))

    # Basic list comp for a single regex, expand to dictionary
    #[print('OK') if re.search('^A[CT]G$', 'ATG') else print('NO')]
    code = '[M]' # for AC
    out_txt = '[AC]'

    for c in SEQ:
        print(f'search:{code} replace:{out_txt} in:{c}' )
        text = re.sub(code, out_txt, c)

    #text = re.sub(code, vowel, text)
    print(f'{text}')

    #print(''.join(text))

# --------------------------------------------------
if __name__ == '__main__':
    main()
