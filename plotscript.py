import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# based on CAD and measurements
mmHeightLaserAboveInductive = 62.738
mmLaserInFrontOfInductive = 100.84

# data from OD value calibration run 3 linear fit, applying 13.17V
def convertmALaser(mA):
    return (mA - 20.037)/(-0.6070)

# data from excel sheet, matlab best fit function using polyfit, degree 5
def convertVoltageInductive(V):
    return 0.0028*V**5 - 0.0796*V**4 + 0.8442*V**3 - 4.0087*V**2 + 10.6857*V + 0.8484

fig = plt.figure()
ax1 = fig.add_subplot(211)
plt.ylabel("Normalized sensor reading (mm)")
ax2 = fig.add_subplot(212)
ax1.set_title("Incoming data stream")
ax2.set_title("Deposit thickness")
plt.xlabel("Distance traveled (mm)")
plt.ylabel("Thickness (mm)")

def animate(i):
    laserData = open("laserdata.txt","r").read()
    inductiveData = open("inductivedata.txt","r").read()
    laserArray = laserData.split('\n')
    inductiveArray = inductiveData.split('\n')
    laserX = []
    laserY = []
    inductiveX = []
    inductiveY = []
    deltaX = []
    deltaY = []
    for line in laserArray:
        if len(line) > 1:
            x, y = line.split(',')
            laserX.append(float(x))
            laserY.append(convertmALaser(float(y)) - mmHeightLaserAboveInductive)
    for line in inductiveArray:
        if len(line) > 1:
            x,y = line.split(',')
            inductiveX.append(float(x))
            inductiveY.append(convertVoltageInductive(float(y)))
    ax1.clear()
    ax1.plot(laserX,laserY)
    ax1.plot(inductiveX,inductiveY)
    ax1.legend(['laser data', 'inductive data'], loc='upper left')
    laserMap = dict(zip(laserX, laserY))
    for i in range(len(inductiveX)):
        x, y = inductiveX[i], inductiveY[i]
        laserXPos = x + mmLaserInFrontOfInductive
        if laserXPos in laserMap:
            laserYPos = laserMap[laserXPos]
            deltaX.append(laserXPos)
            deltaY.append(y - laserYPos)
    ax2.clear()
    ax2.plot(deltaX,deltaY)
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()