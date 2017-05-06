# FOR NUCLEAR ROBOTICS
# OBJECTIVES: Plotting sensor data for visualization as mm vs step graph
# MAIN FUNCTION: plot; args: step_size, file1, file2
# step_size <- in mm the size per step of the cart
# file1 <- filename of Inductive Proximity Sensor Testing
# file2 <- filename of Displacement Measurement (laser) Sensor Testing
# ASSUMPTIONS:
# 1. input file will have all voltage values in row[1] (0-indexed)
# 2. file type is csv
# 3. assumption both files have same number of steps
################################################################################

import plotly
from plotly.graph_objs import Scatter, Layout
import csv


def voltage_to_mm(step_size, voltage):
    # coverts analog voltage to mm
    return voltage # MODIFY LATER

def convert(step_size, data):
    # gets data and converts to mm
    a = []
    for i in range(len(data)):
        a.append(voltage_to_mm(step_size, data[i]))
    return a

def read(step_size, filename):
    # reads in file, and stores data in a list
    # looks it up and returns a list
    # of voltages converted to mm 
    data = []
    with open('count100.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row[1])
    return convert(step_size, data)

def plot_lines(sensor1, sensor2):
    # plot both graphs
    step = [i for i in range(len(sensor1))]
    trace0 = Scatter(
        x = step,
        y = sensor1,
        name = "Inductive Sensor",
        line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
    )
    
    trace1 = Scatter(
        x = step,
        y = sensor2,
        name = "Displacement Measurement Sensor",
        line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
    )

    data = [trace0, trace1]

    # Edit the layout
    layout = dict(title = 'Readings from both sensors',
                  xaxis = dict(title = 'Step'),
                  yaxis = dict(title = 'Distance mapped by sensor (in mm)'),
                  )

    fig = dict(data=data, layout=layout)
    # this will plot this locally as an HTML file
    # and automatically open it after it saves
    plotly.offline.iplot(fig, auto_open)

def plot(step_size, file1, file2):
    # read in both files, get their distance in mm
    # and plot both graphs
    sensor1 = read(step_size, file1)
    sensor2 = read(step_size, file2)

    plot_lines(sensor1, sensor2)