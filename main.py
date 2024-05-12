import random
from math import sqrt


def euclidean_distance(oberv1, observ2):
    distance = 0.0
    #last column in each observation is a label
    for i in range(len(oberv1)-1):
        distance += (float(oberv1[i]) - float(observ2[i]))**2
    return sqrt(distance)


##select randomly k distinct data point

#mesure the distance between 1 point and k clusters

#assign point to the nearest cluster

#calculate the mean of each cluster m- measure
def main():
    k = input("Write a key number of clusters: ")

if __name__ == "__main__":
    main()