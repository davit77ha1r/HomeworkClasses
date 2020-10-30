import logging
import random
import threading
logging.basicConfig(filename='number_check.log',level=logging.DEBUG,format='%(asctime)s %(message)s')


class Start():
	def __init__(self):
		list_num = []
		for i in range(50):
			num = random.randint(0,50)
			list_num.append(num)
		self.list_num = list_num
	def Logging_start(self):
		def Check(num):
			if num >= 0 and num <= 9:
				logging.debug(f"Your number is {num} and   0 <= {num} <= 9  ")
				print(f"DEBUG:  Your number is {num} and   0 <= {num} <= 9  ") 
			elif num >= 10 and num <= 19:
				logging.info(f"Your number is {num} and   10 <= {num} <= 19  ")
				print(f"INFO:  Your number is {num} and   10 <= {num} <= 19  ")
			elif num >= 20 and num <= 29:
				logging.warning(f"Your number is {num} and   20 <= {num} <= 29  ")
				print(f"WARNING:  Your number is {num} and   20 <= {num} <= 29  ")
			elif num >= 30 and num <= 39:
				logging.error(f"Your number is {num} and   30 <= {num} <= 39  ")
				print(f"ERROR:   Your number is {num} and   30 <= {num} <= 39  ")
			elif num >= 40 and num <= 50:
				logging.critical(f"Your number is {num} and   40 <= {num} <= 50  ") 
				print(f"CRITICAL:   Your number is {num} and   40 <= {num} <= 50  ")

		for num in self.list_num:
			if __name__ == "__main__":
				x = threading.Thread(target=Check,args=(num,))
				x.start()
main = Start()
main.Logging_start()