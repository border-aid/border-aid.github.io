#!/usr/bin/env bash

CWD=$(pwd)
MEDIA_DIR="$CWD/media"
PDF_DIR="$CWD/media/general-flyers"
EXIF_LOC="$HOME/Downloads/Image-ExifTool-12.70/exiftool"
QPDF_LOC="$HOME/Downloads/qpdf/build/qpdf/qpdf"



qpdf_linearize_new_pdfs() {
# format: General Flier - Native - Nepali - MMDDYYYY.pdf
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

    OUTFILE="$PDF_DIR/jacumba-flyer-$DATE-$TRANSLATOR-$LANG.pdf"
    echo "$OUTFILE"

    $QPDF_LOC --linearize "$flyer" "$OUTFILE"
    RET=$?
    if [ $RET -eq 0 ]; then
        rm "$flyer"
    else
        echo "ERROR = $RET"
    fi
done
}



qpdf_linearize_extant_pdfs() {
    for flyer in $PDF_DIR/*-flyer-*.pdf ; do

        $QPDF_LOC --linearize "$flyer" --replace-input
        RET=$?

        if [ $RET -ne 0 ]; then
            echo "ERROR = $RET"
        fi

    done

    for flyer in $MEDIA_DIR/*.pdf ; do

        $QPDF_LOC --linearize "$flyer" --replace-input
        RET=$?

        if [ $RET -ne 0 ]; then
            echo "ERROR = $RET"
        fi

    done
}

#pdfseparate ./media/general-flyers/W8\ Flier\ -\ 10\ languages.pdf %d.pdf

$EXIF_LOC -all:all= $PDF_DIR/*.pdf
RET=$?
if [ $RET -eq 0 ]; then
    rm $PDF_DIR/*.pdf_original
fi

$EXIF_LOC -all:all= $MEDIA_DIR/*.pdf
RET=$?
if [ $RET -eq 0 ]; then
    rm $MEDIA_DIR/*.pdf_original
fi

#qpdf_linearize_new_pdfs
qpdf_linearize_extant_pdfs