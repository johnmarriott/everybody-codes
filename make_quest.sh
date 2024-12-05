#!/bin/zsh

# assume running in a year directory

if [[ $# == 0 ]] 
then
  quest=$( date +%d )
else
  quest=$( printf "%02d" $1 )
fi

mkdir "quest$quest"
cd "quest$quest"
touch input.txt
touch sample.txt
echo "#!/usr/bin/env python\n\nimport fileinput\n\nlines = [line.strip() for line in fileinput.input()]" > 1.py
