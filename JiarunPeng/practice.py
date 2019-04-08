#!/usr/bin/python3
import sys
import csv


def category_mapper():
    print('inside')
    reader = csv.reader(sys.stdin)
    data = list()
    for line in reader:
        n = 0
        if len(line) != 12:
            continue
        if line[0] == 'video_id':
            continue
        video_id = line[0].strip()
        country = line[11].strip()
        category = line[3].strip()
        vnc = video_id + country
        data.append((category, vnc))
        n = n + 1

    v_types = set()
    
    for line in data:
        v_types.add(line[0].strip())

    for v_type in v_types:
        country_count = set()
        video_count = set()
        for category, vnc in data:
            video_id = vnc[0:-2]
            if v_type == category:
                country_count.add(vnc)
                video_count.add(video_id)
        division_1 = len(country_count)
        division_2 = len(video_count)
        if division_2 == 0:
            result = 0.0
        else:
            result = round((float(division_1) / float(division_2)), 2)
        print("{}\t:{}".format(v_type, result))


if __name__ == "__main__":
    category_mapper()