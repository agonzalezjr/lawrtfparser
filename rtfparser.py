import argparse
import os
import sys
import csv

parser = argparse.ArgumentParser(description='Parses RTF files.')

# if no 'directory' argument is passed, assume the cwd
parser.add_argument('-d', '--directory', default=os.getcwd(),
                    help='The directory with the RTF files to parse')
parser.add_argument('-o', '--output', default='output.csv',
                    help='The name of the output CSV file')

args = parser.parse_args()

dataFields = ['judge', 'case', 'court'];

# an array of dicts with the result of the run
data = [];

def dumpData(fileName, data, dataFields):
    print('Generating ' + fileName + ' ...')
    with open(fileName, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = dataFields)
        writer.writeheader()
        for row  in data:
            writer.writerow(row)
    print('Done.')

def processFile(root, file):
    print('Processing file: ' + os.path.join(root, file))

    # TODO: The actual parsing ...

    # For now, assume this is the output for each file
    dataRow = {}
    dataRow['judge'] = 'foo'
    dataRow['case'] = '123'
    data.append(dataRow)

if not os.path.isdir(args.directory):
    sys.exit('ERROR: passed argument is not a directory (' + args.directory + ')')

for root, dirs, files in os.walk(args.directory):
    for file in files:
        if file.endswith(".rtf"):
            processFile(root, file)

dumpData(args.output, data, dataFields)
