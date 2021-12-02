import csv
import sys
import os


if len(sys.argv) > 2:
    rows_per_csv = int(sys.argv[2])
else: 
    rows_per_csv=1000000

with open('2Crore - Copy.csv') as inp:
    r = csv.DictReader(inp)
    head = r.fieldnames
    rows = [row for row in r]
    list = []

    cnt = len(rows)
    idx = 0

    while idx < cnt:
        end=idx+rows_per_csv
        list.append(rows[idx: end])
        idx +=rows_per_csv

    for i, page in enumerate(list):
        with open('Split(20)-2crore\{}_{}.csv'.format('sample', i+1), 'w',newline='') as f:
            writer = csv.DictWriter(f, fieldnames=head)
            writer.writeheader()
            for row in page:
                writer.writerow(row)

        print('splitted into {} files'.format(len(list)))