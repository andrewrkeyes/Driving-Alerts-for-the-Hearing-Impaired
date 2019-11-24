import serial
import matplotlib
import time
import sys
import pickle

def main():
    window_size = 20

    loaded_svm = pickle.load(open('svm_model.sav', 'rb'))

    ser = serial.Serial('/dev/ttyACM0',9600)

    window = np.zeros(window_size*3)

    counter = 0
    while len(window) <= window_size*3:
        line = ser.readline()
        line = line.rstrip()
        line = line.strip("b")
        line = line.strip("'")
        line = line.rstrip()
        info = line.split(":")

        if info[0] == "0":                 
            window[counter] = info[2].split("\\")[0]
        if info[0] == "1":
            window[counter+window_size] = info[2].split("\\")[0]
        if info[0] == "2": 
            window[counter+(2*window_size)] = info[2].split("\\")[0]

        counter += 1

    
    x = loaded_svm.predict(window)
    newFile = open("Mayasinput.txt", 'w')
    newFile.write(x)
    
main()
