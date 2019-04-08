 #!/usr/bin/python3

import sys


def read_map_output(file):
    for line in file:
        yield line.strip().split("\t", 1)


def category_reducer():
    v_types = set()
    data = read_map_output(sys.stdin)
    for line in data:
        parts = line.strip().split("\t")
        v_types.add(parts[1].strip())

    for v_type in v_types:
        for category, vnc in data:
            video_id = vnc[0:-2]
            country_count = set()
            video_count = set()
            if v_type == category:
                country_count.add(vnc)
                video_count.add(video_id)
            result = round((float(len(country_count)) / float(len(video_count))), 1)
            print("{}\t:{}".format(v_type, result))


if __name__ == "__main__":
    category_reducer()