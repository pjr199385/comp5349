#!/usr/bin/python3
import sys


def category_mapper():

    for line in sys.stdin:
        parts = line.strip().split("\t")
        if len(parts) != 12 | parts[0] == 'video_id':
          continue
        video_id = parts[0].strip()
        country = parts[11].strip()
        category = parts[3].strip()
        vnc = video_id + country

        print("{}\t{}".format(category, vnc))


if __name__ == "__main__":
    category_mapper()