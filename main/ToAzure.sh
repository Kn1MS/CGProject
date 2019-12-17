#!/bin/bash
az vm start --name MyVm --resource-group MyResourceGroup
ssh kn1ms@40.127.98.194 python3 CGProject/GenerateNumber.py
az vm deallocate --resource-group MyResourceGroup --name MyVm