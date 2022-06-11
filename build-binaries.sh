#!/bin/bash
pip install pyinstaller
pyinstaller -F --onefile zxc.py
cd dist
cp zxc ..
cd ..
rm -rf zxc.spec dist build
clear
echo "Готово!"

