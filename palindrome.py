#!/usr/bin/env python
# A simple script for checking if a given string is a palindrome.
# Copyright (C) 2016  Alan Garcia
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


def isPalindrome(string, punctuation=".,' "):
    for char in punctuation:
        string = string.replace(char, "")
    string = string.lower()
    return string == string[::-1]

if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        print(isPalindrome(argv[1]))
    if len(argv) == 3:
        print(isPalindrome(argv[1], argv[2]))
    else:
        print("usage: {0} <string> [<punctuation>]\n"
              "\tstring: the string to check\n"
              "\tpunctuation: a string consisting of valid punctuation.\n"
              "\t\tAny characters in <punctuation> are ignored when \n"
              "\t\tchecking the string.\n"
              "\t\tBy default this is set to \".,' \"".format(__file__))
