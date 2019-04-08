#!/usr/bin/python3
import sys
import csv


def category_mapper():
    v_types = set()
    data = list()
    reader = csv.reader(sys.stdin)
    for line in reader:
        if len(line) != 12:
            continue
        if line[0] == 'video_id':
            continue
        v_types.add(line[3].strip())
        video_id = line[0].strip()
        country = line[11].strip()
        category = line[3].strip()
        vnc = video_id + country
        data.append((category, vnc))

    for v_type in v_types:
        for parts in data:
            if v_type == parts[0].strip():
                 print("{}\t{}".format(parts[0], parts[1]))
        
        
        
if __name__ == "__main__":
    category_mapper()
