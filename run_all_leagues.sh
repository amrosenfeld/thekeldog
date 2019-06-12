#!/bin/bash

for f in ./input_files/*;
do
    echo "New Test $f"
    echo "argument"
    python3 league_builder.py $f
    echo "stdin"
    python3 league_builder.py < $f
done

pip install pytest
pytest


