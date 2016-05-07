try:
	raise Exception('Error.com')
except:
	error_file = open('C:\\error_log.txt', 'a')
	error_file.write(traceback.format_exc())
	error_file.close()
	print('A traceback entry has been written to error_log.txt')
