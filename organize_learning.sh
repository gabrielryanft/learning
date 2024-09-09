#use index of tree
#pode fazer finc recursiva
#!/bin/bash

organize () {
	ls | grep -v -e "README.md" -e "LICENSE" -e "organize_learning.sh" -e "exists.txt" > exists.txt
	printf "$(basename $PWD) \n" > README.md
	while read name
	do 
		if [ $(file -b $name) = "directory" ]; then
			printf "<a href='$1/$name/' target='_blank' rel='next'>$name</a><br/>\n" >> README.md
			cd $name
			organize "$1/$name" "$2"
		fi
	done < exists.txt
}
organize "https://gabrielryanft.github.io/learning" "$(pwd)"
