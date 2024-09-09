#!/bin/bash

organize () {
    find "$2" -maxdepth 1 -mindepth 1 -not -name "README.md" -not -name "LICENSE" -not -name "organize_learning.sh" -not -name "exists.txt" -exec basename {} \; > "$2/exists.txt"
    printf "# $(basename $2) \n" > "$2/README.md"
    while read -r name
    do
        if [ "$(file -b "$2/$name")" = "directory" ]; then
        	printf "<a href='$1/$name/' target='_blank' rel='next'>$name</a><br/>\n" >> "$2/README.md"
            organize "$1/$name" "$2/$name"
		else
        	printf "<a href='$1/$name' target='_blank' rel='next'>$name</a><br/>\n" >> "$2/README.md"
        fi
    done < "$2/exists.txt"
}
organize "https://gabrielryanft.github.io/learning" "$(pwd)"

