#!/bin/sh

python executor.py --total -1 --config config_gender.yaml --datahandler data_handler

python executor.py --total -1 --config config_religion.yaml --datahandler data_handler

python executor.py --total -1 --config config_ebe_gender.yaml --datahandler ebe

python executor.py --total -1 --config config_ebe_religion.yaml --datahandler ebe

python executor.py --total -1 --config config_ibe.yaml --datahandler ibe