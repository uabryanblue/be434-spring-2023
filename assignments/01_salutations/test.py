""" Tests for howdy.py """

import os
from subprocess import getstatusoutput

PRG = './salutations.py'


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_defaults():
    """ Prints expected default values """

    rv, out = getstatusoutput(f'{PRG}')
    assert rv == 0
    assert out.strip() == 'Howdy, Stranger.'


# --------------------------------------------------
def test_greeting():
    """ Accepts greeting """

    for opt in ['-g', '--greeting']:
        rv, out = getstatusoutput(f'{PRG} {opt} Hola')
        assert rv == 0
        assert out.strip() == 'Hola, Stranger.'


# --------------------------------------------------
def test_name():
    """ Accepts name """

    for opt in ['-n', '--name']:
        rv, out = getstatusoutput(f'{PRG} {opt} Jorge')
        assert rv == 0
        assert out.strip() == 'Howdy, Jorge.'


# --------------------------------------------------
def test_excited():
    """ Prints bang """

    for flag in ['-e', '--excited']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.strip() == 'Howdy, Stranger!'


# --------------------------------------------------
def test_all_options():
    """ Handles all options """

    rv, out = getstatusoutput(f'{PRG} -e -g Greetings -n Sarah')
    assert rv == 0
    assert out.strip() == 'Greetings, Sarah!'