#!/bin/bash

# activate conda env
source /home/ys/miniconda3/bin/activate langchain

# use target path
cd /mnt/d/Python/Langchain-Chatchat

# start service
python startup.py -a
