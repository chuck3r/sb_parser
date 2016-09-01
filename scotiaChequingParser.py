import csv

output_file = open("bankingOutputSco.csv", "w")
writer = csv.writer(output_file)


with open('pcbanking.csv', 'rb') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        if row[1][0] == '-' and row[3] != "ABM Withdrawal":
            date = row[0]
            amount = row[1][1:]
            description = " ".join(row[4].lower().split())
            writer.writerow([date, amount, description])

with open('pcbanking.csv', 'rb') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        if row[1][0] != '-':
            date = row[0]
            amount = row[1]
            description1 = " ".join(row[3].lower().split())
            description = " ".join(row[4].lower().split())
            writer.writerow([date, amount, description, description1])

output_file.close()
    