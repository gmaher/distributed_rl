#!/bin/bash

python main_thread.py -input ./input_files/epsilon_greedy/frozenlake_standard_1.json
python main_thread.py -input ./input_files/epsilon_greedy/frozenlake_standard_10.json
python main_thread.py -input ./input_files/epsilon_greedy/frozenlake_uniform_1.json
python main_thread.py -input ./input_files/epsilon_greedy/frozenlake_uniform_10.json

python main_thread.py -input ./input_files/epsilon_greedy/nchain_standard_1.json
python main_thread.py -input ./input_files/epsilon_greedy/nchain_standard_10.json
python main_thread.py -input ./input_files/epsilon_greedy/nchain_uniform_1.json
python main_thread.py -input ./input_files/epsilon_greedy/nchain_uniform_10.json

python main_thread.py -input ./input_files/thompson/frozenlake_standard_1.json
python main_thread.py -input ./input_files/thompson/frozenlake_standard_10.json
python main_thread.py -input ./input_files/thompson/frozenlake_uniform_1.json
python main_thread.py -input ./input_files/thompson/frozenlake_uniform_10.json

python main_thread.py -input ./input_files/thompson/nchain_standard_1.json
python main_thread.py -input ./input_files/thompson/nchain_standard_10.json
python main_thread.py -input ./input_files/thompson/nchain_uniform_1.json
python main_thread.py -input ./input_files/thompson/nchain_uniform_10.json
