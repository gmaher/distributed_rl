#!/bin/bash

py3 run.py -env ./input_files/environment/frozen_lake.json\
 -agent ./input_files/agent/thompson_tabular_q.json

py3 run.py -env ./input_files/environment/frozen_lake.json\
 -agent ./input_files/agent/tabular_q.json

py3 run.py -env ./input_files/environment/frozen_lake.json\
 -agent ./input_files/agent/thompson_tabular_q.json --n_agents 10

py3 run.py -env ./input_files/environment/frozen_lake.json\
 -agent ./input_files/agent/tabular_q.json --n_agents 10

#Nchain
py3 run.py -env ./input_files/environment/nchain.json\
 -agent ./input_files/agent/thompson_tabular_q.json

py3 run.py -env ./input_files/environment/nchain.json\
  -agent ./input_files/agent/tabular_q.json

py3 run.py -env ./input_files/environment/nchain.json\
 -agent ./input_files/agent/thompson_tabular_q.json --n_agents 10

py3 run.py -env ./input_files/environment/nchain.json\
 -agent ./input_files/agent/tabular_q.json --n_agents 10
