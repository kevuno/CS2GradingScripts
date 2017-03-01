"""
file: sli_testing_python_diff.py

Author: Kevin Bastian

"""

import subprocess
import os
import shutil
student_array = []
real_array = []
for student_file in os.listdir("stu/"):
	complete_stu_file = "stu/"+student_file
	student_array.append(complete_stu_file)
for real_file in os.listdir("real/"):
	complete_real_file = "real/"+real_file
	real_array.append(complete_real_file)

i = 0
for real_file in os.listdir("real/"):
		file_output = subprocess.Popen(['diff','--side-by-side','--suppress-common-lines','-w',real_array[i], student_array[i]], universal_newlines=True,  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		#save the output of each student at its own file
		output_filename = real_file+"+diff.txt"
		fout = open(output_filename, "w")
		fout.write(file_output.communicate()[0])
		fout.close()
		i+=1
		"""
		## Displaying output ##
		"""
		print("=========================================")
		print("=========================================")
		print("Diff for "+ real_file +": " )
		for line in open(output_filename):
			print(line)
				




