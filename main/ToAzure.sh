#!/bin/bash
az vm start --name MyVm --resource-group MyResourceGroup
ssh kn1ms@137.135.241.56 python3 CGProject/GenerateNumber.py
az vm deallocate --resource-group MyResourceGroup --name MyVm