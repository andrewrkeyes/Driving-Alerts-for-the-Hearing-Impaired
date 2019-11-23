
import scipy.io
import os
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import random
import math

def train(X_train, y_train):
    X_train, X_test, y_train, _ = train_test_split(X_train, y_train, test_size=0.2)

    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    pca = PCA(.99)
    pca.fit(X_train)

    X_train = pca.transform(X_train)
    X_test = pca.transform(X_test)
    svclassifier = SVC(kernel='linear')
    svclassifier.fit(X_train, y_train)

    svclassifier.predict(X_test)

def file_lines(f):
    count = 0
    for line in f:
        count += 1

    return count

def main():
    sensor_one = open("sensor_one.txt")
    sensor_two = open("sensor_two.txt")
    sensor_three = open("sensor_three.txt")

    X_train = list()

    for x in range(300, file_lines(sensor_one)):
        window = np.zeros((3,200))
        for y in range(x, x+300):
            window[0, y] = int(sensor_one.readline())
            window[1, y] = int(sensor_two.readline())
            window[2, y] = int(sensor_three.readline())
        X_train.append(window)

    




main()