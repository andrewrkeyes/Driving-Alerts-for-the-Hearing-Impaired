
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

def fp():
    window_size = 300


    sensor_one = open("sensor_one.txt").readlines()
    sensor_two = open("sensor_two.txt").readlines()
    sensor_three = open("sensor_three.txt").readlines()

    X_train = list()

    for x in range(window_size, file_lines(sensor_one)):
        window = np.zeros((3,window_size))
        for y in range(x, x+window_size):
            window[0, y] = int(sensor_one[y])
            window[1, y] = int(sensor_two[y])
            window[2, y] = int(sensor_three[y])
        X_train.append(window)




def main():
    f = open("output.txt")
    s0 = open("sens0", "a")
    s1 = open("sens1", "a")
    s2 = open("sens2", "a")

    for line in f:
        if line.strip() != "":
            info = line.split(":")
            sensor = info[0]
            time = info[1]
            noise = info[2]

            if sensor == "0":
                s0.write(str(noise))
            if sensor == "1":
                s1.write(str(noise))
            if sensor == "2":
                s2.write(str(noise))


main()