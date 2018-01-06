#!/bin/bash

TEST_INPUT=(
    "0.38813665"
    "0.2"
    "1.6"
)

COUNT=${#TEST_INPUT[@]}

for ((i=0; i<$COUNT; i++)); do
    export POPCLIP_TEXT="${TEST_INPUT[$i]}"
    printf "$POPCLIP_TEXT is: "
    python bitcoin.py
done
