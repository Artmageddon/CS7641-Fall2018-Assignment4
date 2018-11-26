# CS7641 Assignment 4
# Arthur Baczyk

GitHub Link: https://github.com/Artmageddon/CS7641-Fall2018-Assignment4

This package should contain all code and data necessary to run all of the expierments for assignment 4.

## Installation

1. Install Conda, a CLI tool

   https://conda.io/docs/user-guide/install/index.html

2. Use Conda to install all dependencies through `environment.yml`

```
    conda env create -f environment.yml
```

3. Activate the environment created by conda

```
    source activate cs-7641
```

4. You're set, read the next sections in order to be able to run any of the experiments.

## Run

```
$ python main.py --help
usage: main.py [-h] [-p {taxi,frozen-lake}]
               [-a {value-iteration,policy-iteration,q-learning}]

optional arguments:
  -h, --help            show this help message and exit
  -p {taxi,frozen-lake}, --problem {taxi,frozen-lake}
                        Problem to solve
  -a {value-iteration,policy-iteration,q-learning}, --algorithm {value-iteration,policy-iteration,q-learning}
                        RL algorithm to use
(cs-7641)
```

## Example

To solve the Taxi MDP with value iteration, try the following command.

```
python main.py -p taxi -a value-iteration
```
