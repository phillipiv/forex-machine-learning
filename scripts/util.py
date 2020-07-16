import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def load_all_data():
    """Loads the data!"""
    return pd.read_pickle('../data/EURUSD-2010_2018-closeAsk.pkl')


def split_intervals(data_intervals, h_split):
    """
    Receives a list of intervals and a split coefficient and returns two lists, each one containing a subinterval
    of input.
    :param data_intervals: List of time series.
    :param h_split: Split coefficient. (float in (0, 1))
    :return:
        - output_train: List of time series, each element in the list is made of a data_interval element,
                        from the indexes 0 to int(len(input) * h_split).
        - output_label: List of time series, each element in the list is made of a data_interval element,
                        each element in the list is from the indexes int(len(input) * h_split) to len(input).
    """
    output_train = []
    output_label = []

    interval_length = np.shape(data_intervals[0])[0]
    split_idx = int(h_split * interval_length)

    for j, data_interval in enumerate(data_intervals):
        output_train.append(data_interval[:split_idx])
        output_label.append(data_interval[split_idx:])

    return output_train, output_label


def get_performance(cluster_indexes, labels):
    """
    Iterates in all clusters and prints the performance for each one of them.
    Each cluster performance is calculated as the sum of its elements' performances.
    :param cluster_indexes: List with cluster indexes for all elements.
    :param labels: List with performances for all elements.
    :return:
        - output_performance: List with the performance (sum of labels) of each cluster.
        - output_labels: List with the list of labels for each cluster.
    """

    clusters = np.sort(np.unique(cluster_indexes))

    output_performance = []
    output_labels = []

    for c in clusters:
        indxs = np.where(cluster_indexes == c)[0]
        labels_ = np.asarray(labels)[indxs]
        output_labels.append(labels_)
        output_performance.append(np.sum(labels_))

    return output_performance, output_labels


def plot_hist(data, hists, title):
    """If 'hists' is True, plots an histogram for each cluster performance."""

    if hists:
        fig = plt.figure()
        plt.hist(data, bins=30)
        plt.grid()
        plt.title(title)


def normalize_intervals(train_intervals):
    """
    Normalize the time series in a given list.
    :param train_intervals: List of time series.
    :return: The same list of time series, with each element ranging between 1 and -1.
    """

    output = []

    for train in train_intervals:
        temp = train - np.mean(train)
        temp = temp / (np.amax(temp) - np.amin(temp))
        output.append(temp)

    return output


def get_cluster_indexes(normalized_train_intervals, n_clusters):
    """Executes a Kmeans algorithm on input data and returns a list with what cluster each element belongs to."""

    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(normalized_train_intervals)

    return kmeans.labels_


def get_labels(label_intervals):
    """
    Calculates each interval performance.
    :param label_intervals: List of time series.
    :return:
        - labels: The performance related to each element in the input, calculated as the subtraction between its
                  last and first element.
    """

    labels = []
    for data_ in label_intervals:
        labels.append(data_[-1] - data_[0])

    return labels


def get_intervals(date_init, date_end, interval):

    """
    Returns a list of time intervals.
    :param date_init: Initial date. (For example: 2010-01-01)
    :param date_end: End date. (For example: 2018-01-01)
    :param interval: List of two integers, the limits of each day being considered. (For example: [6, 15])
    :return:
        - output: List of time intervals.
                  Each element is a different day, restricted to the hours as specified in 'interval'.
    """

    h_init, h_end = interval

    output = []
    rango_total = pd.date_range(date_init, date_end, freq='D')

    for i in rango_total:
        _ = pd.date_range(i, periods=1440, freq='T')
        output.append(_[h_init * 60:h_end * 60])

    return output


def data_to_intervals(data, intervals):
    """
    Split input data into a list of intervals. Each interval is a range of datetimes.
    :param data: Time series.
    :param intervals: List of datetimes time series.
    :return: A list where each element is input data restricted to a time interval defined by elements in 'intervals'.
    """

    interval_length = np.shape(intervals[0])[0]

    output = []

    for j, interval in enumerate(intervals):

        data_ = data[interval]

        if (not(np.isnan(data_).any())) and (np.shape(data_)[0] == interval_length):
            output.append(data_)

    return output
