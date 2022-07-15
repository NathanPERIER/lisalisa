
import sys

class Options :
	debugMode = False
	doFront   = False
	doBack    = True


def __d_help(ret_code = 0) :
	script = sys.argv[0]
	print(f"usage : {script} [--front] [--back] [--debug]")
	sys.exit(ret_code)


def parse() :
	args = sys.argv[1:]

	if len(args) > 0 and args[0] in ['-h', '--help'] :
		__d_help(0)

	if len(args) > 0 and args[0] == '--front' :
		Options.doFront = True
		del args[0]
	
	if len(args) > 0 and args[0] == '--back' :
		Options.doBack = True
		del args[0]
	
	if len(args) > 0 and args[0] == '--debug' :
		Options.debugMode = True
		del args[0]
	
	if len(args) > 0 :
		__d_help(1)
