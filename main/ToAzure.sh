#!/bin/bash
az vm start --name MyVm --resource-group MyResourceGroup
ssh azureuser@137.135.241.56 python3 RandomNumberGenerator/GenerateNumber.py
az vm deallocate --resource-group MyResourceGroup --name MyVm