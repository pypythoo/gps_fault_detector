import matplotlib.pyplot as plt
import random 
import time 

gps_data = []
time_stmp= []

print("Starting Navigation System...\n")

plt.ion()
for t in range(20):  #runs 20 times = 20 seconds (simulation)
    if t == 10:
        gps = 500
    else:
        gps = 100 + random.randint(-5,5) + t

    gps_data.append(gps)
    time_stmp.append(t)

if t > 0:
    change = gps_data[t] - gps_data[t-1] #Compare current vs previous value

    if abs(change) > 50:
        print(f"GPS fault detected at time {t} seconds! GPS value: {gps_data[t]}")

    plt.clf() #Clears previous frame Otherwise graph overlaps

    plt.plot(time_stmp, gps_data, marker='o') #marker='o' → dots on points
    plt.title("Real time GPS monitoring")
    plt.xlabel("time")
    plt.ylabel("position")

    ply.pause(0.5)
plt.ioff() #Turn off interactive mode
plt.show()  

 
