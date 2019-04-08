# Unsupervised learning approach to Forex trading analysis  

Implementation of an unsupervised learning algorithm to analyse forex signals and support trading strategies. 

## Getting Started

### Clone repository

    ~ $ git clone https://github.com/philipiv/forex-machine-learning.git
    ~ $ cd forex-machine-learning

### Project requirements 

It is strongly advised you work in a virtual environment.\
First step is to create one and install all necessary project requirements.
       
    ~/forex-machine-learning $ virtualenv env --python=python3
    ~/forex-machine-learning $ source env/bin/activate
    ~/forex-machine-learning $ pip install -r requirements.txt

## Execution

    ~/forex-machine-learning $ cd scripts
    ~/forex-machine-learning $ python main.py [--file /path/to/file]

Optionaly, you can set the path to a file containing your data, default path is _../data/sample.csv_.

For example:

    ~/forex-machine-learning $ python strategy.py --file ../data/sample.csv

## Results

After execution, the script output is a Figure containing original signal and output to all filters.

When executed with the sample data the output looks like this:

![image](https://github.com/philipiv/rssi-filtering-kalman-grey-fourier-particles-bellavista2006/blob/master/sample_output.png)

