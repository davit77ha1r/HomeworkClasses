
class Hotel():

	def __init__(self,name_hotel,place,mid_room_price,lux_room_price):
		dict_1 = {"room_1":"Busy","room_2":"Free","room_3":"Free","room_4":"Free","room_5":"Busy"}
		dict_2 = {"room_1":"Free","room_2":"Busy","room_3":"Free","room_4":"Busy","room_5":"Free","room_6":"Busy","room_7":"Free",}
		self.name_hotel = name_hotel
		self.place = place
		self.rooms_mid = dict_1
		self.mid_room_price = mid_room_price
		self.rooms_lux = dict_2
		self.lux_room_price = lux_room_price
	def presentation(self):
		text = "-"*10 + "HOTEL" + "-"*10
		text += "\nWelcome to {} in our Hotel:\nIt is in {}\nMid rooms are {} and the mid room price is {}\nLux rooms are {} and lux rooms price is {}".format(self.name_hotel,self.place,self.rooms_mid,self.mid_room_price,self.rooms_lux,self.lux_room_price)
		return text
	def booking(self):
		room_lux_or_mid = input("Enter lux or mid room:\n")
		if room_lux_or_mid =="lux" or room_lux_or_mid =="Lux":
			room = input("Enter room name:\n")
			self.rooms_lux[room] = "Busy"
			text = f"You are booking {room}Thanks for booking\nNow rooms are {self.rooms_lux}"
			return text
		if room_lux_or_mid =="mid" or room_lux_or_mid =="Mid":
			room = input("Enter room name:\n")
			self.rooms_mid[room] = "Busy"
			text = f"You are booking {room}Thanks for booking\nNow rooms are {self.rooms_mid}"
			return text
	def discount(self,discount_mid,discount_lux):
		print(self.mid_room_price,self.lux_room_price)
		a = (self.mid_room_price*(100-discount_mid))/100
		b = (self.lux_room_price*(100-discount_lux))/100
		text = "The discount for mid room is {} and the price now is {}\nThe discount for lux room is {} and the price now is {}".format(discount_mid,a,discount_lux,b)
		return text


class Taxi():
	def __init__(self,name_taxi,price_for_tour):
		list_1 = ("nissan teana","mersetes c klass","BMW x 5","Mersedes kupe","toyota plyus 3","toyota camry","BMW X6","Toyoto corola","Mersedes G class")
		self.name_taxi = name_taxi
		self.car_types = list_1
		self.price_for_tour = price_for_tour
	def presentation(self):
		text = "-"*10 + "TAXI" + "-"*10
		text += "\nWelcome to {} Taxi company\nOur car types are {}\nAnd price is {} AMD".format(self.name_taxi,self.car_types,self.price_for_tour)
		return text
	def discount(self,discount):
		self.discount_taxi = (self.price_for_tour*(100 - discount))/100
		text = "The discount is {} and you must pay {} for 1 kilometer".format(discount,self.discount_taxi)
		return text



class Tour(Taxi,Hotel):
	def __init__(self,name,name_hotel,place,mid_room_price,lux_room_price,name_taxi,price_for_tour,taxi_discount,htm,htl,):
		Hotel.__init__(self,name_hotel,place,mid_room_price,lux_room_price)
		print(Hotel.presentation(self))
		Hotel.booking(self)
		print(Hotel.discount(self,htm,htl))
		Taxi.__init__(self,name_taxi,price_for_tour)
		print(Taxi.presentation(self))
		text = "-"*10 + "TOUR" + "-"*10
		text += "The lux tour is {}\nThe mid tour is {}".format(lux_room_price+price_for_tour,mid_room_price+price_for_tour)
		print(text)



ok = Tour("MyCity Tour","Classio","Amerika,New York",30000,50000,"Super_Fast",50000,30,15,20)