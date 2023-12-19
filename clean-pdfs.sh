#!/usr/bin/env bash

CWD=$(pwd)
PDF_DIR="$CWD/media/general-flyers"
EXIF_LOC="$HOME/Downloads/Image-ExifTool-12.70/exiftool"
QPDF_LOC="$HOME/Downloads/qpdf/build/qpdf/qpdf"

$EXIF_LOC -all:all $PDF_DIR/*.pdf

# General Flier - Native - Nepali - MMDDYYYY.pdf
for flyer in $PDF_DIR/General*.pdf ; do
    IFS='-' read -ra flyer_elmts <<< "$flyer"

    COUNTER=0
    DATE="MM-DD-YYYY"
    TRANSLATOR="GT"
    LANG="English"
    for i in "${flyer_elmts[@]}"
    do
        if [[ "$COUNTER" -eq 3 ]]; then
            TRANSLATOR=$(echo $i | sed 's/ //g' | awk '{print tolower($0)}')
            
        elif [[ "$COUNTER" -eq 4 ]]; then
            LANG=$(echo $i | sed 's/ //g' | awk '{print tolower($0)}')
            
        elif [[ "$COUNTER" -eq 5 ]]; then
            VAR=$(echo $i | sed 's/ //g')

            MM=$(echo ${VAR:0:2})
            DD=$(echo ${VAR:2:2})
            YYYY=$(echo ${VAR:4:4})
            
            DATE="$MM-$DD-$YYYY"
        fi
        let COUNTER=COUNTER+1
    done

    OUTFILE="$PDF_DIR/general-flyer-$DATE-$TRANSLATOR-$LANG.pdf"
    echo "$OUTFILE"

    $QPDF_LOC --linearize "$flyer" "$OUTFILE"

    RET=$?

    if [ $RET -eq 0 ]; then
        rm "$flyer"
    else
        echo "ERROR = $RET"
    fi

done

