#!/usr/bin/python3
import sys
import csv


def category_mapper():
    print('inside')
    n = 1
    reader = csv.reader(sys.stdin)
    for line in reader:
        n = n + 1
        if len(line) != 12 :
          continue
        video_id = line[0].strip()
        country = line[11].strip()
        category = line[3].strip()
        vnc = video_id + country
        print("{}\t{}".format(category, vnc))
        
        
if __name__ == "__main__":
    category_mapper()