#!/usr/bin/python3

import logging
logging.basicConfig(level=logging.INFO, format="(%(name)s) [%(levelname)s] %(message)s", datefmt='%d/%m/%Y %H:%M:%S')

import args
args.parse()

from args import Options

import back

if __name__ == '__main__' :
	if Options.doBack :
		back.dispatch()
