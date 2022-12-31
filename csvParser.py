import csv

# input name of csv file (Do NOT put .csv)
file = input("Enter name of file to open (Omit .csv): ")

# open CSV file for reading
with open("C:\\*\\*\\{}.csv".format(file), 'r') as f:
    reader = csv.reader(f)

# iterate over rows of the CSV file output to txt file
    with open("{}.txt".format(file), "w") as w: 
        for row in reader:
            w.write("\t".join(row) + "\n")


