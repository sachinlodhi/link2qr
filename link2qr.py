import csv
import pyqrcode
import png

# distribution of the data is even i.e. 50% are benign and 50% are malicious
benign = 'images/benign/'
malicious = 'images/malicious/'
ctr = 0
# opening the CSV file
with open('balanced_urls.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)


    # displaying the contents of the CSV file
    for lines in csvFile:
        url = lines[0]
        qr = pyqrcode.create(url)
        if lines[2] == '0':
            qr.png(benign+ str(ctr) + ".png", scale=8)
        else:

            qr.png(malicious + str(ctr) + ".png", scale=8)

        break

