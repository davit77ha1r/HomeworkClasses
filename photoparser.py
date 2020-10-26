import os
import requests
import webbrowser
import shutil
g = 0
class Start():
	# Makeing folder where will put all photos and add html of page
	def __init__(self,url):
		text = url
		if (".com" in text) == True:
			domain_find = text.find(".com") + len(".com")
		elif (".ru" in text) == True:
			domain_find = text.find(".ru") + len(".ru")
		elif (".net" in text) == True:
			domain_find = text.find(".net") + len(".net")
		elif (".am" in text) == True:
			domain_find = text.find(".am") + len(".am")
		if ("https://" in text) == True:
			url_name = text[8:domain_find]
			sec = "https://"
		if (("https://" in text) == False) and ("http://" in text) == True:
			sec = "http://"
			url_name = text[7:domain_find]
		self.url_name = url_name
		self.sec = sec
		self.url = url
		try:
			response = requests.get(url)
			with open("Parse_Photos/html_parser_code.html","w") as file:
				file.write(response.text)
		except:
			print("Error reading file")

	def Download(self):
		# Working with png
		global g
		list_png = []
		c = ""
		with open("Parse_Photos/html_parser_code.html","r") as file:
			text = file.read()
		for i in text:
			if i == " " or i == "\n":
				if (".png" in c) == True:
					list_png.append(c)
				c=""
			else:
				c += i
		for i in list_png:
			first_index = i.find("\"")
			devide = i[first_index+1 : len(i)]
			second_index = first_index + devide.find("\"")
			devide_2 = i[first_index+1 : second_index+1]
			if (self.url_name in i) == False:
				if (self.sec in devide_2) == False:
					devide_2 = self.sec + self.url_name + i[first_index+1 : second_index+1]
				else:
					devide_2 = url_name+i[first_index+1 : second_index+1]
			else:
				if (self.sec in devide_2) == False:
					devide_2 = self.sec+i[first_index+1 : second_index+1]
				else:
					devide_2 = i[first_index+1 : second_index+1]
			if (devide_2[-2] + devide_2[-1]) == "pn":
				devide_2 += "g"
			if ("////" in devide_2):
				devide_2 = devide_2.replace("////","//")
			if devide_2 == "https://" or devide_2 == "http://":
				continue
			try:
				response_1 = requests.get(devide_2)
				g += 1
				with open("Parse_Photos/Parse_photo_{}.png".format(g),"wb") as file:
					file.write(response_1.content)
				print("Download of {} is successfully done".format(devide_2))
			except:
				print("Can not download {}".format(devide_2))

		# Working with jpg
		list_jpg = []
		c = ""
		with open("Parse_Photos/html_parser_code.html","r") as file:
			text = file.read()
		for i in text:
			if i == " " or i == "\n":
				if (".jpg" in c) == True:
					list_jpg.append(c)
				c=""
			else:
				c += i
		for i in list_jpg:
			first_index = i.find("\"")
			devide = i[first_index+1 : len(i)]
			second_index = first_index + devide.find("\"")
			devide_2 = i[first_index+1 : second_index+1]
			if (self.url_name in i) == False:
				if (self.sec in devide_2) == False:
					devide_2 = self.sec + self.url_name + i[first_index+1 : second_index+1]
				else:
					devide_2 = url_name+i[first_index+1 : second_index+1]
			else:
				if (self.sec in devide_2) == False:
					devide_2 = self.sec+i[first_index+1 : second_index+1]
				else:
					devide_2 = i[first_index+1 : second_index+1]
			if (devide_2[-2] + devide_2[-1]) == "jp":
				devide_2 += "g"
			if ("////" in devide_2):
				devide_2 = devide_2.replace("////","//")
			if devide_2 == "https://" or devide_2 == "http://":
				continue
			try:
				response_1 = requests.get(devide_2)
				g += 1
				with open("Parse_Photos/Parse_photo_{}.jpg".format(g),"wb") as file:
					file.write(response_1.content)
				print("Download of {} is successfully done".format(devide_2))
			except:
				print("Can not download {}".format(devide_2))
	def MakeHTML(self):
		text = ""
		text = '''
<!DOCTYPE html>
<html>
<head>
	<title>Photo Parser</title>
</head>
<body>
		'''
		list_of_photos = (os.listdir(os.getcwd()+"/Parse_Photos"))
		for i in list_of_photos:
			if ((".png" in i) == True) or ((".jpg" in i) == True):
				text += "<img src=\"{}\">\n<br>\n<br>\n".format(i)
		text += '''
</body>
</html>
		'''
		with open("Parse_Photos/parsed_photos..html","w") as f:
			f.write(text)



try:
	os.mkdir("Parse_Photos")
except:
	d = input("Do you want to delete Folder and make new? (y/yes n/no):\n")
	if (d == "y") or (d == "Y"):
		shutil.rmtree(os.getcwd()+"/Parse_Photos")
		os.mkdir("Parse_Photos")



# The method to call for one site

#start_main = Start("https://xkcd.com/1699/")
#start_main.Download()
#start_main.MakeHTML()




# The parser for     xccd.com  
for i in range(300,320):
	start_main = Start("https://xkcd.com/{}/".format(i))
	start_main.Download()
	start_main.MakeHTML()