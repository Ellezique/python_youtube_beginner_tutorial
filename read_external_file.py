#read external files

#Open file. r for read, w for write, a for appending info to end of file, r+ is read and write
employee_file = open("employees.txt", "r")
# print(employee_file.readable()) #returns boolean e.g true if file can read.
# print(employee_file.readline()) #read line from file
# print(employee_file.readlines()) #read each line and to array
# print(employee_file.readlines()[1]) 
for employee in employee_file.readlines():
  print(employee)
#close file
employee_file.close()

#a for appending info to end of file
employee_file = open("employees.txt", "a")
employee_file.write("\nEmployee 99")
employee_file.close() #writes to txt file.


#w for write. will overwrite the entire file. 3:28:00