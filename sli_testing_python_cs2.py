"""
file: sli_testing_python.py

Author: Kevin Bastian

"""

import subprocess
import os
import shutil

"""
Run for each student:
1. Copy files to the testing directory.
2. Compile classes inside the testing directory and run program with given arguements.
3. Save output of the compile and run into a file.
4. Display each line of the run output.
5. For next student, the copy will overwrite the files. (TODO, delete files so that if one student is missing a file, it doesn't a previous copied file of another student)
"""

"""
Config vars:
"""
arguments = ""
files_inside_folder = False #In some submissions, their java classes will be inside a folder, which is then inside the zip file; otherwise the files are just inside the zip file.
base_stu_dir = "../" #The base directory, where all the students implementation is found (each folder has another folder with some name, that last folder is the one containing the java files)
student_testing_sol_dir = "stu" #The name of the folder where the student's solution is found
testing_dir = "src/poly/" #The root folder where the student's solution and where the correct and actual solution (the one provided by CS deparment) is found
ignore = [103974,104311,105044] #Student ID's that have their files in a different structure than the one they were asked to
output_dir = "../output/" #Where to save the output of the compile and run
data_dir = "" #Directory containing some data files (usually .txt files)
main = "src/PolyTest.java" #File to be compiled and run

"""
File copying function. Inside the given directory
"""
def copy_files(src_dir,dest_dir):
	for file_name in os.listdir(src_dir):
		"""
		## COPYING ##
		"""
		full_file_name_src = os.path.join(src_dir, file_name)
		full_file_name_dest = os.path.join(dest_dir, file_name)
		shutil.copy(full_file_name_src, full_file_name_dest)





for student_sol_dir in os.listdir(base_stu_dir):
	if(student_sol_dir[0].isdigit() and int(student_sol_dir.strip().split("-")[0]) not in ignore): #make sure that we only go inside student folders and that they are not ignored
		#In myCourses the fileformat is numbers-morenums - Lastname,Firstname - student_sol_dir
		student_fullname = student_sol_dir.strip().split("-")[2]
		student_dir = base_stu_dir + student_sol_dir
		#Check wether their files are inside another folder or if they are already inside the first unzipped folder
		if(files_inside_folder):
			for ZipFolder in os.listdir(student_dir):
				source = os.path.join(student_dir, ZipFolder)
				dest = testing_dir + student_testing_sol_dir
				copy_files(source,dest)
		else:
				dest = testing_dir + student_testing_sol_dir
				copy_files(student_dir,dest)
		"""
		## Compiling ##
		"""
		file_output = subprocess.Popen(['javac','-sourcepath','src/', main], universal_newlines=True,  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		#save the output of each student at its own file
		output_filename = output_dir+student_fullname+"_compile_output.txt"
		fout = open(output_filename, "w")
		fout.write(file_output.communicate()[0])
		fout.close()
		"""
		## Running ##
		"""
		main_class = "PolyTest"
		file_output = subprocess.Popen(['java','-cp','src/', main_class], universal_newlines=True,  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		#save the output of each student at its own file
		output_filename = output_dir+student_fullname+"_run_output.txt"
		fout = open(output_filename, "w")
		fout.write(file_output.communicate()[0])
		fout.close()
		"""
		## Displaying output ##
		"""
		print("=========================================")
		print("=========================================")
		print("Solution for "+ student_fullname +": " )
		for line in open(output_filename):
			print(line)
				

