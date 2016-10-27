import argparse
import os
import sys

parser = argparse.ArgumentParser(description='Parses RTF files.')

# if no 'directory' argument is passed, assume the cwd
parser.add_argument('-d', '--directory', default=os.getcwd(),
                    help='The directory with the RTF files to parse')

args = parser.parse_args()

def processFile(root, file):
    # TODO: Everything :)
    print(os.path.join(root, file))

if not os.path.isdir(args.directory):
    sys.exit('ERROR: passed argument is not a directory (' + args.directory + ')')

for root, dirs, files in os.walk(args.directory):
    for file in files:
        if file.endswith(".rtf"):
            processFile(root, file)
