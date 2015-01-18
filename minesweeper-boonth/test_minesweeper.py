"""
Tests for minesweeper. Meant to be run with py.test.

usage: py.test -v test_minesweeper.py

"""

import os
import sys

import minesweeper_adaptor

def test_no_field():
    """Test of no fields in input file"""

    input = ('0 0')
    expected_output = ('')
    expected_output = expected_output.replace('\n', os.linesep)

    output = minesweeper_adaptor.run_minesweeper(input)
    assert output == expected_output

def test_1x1_no_mine():
    """Test of small field with no mine"""

    input = ('1 1\n'
             '.\n'
             '0 0')
    expected_output = ('Field #1:\n'
                       '0\n'
                       '\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = minesweeper_adaptor.run_minesweeper(input)
    assert output == expected_output

def test_1x1_mine():
    """Test of small field with a mine"""

    input = ('1 1\n'
             '*\n'
             '0 0')
    expected_output = ('Field #1:\n'
                       '*\n'
                       '\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = minesweeper_adaptor.run_minesweeper(input)
    assert output == expected_output

def test_4x4_no_mine():
    """Test of 4x4 field with no mines"""

    input = ('4 4\n'
             '. . . .\n'
             '. . . .\n'
             '. . . .\n'
             '. . . .\n'
             '0 0')
    expected_output = ('Field #1:\n'
                       '0 0 0 0\n'
                       '0 0 0 0\n'
                       '0 0 0 0\n'
                       '0 0 0 0\n'
                       '\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = minesweeper_adaptor.run_minesweeper(input)
    assert output == expected_output

def test_4x4_1mine_1():
    """Test of 4x4 field with 1 mine in a corner"""

    input = ('4 4\n'
             '* . . .\n'
             '. . . .\n'
             '. . . .\n'
             '. . . .\n'
             '0 0')
    expected_output = ('Field #1:\n'
                       '* 1 0 0\n'
                       '1 1 0 0\n'
                       '0 0 0 0\n'
                       '0 0 0 0\n'
                       '\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = minesweeper_adaptor.run_minesweeper(input)
    assert output == expected_output

def test_4x4_1mine_2():
    """Test of 4x4 field with 1 mine in the middle"""

    input = ('4 4\n'
             '. . . .\n'
             '. . . .\n'
             '. * . .\n'
             '. . . .\n'
             '0 0')
    expected_output = ('Field #1:\n'
                       '0 0 0 0\n'
                       '1 1 1 0\n'
                       '1 * 1 0\n'
                       '1 1 1 0\n'
                       '\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = minesweeper_adaptor.run_minesweeper(input)
    assert output == expected_output

def test_4x4_2mines():
    """Test of 4x4 field with 2 mines"""

    input = ('4 4\n'
             '. . . .\n'
             '. . . *\n'
             '. * . .\n'
             '. . . .\n'
             '0 0')
    expected_output = ('Field #1:\n'
                       '0 0 1 1\n'
                       '1 1 2 *\n'
                       '1 * 2 1\n'
                       '1 1 1 0\n'
                       '\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = minesweeper_adaptor.run_minesweeper(input)
    assert output == expected_output

def test_4x4_16mines():
    """Test of 4x4 field with all mines"""

    input = ('4 4\n'
             '* * * *\n'
             '* * * *\n'
             '* * * *\n'
             '* * * *\n'
             '0 0')
    expected_output = ('Field #1:\n'
                       '* * * *\n'
                       '* * * *\n'
                       '* * * *\n'
                       '* * * *\n'
                       '\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = minesweeper_adaptor.run_minesweeper(input)
    assert output == expected_output

def test_acceptance():
    """Test example acceptance input listed in book"""

    input = ('4 4\n'
             '* . . .\n'
             '. . . .\n'
             '. * . .\n'
             '. . . .\n'
             '3 5\n'
             '* * . . .\n'
             '. . . . .\n'
             '. * . . .\n'
             '0 0')
    expected_output = ('Field #1:\n'
                       '* 1 0 0\n'
                       '2 2 1 0\n'
                       '1 * 1 0\n'
                       '1 1 1 0\n'
                       '\n'
                       'Field #2:\n'
                       '* * 1 0 0\n'
                       '3 3 2 0 0\n'
                       '1 * 1 0 0\n'
                       '\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = minesweeper_adaptor.run_minesweeper(input)
    assert output == expected_output


