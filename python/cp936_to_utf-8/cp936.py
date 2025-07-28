#!/usr/bin/env python3

import sys

def translate(filename):
    source = open(filename, encoding='cp936')

    target_filename = filename + '.md'
    target = open(target_filename, 'w', encoding='utf-8')

    target.write(source.read())

if __name__ == '__main__':

    translate(sys.argv[1])
