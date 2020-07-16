# Unsupervised learning approach to Forex trading analysis  

Implementation of an unsupervised learning algorithm to analyse forex signals and support trading strategies. 

## Getting Started

### Clone repository

    ~ $ git clone https://github.com/philipiv/forex-machine-learning.git
    ~ $ cd forex-machine-learning

### Project requirements 

It is strongly advised you work in a virtual environment.\
First step is to create one and install all necessary project requirements.
       
    ~/forex-machine-learning $ virtualenv env --python=python3.6
    ~/forex-machine-learning $ source env/bin/activate
    ~/forex-machine-learning $ pip install -r requirements.txt
    
## System description

### 

All trading data is split into days and each day is then further split into a given time interval. 

A clustering algorithm is executed and all of these days (time intervals) are grouped based on their similarity.

Then, a detailed study is made on each cluster composition to assess its profitability. 

## Pipeline

System pipeline is summarized in this image:

![image](https://github.com/philipiv/forex-machine-learning/blob/master/imgs/system-pipeline.png)

Lets see this pipeline a little closer with some examples. The data showed in the following Figures belongs to EUR/USD asking price at close for January 4th, 2010. 

Some parameters are set when starting the program; backtesting period, time interval to be considered, number of clusters of kmeans algorithm, etc.

The system only considers an specific interval of each trading day, in the following example we are only considering the 9-17 hs interval.

![image](https://github.com/philipiv/forex-machine-learning/blob/master/imgs/all_day_prices_with_interval_selection.png)

Each of these intervals are further split into two subintervals. The first one (usually with larger length) is used to feed the clustering algorithm and the other one is used to calculate a label. For example: 9-15 hs is used for clustering and 15-17 hs for labelling.

![image](https://github.com/philipiv/forex-machine-learning/blob/master/imgs/train_label_split.png)

A kmeans clustering algorithm is fitted using the time series from first group, all sequences are then grouped into _n_ different clusters.

Each of these sequences is labelled as the difference between the first and the last element of its 'labelling subinterval'. 

    labels = []
    for subinterval in labelling_subintervals:

        labels.append(subinterval[-1]-subinterval[0]) 

At last, a measure of 'performance' is calculated for each cluster. Performance is calculated as the sum of all labels of sequences belonging to that particular cluster.

## Data

Some example data can be downloaded [here](https://drive.google.com/drive/folders/1SlIbz-_tprP_ZlnDk_y8SGdDK2Tgynuy?usp=sharing).


## Execution

    ~/forex-machine-learning $ cd scripts
    ~/forex-machine-learning/scripts $ python main.py [args]

Optionaly, you can change the value of a selected set of script parameters:
    
    --date_init     backtesting initial date
    --date_end      backtesting end date
    --h_init        initial hour of selected day intervals
    --h_end         final hour of selected day intervals
    --h_split       percentage of interval destinated to training
    --n_clusters    number of clusters for kmeans algorithm
    --hists         plot cluster histograms
    
If you don't, a value is set by default.

For example:

    ~/forex-machine-learning/scripts $ python main.py --date_init '2010-01-01' --date_end '2016-06-07' --h_init 6 --h_split 0.65 --hists false 

