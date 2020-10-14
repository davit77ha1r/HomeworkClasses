class Country:
	def __init__(self,c_name,continent):
		self.c_name = c_name
		self.continent = continent
	def presentation_country(self):
		text = "The making country is {} and it is in {} ".format(self.c_name,self.continent)
		print(text)
class Brand:
	def __init__(self,b_name,start_date):
		self.b_name = b_name
		self.start_date = start_date
	def presentation_brand(self):
		text = "It is from  {} brand and is made in {} ".format(self.b_name,self.start_date)
		print(text)
class Season:
	def __init__(self,s_name,temperature):
		self.s_name = s_name
		self.temperature = temperature
	def presentation_season(self):
		text = "You can choose it in {} when average temperature is {} ".format(self.s_name,self.temperature)
		print(text)
class Product (Country,Brand,Season):
	def __init__(self,c_name,continent,b_name,start_date,s_name,temperature,pr_name,pr_type,pr_price,pr_quality,discount):
		self.c_name = c_name
		self.continent = continent
		self.b_name = b_name
		self.start_date = start_date
		self.s_name = s_name
		self.temperature = temperature
		self.pr_name = pr_name
		self.pr_type = pr_type
		self.pr_price = pr_price
		self.pr_quality = pr_quality
		self.discount = discount
		Country.__init__(self,c_name,continent)
		Brand.__init__(self,b_name,start_date)
		Season.__init__(self,s_name,temperature)
	def mixed_presentation(self):
		self.presentation_country()
		self.presentation_brand()
		self.presentation_season()
		# QUality is here in print
		print("The name of product is {} \nThe type of product is {} \nProduct price is {} \nAnd product quality is {} from 10".format(self.pr_name,self.pr_type,self.pr_price,self.pr_quality))
	def discount_price(self):
		print("When discount is {} and price is {} the price will be {}".format(self.discount,self.pr_price,int((self.pr_price*(100-self.discount))/100)))

start = Product("China","Evrasia","MegaClothes",2005,"Summer",36.6,"Smurch","Bluse",5000,7,23)
start.mixed_presentation()
start.discount_price()
print("-"*30)
start = Product("Amerika","Amerika","SmartLamp",2015,"Winter",-10,"Lamp _sm 07","led",2500,9,10)
start.mixed_presentation()
start.discount_price()
print("-"*30)
start = Product("Armenia","Evrasia","Lori Panir",1979,"Summer",36.6,"Lori (Yuxayin)","Cheese",3000,8,15)
start.mixed_presentation()
start.discount_price()

