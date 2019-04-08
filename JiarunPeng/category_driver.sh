#!/bin/bash

hadoop jar /usr/lib/hadoop/hadoop-streaming-2.8.5-amzn-2.jar \
-D mapreduce.job.name='COMP5349_assignment1' \
-file practice_mapper.py \
-mapper "practice_mapper.py" \
-file practice_reducer.py \
-reducer "practice_reducer.py" \
-input $1 \
-output $2

