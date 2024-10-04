#!/bin/sh

find steps -name solution.ipynb -type f -exec jupyter nbconvert --clear-output --inplace {} \;
find steps -name demo.ipynb -type f -exec jupyter nbconvert --clear-output --inplace {} \;
