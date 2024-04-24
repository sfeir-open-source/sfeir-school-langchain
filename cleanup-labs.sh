#!/bin/bash

find steps/**/solution.ipynb -type f -exec jupyter nbconvert --clear-output --inplace {} \;
