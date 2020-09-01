#!/bin/bash
>oldFiles.txt

files=$(grep ' jane ' ../data/list.txt | cut -d' ' -f3 |cut -d'/' -f3)

for file in $files;do
        if test -e ~/data/$file;then
                echo ~/data/$file>>oldFiles.txt
        else echo "File not found"
        fi
done
