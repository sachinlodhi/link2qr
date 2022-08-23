import csv
import pyqrcode
import png
from tqdm import tqdm


# distribution of the data is even i.e. 50% are benign and 50% are malicious
benign = 'images/benign/'
malicious = 'images/malicious/'
ctrM, ctrB = -1, -1

# rading using CSV module.... This would be changed to reading by pandas
file = open('balanced_urls.csv', mode='r')

# reading the CSV file
# csvFile = csv.reader(file)
# leaving the header
# next(csvFile, None)

# rading the csv rows in the line and then skipping the header
lines = file.readlines()[1:]
# stacking the lines in the list variable
lines = [line.rstrip() for line in lines]

# devision of the datast in 4 parts

part1 = lines[1:len(lines)//4]
part2 = lines[len(lines)//4:len(lines)//2]
part3 = lines[len(lines)//2:len(lines)//4 * 3 ]
part4 = lines[len(lines)//4 * 3:len(lines)]




# for lines in tqdm(iterable=csvFile, desc='Progress', total=632508):
#     if ctrB ==-1 and ctrM == -1:
#         ctrM, ctrB = 0, 0
#         continue
#     url = lines[0]
#     qr = pyqrcode.create(url)
#     if lines[2] == '0':
#         qr.png(benign+ str(ctrB) + ".png", scale=8)
#         ctrB+=1
#     else:
#         qr.png(malicious + str(ctrM) + ".png", scale=8)
#         ctrM+=1
#
#
#



