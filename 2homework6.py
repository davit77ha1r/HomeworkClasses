import os 
class Create:
	def __init__(self):
		base_dir = os.getcwd()
		self.base_dir = base_dir
	def __del__(self):
		print("Class Create finished its work:")
	def start(self,current_dir,dir_1,dir_2,dir_3,dir_4):
		base_dir = self.base_dir
		os.mkdir(current_dir)
		new_dir = base_dir+"/" + current_dir
		os.chdir(new_dir)
		os.mkdir(dir_1)
		new_dir += "/" + dir_1
		os.chdir(new_dir)
		os.mkdir(dir_2)
		os.mkdir(dir_3)
		new_dir += "/" + dir_3
		os.chdir(new_dir)
		os.mkdir(dir_4)
		self.new_dir = new_dir
		self.current_dir = current_dir
		self.dir_4 = dir_4
		self.dir_3 = dir_3
		self.dir_2 = dir_2
		self.dir_1 = dir_1

	def delete(self,output):
		if output == "y" or output == "Y":
			try:
				os.rmdir(os.getcwd()+"/"+self.dir_4)
				os.chdir("..")
				print("{} succesfully deleted".format(os.getcwd()+"/"+self.dir_4))
			except:
				print("Error deleting {} Operation breaked".format(os.getcwd()+"/"+self.dir_4))
			try:
				os.rmdir(os.getcwd()+"/"+self.dir_3)
				print("{} succesfully deleted".format(os.getcwd()+"/"+self.dir_3))
			except:
				print("Error deleting {} Operation breaked".format(os.getcwd()+"/"+self.dir_3))
			try:
				os.rmdir(os.getcwd()+"/"+self.dir_2)
				print("{} succesfully deleted".format(os.getcwd()+"/"+self.dir_2))
				os.chdir("..")
			except:
				print("Error deleting {} Operation breaked".format(os.getcwd()+"/"+self.dir_2))
			try:
				os.rmdir(os.getcwd()+"/"+self.dir_1)
				print("{} succesfully deleted".format(os.getcwd()+"/"+self.dir_1))

			except:
				print("Error deleting {} Operation breaked".format(os.getcwd()+"/"+self.dir_1))
			try:
				os.remove(os.getcwd()+"/file.txt")
				os.chdir("..")
				print("{} succesfully deleted".format(os.getcwd()+"/file.txt"))

			except:
				print("Error deleting {} Operation breaked".format(os.getcwd()+"/file.txt"))
			
			try:
				print("{} succesfully deleted".format(os.getcwd()+"/"+self.current_dir))
				os.rmdir(os.getcwd()+"/"+self.current_dir)
			except:
				print("Error deleting {} Operation breaked".format(os.getcwd()+"/"+self.current_dir))


main = Create()
main.start("Current_work_dir","Dir_1","Dir_2","Dir_3","Dir_4")
output = input("If you want to delete all in folder write \"y\"")
main.delete(output)