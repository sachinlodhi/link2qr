# threading is used in this implementation

# -*- coding: utf-8 -*-
"""link2qr.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-IpMvSjs8wZXQiqztykHIGBnXFP0Qo1K
"""
import csv
import pyqrcode
import png
from tqdm import tqdm
import threading
import time


# distribution of the data is even i.e. 50% are benign and 50% are malicious
benign = 'images/benign/'
malicious = 'images/malicious/'
ctrM, ctrB = 0, 0

file = open('/content/URLS/balanced_urls.csv', mode='r')

# reading the CSV file
csvFile = csv.reader(file)

lines = file.readlines()[1:]

lines = [line.rstrip() for line in lines]


# part1 = lines[0:158127]
# part2 = lines[158127:316254]
# part3 = lines[316254:474381]
# part4 = lines[474381:632508]


print(len(lines)//4)
print(len(lines)//2)
print(len(lines)//4 * 3)
print(len(lines))

part1 = lines[1:len(lines)//4]
part2 = lines[len(lines)//4:len(lines)//2]
part3 = lines[len(lines)//2:len(lines)//4 * 3 ]
part4 = lines[len(lines)//4 * 3:len(lines)]

def QRgen(recs):
  global ctrB, ctrM
  print('in function')
  for line in tqdm(iterable=recs, desc='Progress', total=len(recs)):
      # if ctrB ==-1 and ctrM == -1:
      #     ctrM, ctrB = 0, 0
      #     continue
      line = line.split(',')
      print(line)
      url = line[0]
      flag = line[2]
      qr = pyqrcode.create(url)
      if flag == '0':
          qr.png(benign+ str(ctrB) + ".png", scale=8)
          ctrB+=1
          print("saved")
      else:
          qr.png(malicious + str(ctrM) + ".png", scale=8)
          ctrM+=1

# import shutil
# shutil.rmtree("/content/images/benign")

# $QRgen(part1)


t1 = threading.Thread(target=QRgen, args=(part1,))
t1.start()

t2 = threading.Thread(target=QRgen, args=(part2,))
t2.start()


t3 = threading.Thread(target=QRgen, args=(part3,))
t3.start()

t4 = threading.Thread(target=QRgen, args=(part4,))
t4.start()

# def test(val):
#   for i in range(1000000):
#     print(val, i)
#
# t1 = threading.Thread(target=test, args=("first",))
# t1.start()
#
# t2 = threading.Thread(target=test, args=("second",))
# t2.start()
#
# print(time.time())
