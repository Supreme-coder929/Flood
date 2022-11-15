#!/bin/bash

echo 'INSTALLING PYARMOR'
pip3 install pyarmor
echo 'OBFUSCATING SCRIPT'
pyarmor obfuscate main.py
echo 'OBFUSCATION COMPLETE'



