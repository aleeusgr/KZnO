#!bin/python

# new functionality:
# train_x, train_y function calls
# watch modules in python!!!
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd

def show_train_x_graphs():

    oil = pd.read_csv('oil.csv')
    rub = pd.read_csv('rub.csv')

    plt.figure(figsize=(10,5))
    plt.plot(oil['Close'],label='Crude Oil')
    plt.plot(rub['Close'],label='USD/RUB')
    plt.legend()
    plt.show()

#print(search)
