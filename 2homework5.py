# temperature = temp
class HouseTemperature:
	def __init__(self,name,current_temp_1,goal_temp_1,current_temp_2,goal_temp_2,):
		self.current_temp_1 = current_temp_1
		self.current_temp_2 = current_temp_2
		self.goal_temp_1 = goal_temp_1
		self.goal_temp_2 = goal_temp_2
		self.name = name
		print("\nIt is {}\n".format(name))
	
	def __del__(self):
		print("All operations with {} were finished".format(self.name))
	def __len__(self):
		return 2 # count of rooms
	def __str__(self):
		text = "room 1 temperature is {}\nroom 2 temperature is {}".format(self.current_temp_1,self.current_temp_2)
		return text
	
	def __repr__(self):
		text = "HouseTemperature(name={}, current_temp_1={}, goal_temp_1={}, current_temp_2={}, goal_temp_2={})".format(self.name,self.current_temp_1,self.goal_temp_1,self.current_temp_2,self.goal_temp_2)
		return text
	
	def get(self):
		text = "Now in first room temperature is {} and in second room temperature is {}".format(self.current_temp_1,self.current_temp_2)
		return text
	
	def set(self,set_temp_1 = 38,set_temp_2 = 38):
		self.current_temp_1 = set_temp_1
		self.current_temp_2= set_temp_2
		text = "You set temperature in room 1 to {} and in room 2 to {}".format(self.current_temp_1,self.current_temp_2)
		return text
	
	def sutisfed(self):
		text = ""
		if self.current_temp_1 == self.goal_temp_1:
			text += "In room 1 temperature is goal. It is {}\n".format(self.goal_temp_1) 
		else:
			text += "In room 1 temperature is not goal. It is {} but must be {}\n".format(self.current_temp_1,self.goal_temp_1)
		if self.current_temp_2 == self.goal_temp_2:
			text += "In room 2 temperature is goal. It is {}\n".format(self.goal_temp_2) 
		else:
			text += "In room 2 temperature is not goal. It is {} but must be {}\n".format(self.current_temp_2,self.goal_temp_2)
		return text

house_1 = HouseTemperature("House 1",15,25,17,30)
print(repr(house_1))
print(house_1.get())
print(house_1.set(25,30))
print(house_1.sutisfed())
print(str(house_1))
print("The lenght is {}".format(len(house_1)))
del(house_1)

house_2 = HouseTemperature("House 2",10,34,12,34)
print(repr(house_2))
print(house_2.get())
print(house_2.set(36,34))
print(house_2.sutisfed())
print(str(house_2))
print("The lenght is {}".format(len(house_2)))	
del(house_2)

house_3 = HouseTemperature("House 3",3,25,0,20)
print(repr(house_3))
print(house_3.get())
print(house_3.set(20,20))
print(house_3.sutisfed())
print(str(house_3))
print("The lenght is {}".format(len(house_3)))
del(house_3)

house_4 = HouseTemperature("House 4",40,30,40,30)
print(repr(house_4))
print(house_4.get())
print(house_4.set(25,25))
print(house_4.sutisfed())
print(str(house_4))
print("The lenght is {}".format(len(house_4)))
del(house_4)

