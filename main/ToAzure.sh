#!/bin/bash
az vm start --name MyVm --resource-group MyResourceGroup
sleep 60s
ssh kn1ms@13.94.101.35 python3 CGProject/GenerateNumber.py
az vm deallocate --resource-group MyResourceGroup --name MyVm