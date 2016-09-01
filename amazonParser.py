import csv

output_file = open("bankingOutputAmz.csv", "w")
writer = csv.writer(output_file)


with open('report.csv', 'rb') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        date = row[1][1:6] + row[1][8:]
        amount = row[2][1:]
        description = row[3]
        writer.writerow([date, amount, description])

output_file.close()