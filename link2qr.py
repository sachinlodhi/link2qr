import csv
import pyqrcode
import png
from tqdm import tqdm

# distribution of the data is even i.e. 50% are benign and 50% are malicious
benign = 'images/benign/'
malicious = 'images/malicious/'
ctrM, ctrB = 0, 0



# opening the CSV file
with open('balanced_urls.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)


    # displaying the contents of the CSV file
    for lines in tqdm(csvFile,desc="Progress"):
        url = lines[0]
        qr = pyqrcode.create(url)
        if lines[2] == '0':
            qr.png(benign+ str(ctrB) + ".png", scale=8)
            ctrB+=1
        else:
            qr.png(malicious + str(ctrM) + ".png", scale=8)
            ctrM+=1




