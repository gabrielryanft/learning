#!/bin/bash
# Script created with the intention of organizing
# the files and dirs by linking them in my README.md files
# In a file explorer like strucrtre

# cleaning

echo something
pwd
ls
# clean () {
# 	str="$(ls $1)"
# 	while read name
# 	do
# 		if [ "$name" != "" ]; then
# 			if [ -d "$1/$name" ]; then
# 				rm "$1/$name/exists.txt" 2> /dev/null
# 				clean "$1/$name"
# 			fi
# 		fi
# 	done <<< "$str"
# }
#
# # Making
# organize () {
# 	ls --ignore={"README.md","LICENSE","organize_learning.sh"} "$2" > "$2/exists.txt"
# 	sed -i '/exists.txt/d' "$2/exists.txt"
# 	printf "# $(basename $2) \n" > "$2/README.md"
# 	while read -r name
# 	do
# 		if [ "$(file -b "$2/$name")" = "directory" ]; then
# 			printf "<a href='$1/$name/' target='_blank' rel='next'>$name</a><br/>\n" >> "$2/README.md"
# 			organize "$1/$name" "$2/$name"
# 		else
# 			printf "<a href='$1/$name' target='_blank' rel='next'>$name</a><br/>\n" >> "$2/README.md"
# 		fi
# 	done < "$2/exists.txt"
# }
# organize "https://gabrielryanft.github.io/learning" "$(pwd)"
#
# rm "$(pwd)/exists.txt" 2> /dev/null
# clean "$(pwd)"
