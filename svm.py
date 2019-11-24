
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
    X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2)

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

    print(svclassifier.score(X_test, y_test))

def file_lines(f):
    count = 0
    for line in f:
        count += 1

    return count

def fp():
    window_size = 300
    sensor_one = open("sensor_one0.txt").readlines()
    sensor_two = open("sensor_two0.txt").readlines()
    sensor_three = open("sensor_three0.txt").readlines()

    X_train = list()
    y_train = list()

    for x in range(window_size, file_lines(sensor_one)-window_size):
        window = np.zeros((3,window_size))
        for y in range(x, x+window_size-1):
            window[0, y] = float(sensor_one[y])
            window[1, y] = float(sensor_two[y])
            window[2, y] = float(sensor_three[y])
        X_train.append(window)
        y_train.append(0)

    sensor_one = open("sensor_one1.txt").readlines()
    sensor_two = open("sensor_two1.txt").readlines()
    sensor_three = open("sensor_three1.txt").readlines()

    for x in range(window_size, file_lines(sensor_one)-window_size):
        window = np.zeros((3,window_size))
        for y in range(x, x+window_size-1):
            window[0, y] = float(sensor_one[y])
            window[1, y] = float(sensor_two[y])
            window[2, y] = float(sensor_three[y])
        X_train.append(window)
        y_train.append(1)

    train(X_train, y_train)





def main():
    for trial in range(0,2):
        s0 = open("sensor_one"+str(trial)+".txt", "a")
        s1 = open("sensor_two"+str(trial)+".txt", "a")
        s2 = open("sensor_three"+str(trial)+".txt", "a")
        for x in range(0, 30):
            file_name =  str(trial) + "/" + str(trial) + "_" + str(x) + ".txt"
            f = open(file_name)
            for line in f:
                line = line.rstrip()
                line = line.strip("b")
                line = line.strip("'")
                line = line.rstrip()
                print(line)
                if line.strip() != "":
                    info = line.split(":")
                    sensor = info[0]
                    time = info[1]
                    noise = info[2].split("\\")[0]

                    if sensor == "0":
                        s0.write(str(noise)+"\n")
                    if sensor == "1":
                        s1.write(str(noise)+"\n")
                    if sensor == "2":
                        s2.write(str(noise)+"\n")
        s0.flush()
        s1.flush()
        s2.flush()


fp()