import csv
import math
import operator
import random


class KNN:
    # Read the data and create both training set and test set
    def load_Dataset(self, filename, split, test_set, training_set):
        with open('iris.data','r') as data:
            lines = csv.reader(data)
            # print(list(lines))
            dataset = list(lines)
            for i in range(len(dataset)-1):
                if random.random() < split:
                    training_set.append(dataset[i])
                else:
                    test_set.append(dataset[i])

    # We are using the Euclidean Distance method to calculate the distance between two instances
    def euclideanDistance(self, new_instance, instance, length):
        distance = 0
        for x in range(length):
            distance += math.sqrt(pow((new_instance[x] - instance[x]), 2))
        return distance

    def getNeighbors(self, trainingSet, testInstance, k):
        distances = []
        length = len(testInstance) - 1
        for y in range(len(trainingSet)):
            dist = self.euclideanDistance(testInstance, trainingSet[y], length)
            distances.append((trainingSet[y], dist))
        distances.sort(key = operator.itemgetter(1))
        neighbors = []
        for z in range(k):
            neighbors.append(distances[z][0])
        return neighbors

    def vote(self, neighbors):
        Votes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-1]
            if response in Votes:
                Votes[response] += 1
            else:
                Votes[response] = 1
        sorted_Votes = sorted(Votes, key=operator.itemgetter(1), reverse=True)
        return sorted_Votes[0][0]


