#!/bin/bash
# arg1: input file
# arg2: output directory

input_file=${1}
input_directory=${2}
output_directory=${3}
mq_write=${4}

echo '#'
echo '#  Starting Process: '
echo '#'

python3 split.py "${input_file}" "${input_directory}"

echo '  Done'