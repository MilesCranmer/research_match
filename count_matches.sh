#!/bin/bash

# This command removes spaces in the names and replaces them with underscores
Z=$(for x in $1/*\ *; do mv "$x" "${x// /_}"; done 2>/dev/null)

# This shows the columns of our table
echo "name, GPU, ML, Bayesian, Monte Carlo, python, C++, dark matter, dark energy, surveys, lss, galaxy formation, statistics, pulsars, PCA"
for x in $(ls -tr $1); do
    # This both searches for GPU in the $1, and prints the person's name
    grep -c -e "\<GPU\>" $1/$x | echo -n "$x, $(cat -), "
    # This command searches for synonyms of machine learning
    grep -c -i -e "neural network" -e "machine\-learning" -e "random forest" -e "machine learning" -e "supervised learning" -e "reinforcement learning" -e "support vector machine" -e "naive bayes" -e "knn" -e "k nearest neighbors" $1/$x | echo -n "$(cat -), "
    grep -c -i "bayes" $1/$x | echo -n "$(cat -), "
    grep -c -e "MCMC" -e "Monte Carlo" $1/$x | echo -n "$(cat -), "
    # The "-i" flag here makes it case insensitive
    grep -c -i "python" $1/$x | echo -n "$(cat -), "
    grep -c -i "C++" $1/$x | echo -n "$(cat -), "
    grep -c -i -e "dark matter" $1/$x | echo -n "$(cat -), "
    grep -c -i -e "dark energy" $1/$x | echo -n "$(cat -), "
    grep -c -i -e "survey" $1/$x | echo -n "$(cat -),"
    grep -c -i -e "lss " -e "large scale structure" $1/$x | echo -n "$(cat -), "
    grep -c -i -e "galaxy formation" $1/$x | echo -n "$(cat -), "
    grep -c -i -e "statistics" $1/$x | echo -n "$(cat -), "
    grep -c -i -e "pulsar" $1/$x | echo -n "$(cat -), "
    grep -c -i -e "pca" -e "principal component analysis" $1/$x | echo -n "$(cat -)"
    # This final echo adds the newline
    echo ""
done
