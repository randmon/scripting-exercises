import csv
import argparse

def printExam(date, time, partOfDay, course, location, format):
    result = format.replace(r'%d', date).replace('%t', time).replace(r'%p', partOfDay).replace(r'%c', course).replace('%l', location)
    print(result)

parser = argparse.ArgumentParser(prog='exam-schedule')
parser.add_argument('path')
parser.add_argument('id')
parser.add_argument('--format', default=r'%d at %t %c (location %l)')
args = parser.parse_args()

with open(args.path) as input:
    data = csv.DictReader(input)
    for s in data:
        id = s['Student ID']
        if id == args.id:
            printExam(s['Datum'], s['Startuur'], s['Dagdeel'], s['OLA Naam'], s['Lokaal'], args.format)