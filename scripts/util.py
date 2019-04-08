import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_all_data():

    return pd.read_pickle('../data/EURUSD-2010_2018-closeAsk.pkl')

def split_intervals(data_intervals,h_split):

    output_train = []
    output_label = []

    interval_length = np.shape(data_intervals[0])[0]
    split_idx=int(h_split*interval_length)

    for j,data_interval in enumerate(data_intervals):
        output_train.append(data_interval[:split_idx])
        output_label.append(data_interval[split_idx:])

    return output_train,output_label

def get_performance(cluster_indexes,labels):

    clusters=np.sort(np.unique(cluster_indexes))

    output_performance=[]
    output_labels = []

    for c in clusters:
        indxs=np.where(cluster_indexes==c)[0]
        labels_=np.asarray(labels)[indxs]
        output_labels.append(labels_)
        output_performance.append(np.sum(labels_))

    return output_performance,output_labels

def plot_hist(data,hists,title):

    if (hists):
        fig = plt.figure()
        plt.hist(data,bins=30)
        plt.grid()
        plt.title(title)

def normalize_intervals(train_intervals):

    output = []

    for train in train_intervals:
        temp = train - np.mean(train)
        temp = temp / (np.amax(temp) - np.amin(temp))
        output.append(temp)

    return output

def get_cluster_indexes(normalized_train_intervals,n_clusters):

    from sklearn.cluster import KMeans

    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(normalized_train_intervals)

    return kmeans.labels_

def get_labels(label_intervals):

    labels=[]

    for data_ in label_intervals:

        labels.append(data_[-1]-data_[0])

    return labels


def get_intervals(date_init,date_end,interval):

    h_init,h_end=interval

    output = []
    rango_total = pd.date_range(date_init, date_end, freq='D')
    for i in rango_total:
        _=pd.date_range(i,periods=1440, freq='T')
        output.append(_[h_init*60:h_end*60])

    return output


def data_to_intervals(data, intervals):

    interval_length=np.shape(intervals[0])[0]

    output=[]

    for j, interval in enumerate(intervals):

        data_ = data[interval]

        if (not(np.isnan(data_).any())) and (np.shape(data_)[0]==interval_length):
            output.append(data_)

    return output
