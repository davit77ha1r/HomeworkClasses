# Importing Libraries
from sqlite3 import Error
import sqlite3
import json




# Making main functions under Class
class Database_methods:
	def __init__(self,file_name):
		# Getting file name
		self.database = "film.db"

		# Trying to connect to  db  file in exception print it
		try:
			self.conn = sqlite3.connect(self.database)
		except Error as e:
			print(e)
		curs = self.conn.cursor()
		self.curs = curs
	

	# Main function wich returns all titles with OUR letter
	def find_starting_letter(self,letter):
		return_text = "\n--------You call find starting letter function----------\n\n"

		# It is method when  you run it it get all elements from OUR file wich is starting with OUR letter
		get_titles = '''SELECT *
						FROM film
						WHERE title LIKE '{}%'
						ORDER BY title
			'''.format(letter)

		self.curs.execute(get_titles)
		answer = self.curs.fetchall()

		# It is method wich help us to get only file titles 
		for i in range(len(answer)):
			info_of_film = answer[i]
			return_text += "Finding match {}:\t{}\n".format(i,info_of_film[1])
		return_text += "Matches count: {}".format(i)
		return return_text

	def longest(self):
		return_text = "\n----------You call the longets function----------\n\n"
		# Method to find the maximum value of lenght 
		max_length= '''SELECT MAX(length)
						FROM film
						ORDER BY title'''


		# Getting maximum length of film
		self.curs.execute(max_length)
		length = self.curs.fetchall()
		length = (length[0])[0]


		# Its find the longest film Title
		title_of_longest = '''
		SELECT title
		FROM film
		WHERE length = {}'''.format(length)

		# Calling method to find the longest film title
		self.curs.execute(title_of_longest)
		title = self.curs.fetchall()
		title = (title[0])[0]
		

		# Making return text and returning it
		return_text += 'The longest film is \"{}\" wich length is {} minutes.'.format(title,length)
		return return_text

	def db_to_json(self):
		return_text = "\n----------You call database to json function----------\n\n"
		return_text += "Reading information...\n"

		# Reading all info from db file
		db_to_js_request = '''
						SELECT *
						FROM film '''
		with self.conn:
			self.curs.execute(db_to_js_request)
			db_text = self.curs.fetchall()

		# Making new dictionary to write there info from database then we put it in json (json accept only putting dictionaries)
		text = ""
		return_text += "Making database to json file...\n"
		for i in range(len(db_text)):
			dict_second = {}
			tuple_text = db_text[i]
			dict_second["film_id"] = tuple_text[0]
			dict_second["title"] = tuple_text[1]
			dict_second["description"] = tuple_text[2]
			dict_second["release_year"] = tuple_text[3]
			dict_second["rate"] = tuple_text[4]
			dict_second["length"] = tuple_text[5]
			dict_second["special_features"] = tuple_text[6]
			text += json.dumps(dict_second)+",\n"
		with open("database_json.json","w") as file:
			file.write(text)
		return_text += "Convert finished successfully!"
		return return_text

		# Making new method for extra task
	def find_fitered_films(self):
		return_text = '\n----------You call find fitered films function----------\n\n'
		# Reading all films wich is above 2010 and is between 3 and 5
		find_fitered = '''SELECT *
						  FROM film
						  WHERE release_year > 2010 and rate BETWEEN 3 and 5 '''
		with self.conn:
			self.curs.execute(find_fitered)
		fitered_films = self.curs.fetchall()

		# Making new database where we will put all fitired fillms
		make_table = ''' CREATE TABLE IF NOT EXISTS fiteredfilm(
								id integer PRIMARY KEY,
								film_id integer NOT NULL,
								title text,
								description text,
								release_year integer,
								rate float,
								length integer,
								special_features text
								); '''
		database = ("FiteredFilms.db")
		conn = sqlite3.connect(database)
		curs = conn.cursor()
		curs.execute(make_table)

		# Inserting all films in database
		for i in range(len(fitered_films)):
			info_of_film = fitered_films[i]
			insert_query = ''' INSERT INTO fiteredfilm(id, film_id,title,description,release_year,rate,length,special_features)
							   VALUES({},{},'{}','{}',{},{},{},'{}')
							'''.format(i+1,info_of_film[0],info_of_film[1],info_of_film[2],info_of_film[3],int(info_of_film[4]),info_of_film[5],info_of_film[6])
			
			# It says when file is already exists
			try:
				curs.execute(insert_query)
				conn.commit()
			except:
				return_text += ("\nFile is ready if you want to make again remove previus")
				break
			return_text += ("\n{}  \"{}\"  inserted in fitered films".format(i+1,info_of_film[1]))
		
		# Returning some data about this fanction
		return return_text
		
start = Database_methods("film.db") # Calling class with our database name

# Calling method wich returns all film names wich is starting with OUR letter
print(start.find_starting_letter("B")) # Calling OUR function with leetter wich we want to start all film names

# Calling method wich returns us the longest film with length
print(start.longest())

# Calling method wich convert database file to json file and returned if all finished
print(start.db_to_json())

# Calling extra method wich read all fitered films and added it in new database
print(start.find_fitered_films())