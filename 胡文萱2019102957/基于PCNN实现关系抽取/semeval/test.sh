#!/bin/bash

python convert_to_rel.py
./semeval2010_task8_scorer-v1.2.pl sem_res.txt test_keys.txt > res.txt
echo "the results save in res.txt"
