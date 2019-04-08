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
    
## System description

### Idea

The basic idea is to search for different 'types of days' in a backtesting trading period, and relate this 'type' with the behaviour of last part of that trading day. 

All trading data is first splitted into days, and to allow flexibility each day is further split into a given time interval.

A clustering algorithm is executed and all of these days (intervals) are grouped based on their similarity.

Is there a relation between each cluster composition and last part of that day (interval) behaviour?

## Pipeline

System pipeline is summarized in this image:

![image](https://github.com/philipiv/forex-machine-learning/blob/master/imgs/pipeline.png)

Lets see this pipeline a little closer with some examples. The data showed in the following Figures belongs to EUR/USD asking price at close for January 4th, 2010. 

At the beginning some parameters are seted. The backtesting period, the time interval to be considered, the number of clusters of kmeans algorithm, etc.

The algorithm only considers an specific interval of each trading day, lets say the 9-17 hs interval.

![image](https://github.com/philipiv/forex-machine-learning/blob/master/imgs/all_day_prices_with_interval_selection.png)

Each of these intervals are splitted into two subintervals, one (with larger lenght) is used to feed the clustering algorithm and the other one (shorter than the former) is used to calculate a label. For example: 9-15 hs is used for clustering and 15-17 hs for labelling.

![image](https://github.com/philipiv/forex-machine-learning/blob/master/imgs/train_label_split.png)

All the larger intervals are used for training a kmeans algorithm. All day intervals from backtesting period are then grouped into _n_ different clusters.

The label is calculated as the substraction between the subinterval's last and first element. This way we answer the question: what would happen if I would buy at the beginning of that time subinterval and I would sell at the end of it?

At last, a measure of 'performance' is calculated for each cluster. Performance is calculated as the sum of all labels of intervals belonging to that particular cluster.



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

