#Secret Message miniproject
#Note: Python3 code

import os
def rename():
	files = os.listdir(r"C:\Users\Pyllon\Downloads\alphabet\alphabet")
	os.chdir(r"C:\Users\Pyllon\Downloads\alphabet\alphabet")
	print (files)
	for file in files:
		os.rename(file, file.lstrip('0123456789'))