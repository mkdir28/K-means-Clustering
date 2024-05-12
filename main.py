import random
from math import sqrt

#mesure the distance between 1 point and k clusters
def euclidean_distance(oberv1, observ2):
    distance = 0.0
    #last column in each observation is a label
    for i in range(len(oberv1)-1):
        distance += (float(oberv1[i]) - float(observ2[i]))**2
    return sqrt(distance)

#assign point to the nearest cluster
def assign_centroid_to_nearest_cluster(k, dataset):
    assign = []
    for points in dataset:
        shortest_distance = ()
        shortest_index = 0
        for i in range(len(k)):
            point = euclidean_distance(points, k[i])
            if point < shortest_distance:
                shortest_distance = point
                shortest_index = i
            assign.append(shortest_index)
        return assign



#select randomly k distinct data point
# def select_random_k_centroid(k, dataset):
#     random = [random]
#     centroid = []

#the purity of each cluster
def purity(label, k):


#calculate the mean of each cluster m- measure
# def stop_point(previous_centroid, centroid, iteration):
#     if iteration > MAX_ITERATIONS: return True
#     return previous_centroid == centroid


def k_means(k, dataset):
    clusters = [[] for _ in range(k)]


def main():
    with open('iris_kmeans.txt', 'r') as file:
        file_data = [read.split(", ") for read in file]
        dataset = [[float[point] for point in observation[:-1]] for observation in file_data]
    k = int(input("Write a key number of clusters: "))

    k_means(k, dataset)

main()