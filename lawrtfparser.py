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

dataFields = ['Judge', 'Docket', 'Topic', 'Court',  'Date', 'Parties'];

# an array of dicts with the result of the run
data = [];
lines = [];

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

    f = open(root+'/'+file,'r')
    for line in f:
        lines.append(line)
    f.close()

    dataRow = {}

    for i in range(0,len(lines)):

        if lines[i].find("Judge(s)") == 0:

            # whenever we find a new Judge(s), save what we have collected so far
            # if we have collected anything at all and start a new row
            if dataRow:
                data.append(dataRow)
                dataRow = {}

            dataRow['Judge'] = lines[i+1]

        elif lines[i].find("Related Docket(s)") == 0:

            dataRow['Docket'] = lines[i+1]

        elif lines[i].find("Topic(s)") == 0:

            dataRow['Topic'] = lines[i+1]

        elif lines[i].find("Court") == 0:

            dataRow['Court'] = lines[i+1]

        elif lines[i].find("Date Filed") == 0:

            dataRow['Date'] = lines[i+1]

        elif lines[i].find("Parties") == 0:

            dataRow['Parties'] = lines[i+1]

# Script execution starts here
if not os.path.isdir(args.directory):
    sys.exit('ERROR: passed argument is not a directory (' + args.directory + ')')

for root, dirs, files in os.walk(args.directory):
    for file in files:
        if file.endswith(".txt"):
            processFile(root, file)

dumpData(args.output, data, dataFields)
