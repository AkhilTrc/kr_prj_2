# KR - Project 2 - PGMs

## Description

This repo is basic implementations of different methods of a bayesian network reasoner.

Methods Implemented:
* D-Separation
* Ordering 
* Network-pruning
* Marginal distribution (prior and posterior)
* MAP and MPE

## Files and folders included
* root folder: has all the programs with test files.
* testing : have different size bayesian networks we used including the BIFXML file developed out of our use-case (crime_causes.BIFXML).

### Setup
From the root folder: 
```
pip install -r requirements.txt
```
### Dependencies

* Python3 - This program is written using Python

### Executing program

 * Running the test files(file names ending with test) will execute the respective method with the given parameters in the test file.
 * In order to test for d-separation, please run the DSeparation.py file. 
