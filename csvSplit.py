import csv
import sys
import os


filename = '1crore - Copy.csv'
rows_per_csv = int(sys.argv[2]) if len(sys.argv) > 2 else 500000

with open(filename) as infile:
    reader = csv.DictReader(infile)
    header = reader.fieldnames
    rows = [row for row in reader]
    pages = []

    row_count = len(rows)
    start_index = 0

    while start_index < row_count:
        pages.append(rows[start_index: start_index+rows_per_csv])
        start_index += rows_per_csv

    for i, page in enumerate(pages):
        with open('Split(20)-1crore\{}_{}.csv'.format('sample', i+1), 'w',newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=header)
            writer.writeheader()
            for row in page:
                writer.writerow(row)

        print('DONE splitting {} into {} files'.format(filename, len(pages)))
