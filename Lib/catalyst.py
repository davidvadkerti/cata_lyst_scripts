# -*- coding: utf-8 -*- 
# Python library for Dynamo nodes

# for easy batch setting of custom log path
dyn_log_path = "L:\\customToolslogs\\dynLogs\\"

# logging Dynamo script usage
def dyn_logger(filePath,user_name,script_name):
	# Dynamo library for easy batch setting of custom paths
	from datetime import datetime
	try:
		lastBackslash = filePath.rindex("\\")+1
	except:
		lastBackslash = filePath.rindex("/")+1
	file_name = filePath[lastBackslash:]
	#user_name = getpass.getuser()
	datestamp = str(datetime.now())
	# tabulator between data to easy import to excel schedule
	separator = "\t"
	line = datestamp + separator + script_name + separator + user_name + "\n"

	try:
		f = open("L:\\customToolslogs\\dynLogs\\" + file_name +".log", "a")
		f.write(line)
		f.close()
		return "log has been written"
	except:
		return "something went wrong"