#!/bin/bash

mkdir datasets
cd datasets
wget http://files.grouplens.org/datasets/movielens/ml-latest-small.zip
unzip ml-latest-small.zip
rm ml-latest-small.zip