#!/bin/bash

if [ $# -ne 2 ]; then
echo "Invalid number of parameters!"
echo "Usage: ./tag_driver_combiner.sh [input_location] [output_location]"
exit 1
fi

hadoop jar /usr/lib/hadoop/hadoop-streaming-2.8.5-amzn-1.jar \
-D mapreduce.job.reduces=3 \
-D mapreduce.job.name='COMP5349_assignment1' \
-file practice_mapper.py \
-mapper practice_mapper.py \
-file practice_reducer.py \
-reducer practice_reducer.py \
-input $1 \
-output $2