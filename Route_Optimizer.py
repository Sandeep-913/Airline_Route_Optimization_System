cities = dict({
    0: "Agra",
    1: "Delhi",
    2: "Bangalore",
    3: "Hyderabad",
    4: "Mumbai",
    5: "Kolkata",
    6: "Chennai",
    7: "Calicut",
    8: "Tirupati"
})

ConnectedFlights = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8],
                    [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8],
                    [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8],
                    [3, 4], [3, 5], [3, 6], [3, 7], [3, 8],
                    [4, 5], [4, 6], [4, 7], [4, 8],
                    [5, 6], [5, 7], [5, 8],
                    [6, 7], [6, 8],
                    [7, 8]]
DistanceFlightsInKM = [[180, 1577, 1084, 1037, 1160, 1586, 1801, 684],
                       [1397, 950, 900, 980, 1405, 1620, 400],
                       [503, 844, 1560, 284, 277, 213],
                       [617, 1180, 521, 747, 428],
                       [1652, 1028, 942, 918],
                       [1366, 1838, 1367],
                       [523, 111],
                       [481]]
CostOfFlights = [[5400, 6000, 6200, 4900, 6500, 6120, 8000, 4000],
                 [7200, 6300, 3800, 5500, 6120, 6793, 9580],
                 [2870, 7500, 5000, 1835, 3139, 4200],
                 [3510, 7835, 2791, 5006, 3500],
                 [9017, 5130, 5230, 7780],
                 [7200, 10316, 11090],
                 [4270, 7280],
                 [6245]]
TimeInMinutes = [[340, 150, 300, 140, 250, 290, 365, 130],
                 [175, 135, 130, 135, 165, 175, 260],
                 [160, 130, 145, 70, 72, 65],
                 [150, 125, 130, 130, 125],
                 [140, 115, 95, 355],
                 [268, 275, 270],
                 [100, 345],
                 [425]]

FlightAdjacencyList = []

for i in range(9):
    k = []
    for j in range(9):
        if i == j:
            continue
        l = []
        if i < j:
            l.append(j)
            l.append(DistanceFlightsInKM[i][j - 1 - i])
            l.append(CostOfFlights[i][j - 1 - i])
            l.append(TimeInMinutes[i][j - 1 - i])
        elif i > j:
            l.append(j)
            l.append(DistanceFlightsInKM[j][i - 1 - j])
            l.append(CostOfFlights[j][i - 1 - j])
            l.append(TimeInMinutes[j][i - 1 - j])
        k.append(l)
    if k:
        FlightAdjacencyList.append(k)


def Dijkshtra(src, dest, index):
    k = [float('inf')] * 9
    v = [0] * 9
    k[src] = 0
    v[src] = 1
    p = [-1] * 9
    a = [[0, src]]
    while len(a) != 0:
        pres = a[0]
        a.pop(0)
        for i in FlightAdjacencyList[pres[1]]:
            if pres[0] + i[index] < k[i[0]]:
                k[i[0]] = pres[0] + i[index]
                a.append([k[i[0]], i[0]])
                p[i[0]] = pres[1]
        a.sort()
    z = []
    z.append(dest)
    z.append(p[dest])
    ele = p[dest]
    while p[ele] != -1:
        z.append(p[ele])
        ele = p[ele]
    z.reverse()
    length = len(z)
    if index == 1:
        print("\nThe shortest distance from " + cities[src] + " to " + cities[dest] + " is: ")
        for i in z:
            print(" -> " + cities[i], end="")
        time = 0
        cost = 0
        for i in range(1, length):
            if z[i - 1] > z[i]:
                time += TimeInMinutes[z[i]][z[i - 1] - 1 - z[i]]
                cost += CostOfFlights[z[i]][z[i - 1] - 1 - z[i]]
            if z[i - 1] < z[i]:
                time += TimeInMinutes[z[i - 1]][z[i] - 1 - z[i - 1]]
                cost += CostOfFlights[z[i - 1]][z[i] - 1 - z[i - 1]]
        print("\n\nThe Minimum Distance is: " + str(k[dest]) + "KM")
        print("\nThe Cost is: " + str(cost) + "Rs")
        print("\nThe Time is: " + str(time) + "min")

    if index == 2:
        print("\nThe cheapest distance from " + cities[src] + " to " + cities[dest] + " is: ")
        for i in z:
            print(" -> " + cities[i], end="")
        distance = 0
        time = 0
        for i in range(1, length):
            if z[i - 1] > z[i]:
                distance += DistanceFlightsInKM[z[i]][z[i - 1] - 1 - z[i]]
                time += TimeInMinutes[z[i]][z[i - 1] - 1 - z[i]]
            if z[i - 1] < z[i]:
                distance += DistanceFlightsInKM[z[i - 1]][z[i] - 1 - z[i - 1]]
                time += TimeInMinutes[z[i - 1]][z[i] - 1 - z[i - 1]]
        print("\n\nThe Minimum Cost is: " + str(k[dest]) + "Rs")
        print("\nThe distance is: " + str(distance) + "KM")
        print("\nThe Time is: " + str(time) + "min")

    if index == 3:
        print("\nThe fastest distance from " + cities[src] + " to " + cities[dest] + " is: ")
        for i in z:
            print(" -> " + cities[i], end="")
        distance = 0
        cost = 0
        for i in range(1, length):
            if z[i - 1] > z[i]:
                distance += DistanceFlightsInKM[z[i]][z[i - 1] - 1 - z[i]]
                cost += CostOfFlights[z[i]][z[i - 1] - 1 - z[i]]
            if z[i - 1] < z[i]:
                distance += DistanceFlightsInKM[z[i - 1]][z[i] - 1 - z[i - 1]]
                cost += CostOfFlights[z[i - 1]][z[i] - 1 - z[i - 1]]
        print("\n\nThe Minimum Time is: " + str(k[dest]) + "min")
        print("\nThe Cost is: " + str(cost) + "Rs")
        print("\nThe distance is: " + str(distance) + "KM")


def takeinput():
    print("Welcome to Airline route optimization system")
    print("These are the flights available right now: ")
    for i in cities:
        print("code: " + str(i) + "\t\t" + str(cities[i]))
    print("Enter your source city code: ")
    src = int(input())
    print("Enter your destination city code: ")
    dest = int(input())
    print("ThankYou for confirming the details")
    print("Enter 1 if you want the shortest path")
    print("Enter 2 if you want the cheapest path")
    print("Enter 3 if you want the fastest path")
    print("Enter 4 to exit")
    run = 1
    while run:
        path = int(input())
        if path == 1:
            Dijkshtra(src, dest, 1)
            pass
        elif path == 2:
            Dijkshtra(src, dest, 2)
            pass
        elif path == 3:
            Dijkshtra(src, dest, 3)
            pass
        else:
            run = 0
            print("Thank You for using. Please vist again")


takeinput()
