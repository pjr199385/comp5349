#!/usr/bin/python3
import sys
import csv


def category_mapper():
    v_types = set()
    data = list()
    data_dad = list()
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
                data_dad.append((parts[0].strip(), parts[1].strip()))
#                 print("{}\t{}".format(parts[0], parts[1]))

    country_count = set()
    video_count = set()
    current_category = ""
    for category, vnc in data_dad:
        video_id = vnc[0:-2]
        if current_category != category:
            if current_category !="":
                division_1 = len(country_count)
                division_2 = len(video_count)
                if division_2 == 0:
                    result = 0.0
                else:
                    result = round((float(division_1) / float(division_2)), 2)
                country_count = set()
                video_count = set()
                print("{}\t:{}".format(current_category, result))
            current_category = category
        country_count.add(vnc)
        video_count.add(video_id)
    division_1 = len(country_count)
    division_2 = len(video_count)
    if division_2 == 0:
        result = 0.0
    else:
        result = round((float(division_1) / float(division_2)), 2)
    print("{}\t:{}".format(current_category, result))
        
        
        
if __name__ == "__main__":
    category_mapper()