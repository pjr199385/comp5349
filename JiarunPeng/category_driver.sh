#!/bin/bash

hadoop jar /usr/lib/hadoop/hadoop-streaming-2.8.5-amzn-1.jar \
-D mapreduce.job.name='COMP5349_assignment1' \
-file category_mapper.py \
-mapper "category_mapper.py" \
-file category_reducer.py \
-reducer "category_reducer.py" \
-input $1 \
-output $2

