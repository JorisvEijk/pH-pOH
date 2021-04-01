import math
import matplotlib.pyplot as plt

H_conc = 1
OH_conc = 1 * 10**-14
k = 50
OH_rate = 0.1

pH = -math.log(H_conc, 10)
pOH = -math.log(OH_conc, 10)

H_set = []
OH_set = []
pH_set = []
pOH_set = []

time_set = []

time = 0
dt = 0.001
time_max = 30

H_set.append(H_conc)
OH_set.append(OH_conc)
pH_set.append(pH)
pOH_set.append(pOH)
time_set.append(time)

while time <= time_max:

    OH_conc += OH_rate * dt

    d_H = 0
    d_OH = 0

    rate = k * H_conc * OH_conc

    d_H -= rate * dt
    d_OH -= rate * dt

    H_conc += d_H
    OH_conc += d_OH

    time += dt

    if OH_conc > H_conc:

        pOH = -math.log(OH_conc, 10)
        pH = 14 - pOH

    elif H_conc > OH_conc:

        pH = -math.log(H_conc, 10)
        pOH = 14 - pH

    else:

        pH = 7
        pOH = 7


    H_set.append(H_conc)
    OH_set.append(OH_conc)
    pH_set.append(pH)
    pOH_set.append(pOH)

    time_set.append(time)

plt.plot(time_set, OH_set, 'b', time_set, H_set, 'r')
plt.xlabel('tijd')
plt.ylabel('concentratie')
plt.grid(True)
plt.xlim(0, time_max)
plt.show()

plt.plot(time_set, pOH_set, 'b', time_set, pH_set, 'r')
plt.xlabel('tijd')
plt.ylabel('pH / pOH')
plt.grid(True)
plt.xlim(0, time_max)
plt.show()
