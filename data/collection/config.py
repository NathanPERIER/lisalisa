
import sys
import logging

LOG_FORMAT  = '(%(name)s) [%(levelname)s] %(message)s'
DATE_FORMAT = '%d/%m/%Y %H:%M:%S'


def __g_help(scriptfile: str, retcode: int) :
	print(f"usage : {scriptfile} [--debug]")
	sys.exit(retcode)


def processArgs(argv: "list[str]") :
	scriptfile = argv[0]

	args = argv[1:]

	if len(args) > 0 and args[0] in ['-h', '--help'] :
		__g_help(scriptfile, 0)
	
	log_level = logging.INFO
	if len(args) > 0 and args[0] == '--debug' :
		log_level = logging.DEBUG
	
	logging.basicConfig(level=log_level, format=LOG_FORMAT, datefmt=DATE_FORMAT)
