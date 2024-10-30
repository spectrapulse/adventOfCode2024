#!/usr/bin/env sh

echo "Today I'll be suffering with:"

sleep 1
echo "."
sleep 1
echo ".."
sleep 1
echo "..."
sleep 1

choice=$(shuf -n 1 language_list.txt)
echo $choice
sed -i "/^$choice$/d" language_list.txt
