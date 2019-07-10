import argparse

from util import *


##################################################################################
##### parse script parameters ####################################################
##################################################################################

parser = argparse.ArgumentParser(description='Unsupervised learning approach to Forex trading analysis')
parser.add_argument('--date_init', nargs='?', help='backtesting initial date', default='2010-01-01')
parser.add_argument('--date_end', nargs='?', help='backtesting end date', default='2018-01-01')
parser.add_argument('--h_init', nargs='?', help='time interval intial hour', default=9)
parser.add_argument('--h_end', nargs='?', help='time interval final hour', default=17)
parser.add_argument('--h_split', nargs='?', help='interval splitting parameter', default=0.8)
parser.add_argument('--n_clusters', nargs='?', help='number of clusters in clustering algorithm', default=6)
parser.add_argument('--hists', nargs='?', help='boolean plot performance distribution histogram', default="F")

args = parser.parse_args()

date_init = args.date_init
date_end = args.date_end
h_init = int(args.h_init)
h_end = int(args.h_end)
h_split = float(args.h_split)
n_clusters = int(args.n_clusters)
hists = args.hists in ["T", "t", "true", "True", "1"]

# data

data = load_all_data()

# intervals

time_interval = [h_init, h_end]

intervals = get_intervals(date_init, date_end, time_interval)

# data to intervals

data_intervals = data_to_intervals(data, intervals)

# split intervals

train_intervals, label_intervals = split_intervals(data_intervals, h_split)

# normalize train data

normalized_train_intervals = normalize_intervals(train_intervals)

# cluster data

cluster_indexes = get_cluster_indexes(normalized_train_intervals, n_clusters)

# labels

labels = get_labels(label_intervals)

# performances

performances_by_cluster, labels_by_cluster = get_performance(cluster_indexes, labels)

for j, performance in enumerate(performances_by_cluster):
    print ('Performance Cluster #', j, performance)
    plot_hist(labels_by_cluster[j], hists, 'Cluster #' + str(j) + ' performance distribution')

if hists:
    plt.show()
