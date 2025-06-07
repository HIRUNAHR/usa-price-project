cd ~/hadoop-3.4.1
bin/hdfs dfs -mkdir -p /usaprice
bin/hdfs dfs -put -f ~/usaprice/data/realtordata.csv /usaprice/
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /usaprice/realtordata.csv \
-output /usaprice/output \
-mapper ~/usaprice/scripts/mapper.py \
-reducer ~/usaprice/scripts/reducer.py
bin/hdfs dfs -cat /usaprice/output/part-*


#!/bin/bash

cd ~/hadoop-3.4.1

# Ensure input exists
bin/hdfs dfs -mkdir -p /usaprice
bin/hdfs dfs -put -f ~/usaprice/data/realtordata.csv /usaprice/

# Remove previous output2 directory
bin/hdfs dfs -rm -r -f /usaprice/output2

# Run MapReduce job
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /usaprice/realtordata.csv \
  -output /usaprice/output2 \
  -mapper ~/usaprice/scripts/mapper2.py \
  -reducer ~/usaprice/scripts/reducer2.py \
  -file ~/usaprice/scripts/mapper2.py \
  -file ~/usaprice/scripts/reducer2.py

# View output (optional)
bin/hdfs dfs -cat /usaprice/output2/part-*
