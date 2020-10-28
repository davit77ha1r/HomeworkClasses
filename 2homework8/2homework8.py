import json
import requests
import threading
import os
import time
class Start():
  def __init__(self):

    # Making dictionaries
    dict_jpg = {}
    dict_png = {}

    # Openning json file to read what is inside it and to get photo url s
    with open("2homework8.json","r") as file:
      text = json.load(file)
    text = text["items"]

    # Adding jpg files to jpg dictionary, png files to png dictionary
    for i in text:
      if (".jpg" in i['url']) == True:
        dict_jpg[i['name']] = i['url']
      elif (".png" in i['url']) == True:
        dict_png[i['name']] = i['url']

    # Making self arguments
    self.dict_png = dict_png
    self.dict_jpg = dict_jpg
    self.text = text 

  # Method to start download process
  def Download(self):
    self.num = 1

    # Main openning method
    def main_png(name):

      # Downloading png files
      response = requests.get(self.dict_png[name])
      with open("{}.png".format(name),"wb") as file:
        file.write(response.content)
      print("{} is successfully downloaded".format(name))
      self.num += 1

    def main_jpg(name):

      # Downloading jpg files
      response = requests.get(self.dict_jpg[name])
      with open("{}.jpg".format(name),"wb") as file:
        file.write(response.content)
      print("{} is successfully downloaded".format(name))
      self.num += 1



    if __name__ == '__main__':
      for i in self.dict_png:
        x = threading.Thread(target=main_png,args=(i,))
        x.start()
      for i in self.dict_jpg:
        x = threading.Thread(target=main_jpg,args=(i,))
        x.start()

  # make html file 
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
    for i in os.listdir():
      print(i)
      if ((".png" in i) == True) or ((".jpg" in i) == True):
        text += "<h2>{}</h2><br>\n<img src=\"{}\">\n<br>\n<hr>\n".format(i,i)
    text += '''
    </body>
    </html>
        '''
    with open("1_parsed_photos..html","w") as f:
      f.write(text)



# calling Main functions
main=Start()
main.Download()
time.sleep(2)
main.MakeHTML()