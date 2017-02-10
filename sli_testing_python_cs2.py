"""
file: sli_testing_python.py

Authors: Kevin Bastian, Andrew Berson

"""

import sys
import subprocess
import os
from shutil import copyfile
import shutil
args = sys.argv

"""
Modify the input test accordingly
"""
input_tests = ["1","2","3"]



"""
Run for each test:
1. Run the program file to be tested in a subprocess.
2. Store the output the file_output instance in bytes.
3. Create a file instance output to write the bytes.
4. Redirect the input if needed using a text file in the same call where it writes the output of the process.
5. Close the output file stream.
TODOS

1. Compare both the output file and the actual output file by just printing the differences.
2. Qualify the tests by a passing or not passing.
3. Personalize the lines and/or a range of characters to be ignored.

"""

"""
Config vars:
"""
require_input = False
base_stu_dir = "../"
student_testing_sol_dir = "stu"
real_sol_dir = "sol"
testing_dir = "src/poly/"
ignore = [103974,104311,105044]
output_dir = "../output/"

#input_dir = "input"
"""
actual_output_prefix = "ex"
actual_output_subfix = "_sol"
input_test_prefix = "ex"
input_test_subfix = ""
"""
import os
#For every student go inside the folder with the files, copy each of the files to testing directory at stu folder
for student_sol_dir in os.listdir(base_stu_dir):
	if(student_sol_dir[0].isdigit() and int(student_sol_dir.strip().split("-")[0]) in ignore):
		#In myCourses the fileformat is numbers-morenums - Lastname,Firstname - student_sol_dir
		student_fullname = student_sol_dir.strip().split("-")[2]
		student_dir = base_stu_dir + student_sol_dir
		student_dir_files = os.listdir(student_dir)		
		for ZipFolder in student_dir_files:
			content_dir = base_stu_dir + student_sol_dir
			content_dir = os.path.join(content_dir, ZipFolder)
			student_src_files = os.listdir(content_dir)
			for file_name in student_src_files:
				dest = testing_dir + student_testing_sol_dir
				src = content_dir
				full_file_name_src = os.path.join(src, file_name)
				#print(full_file_name_src)
				full_file_name_dest = os.path.join(dest, file_name)
				#print(full_file_name_dest)
				shutil.copy(full_file_name_src, full_file_name_dest)
		#After the files had been copied
		#Compile and run 
		
		#File to be compiled and run
		main = "src/PolyTest.java"
		#Compile---------
		file_output = subprocess.Popen(['javac','-sourcepath','src/', main], universal_newlines=True,  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		#save the output of each student at its own file
		output_filename = output_dir+student_fullname+"_compile_output.txt"
		fout = open(output_filename, "w")
		fout.write(file_output.communicate()[0])
		fout.close()
		#Run---------
		main_class = "PolyTest"
		file_output = subprocess.Popen(['java','-cp','src/', main_class], universal_newlines=True,  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		#save the output of each student at its own file
		output_filename = output_dir+student_fullname+"_run_output.txt"
		fout = open(output_filename, "w")
		fout.write(file_output.communicate()[0])
		fout.close()
		#Now read the program's run output
		print("=========================================")
		print("=========================================")
		print("Solution for "+ student_fullname +": " )
		for line in open(output_filename):
			print(line)
				

