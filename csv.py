# CSV MODULE:- HOW TO READ, PARSE AND WRITE CSV FILES...

# EXAMPLE 1:- Reading to a CSV file:
import csv

with open('googhistory.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)             # Steps over the first line(Removes fields/column names)

    for line in csv_reader:
        print(line)               # Prints all columns....
        print(line[6])            # Prints a particular column index....


# EXAMPLE 2:- Writing to a CSV File from our original read() File:-
import csv

with open('googhistory.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_googhistory.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')       # Hyphen seperates csv file columns
        csv_writer = csv.writer(new_file, delimiter='\t')      # Tabs seperates csv file columns

        for line in csv_reader:
            csv_writer.writerow(line)


# EXAMPLE 3:- Reading csv data Using the DICTIONARY reader....
import csv

with open('googhistory.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)                     # Prints all fields and its value(key:value)....
        print(line['Close'])            # Prints only a specified field....


# EXAMPLE 4:- Writing csv data Using the DICTIONARY writer..
import csv

with open('googhistory.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_googhistory.csv', 'w') as new_file:
        fieldnames = ["b'Date", 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            # NB: To delete the 'volume' field, we'll remove it from the fieldnames list
            # And add this line of code here:- del line['Volume']
            csv_writer.writerow(line)
