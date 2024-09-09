#use index of tree
#pode fazer finc recursiva
#!/bin/bash

organize () {
	ls "$2" | grep -v -e "README.md" -e "LICENSE" -e "organize_learning.sh" -e "exists.txt" > "$2/exists.txt"
	echo 1 $1
	echo 2 $2
	printf "$(basename $PWD) \n" > "$2/README.md"
	while read name
	do 
		printf "<a href='$1/$name/' target='_blank' rel='next'>$name</a><br/>\n" >> "$2/README.md"
		if [ "$(file -b $name)" = "directory" ]; then
			organize "$1/$name" "$2/$name"
		fi
	done < "$2/exists.txt"
}
organize "https://gabrielryanft.github.io/learning" "$(pwd)"

