import csv
import argparse
import sys

import requests
from Filtering import Filtering
from Sorting import Sorting
from File_processing import File_processing

file_processing = File_processing()
filtering = Filtering()
sorting = Sorting()
file_processing.Save_file()


parser = argparse.ArgumentParser(description='Arguments')
parser.add_argument("--sort_by", type=str, help="Name of column")
parser.add_argument("--filter_by", required=False, type=str, help="", nargs=2)

args = parser.parse_args()

sort_by_args = args.sort_by
filter_by_args = args.filter_by

if len(sys.argv) == 1:
    print("Choose one option: sort_by or filter_by")
elif sys.argv[1] == "--sort_by":
    sorting.Sort(sort_by_args)
elif sys.argv[1] == "--filter_by":
    filtering.Filter(sys.argv[2],sys.argv[3])
