from math import *
path = "/Users/davidchorvinsky/Desktop/School/Thesis Class/currentCore/cleanedFires/"
weatherPath = "/Users/davidchorvinsky/Desktop/School/Thesis Class/currentCore/weatherSets/"
results = "/Users/davidchorvinsky/Desktop/School/Thesis Class/currentCore/results/"

xBeijing = 116.366 #lon
yBeijing = 39.916 #lat

stations = ['ZBSJ','ZBTJ','ZBAA']

missing = 0
missingCheck = 0

for i in range(0,3):
    fires = path + stations[i] + "_fires11_29_1452.txt"

    inf = open(fires, 'r+')
    data = inf.read()
    inf.close()
    parts = data.partition('\n')
    header = parts[0]
    body = parts[2]
    body2 = body
    bodyList = body2.split('\n')

    trueArr = []
    trueArr.append(header)
    falseArr = []
    falseArr.append(header)

    weather = weatherPath + "weather_by_fire_time_for_" + stations[i] + "_11_29_1815.txt"
    winf = open(weather,'r+')
    wData = winf.read()
    winf.close()

    outW = []

    missingArr = []
    missingArr.append(header)

    print stations[i]

    for l in range(0, len(bodyList)):
                    line = bodyList[l].split(',')

                    time = line[3]
                    yFire = float(line[0])
                    xFire = float(line[1])

                    y = yBeijing-yFire
                    x = xBeijing-xFire

                    if y < 0:
                                    vd = 0
                    else:
                                    vd = 180
                    if x < 0:
                                    hd = 90
                    else:
                                    hd = 270
                    if x == 0:
                        x = .0000001
                    if y == 0:
                        y = .0000001

                    angle = degrees(atan(abs(x)/abs(y)))

                    if vd == 0:
                                    if hd == 90:
                                                    a = vd + angle
                                    else:
                                                    a = 360 - angle
                    else:
                                    if hd > vd:
                                                    a = vd +angle
                                    else:
                                                    a = vd - angle
                    #SEARCH HERE
                    i1 = wData.find(time)
                    if i1 == -1:
                        if time == "2012-10-09 06:00:00": #first 6 cases
                            missing = missing + 1
                            target = 350
                        elif time == "2014-08-25 05:00:00": #1 case
                            missing = missing + 1
                            target = 25
                        elif time == "2014-08-21 05:00:00": #1 case
                            missing = missing + 1
                            target = 115
                        elif time == "2014-08-14 04:00:00": #3 cases
                            missing = missing + 1
                            target = 190
                        elif time == "2014-09-08 04:00:00": #2 cases
                            missing = missing + 1
                            target = 75
                        else:
                            missing = missing + 1
                            missingArr.append(bodyList[l])
                            missingCheck = 1


                            # print time
                            # print bodyList[l]
                            # print "missing weather line count:{m}".format(m = missing)
                    else:
                        d0 = (wData[i1-6:i1-1])
                        d1 = d0.split(',')
                        d2 = d1[-1]

                        # d1 = ((wData[i1-6:i1-1]).split(','))[-1]

                        target = int(d2)

                    if missing == 13:
                        missingArr = "\n".join(missingArr)
                        if missingCheck == 1:
                            print missingArr
                        else:
                            print "all missing lines fixed"
                        missing = 0

##############################
#+-15/30degree range
    #                     if a + 15 >= 360:
    #                         aH = a - 345
    #                         aL = a - 15
    #                         if target <= aH or target >= aL:
    #                             trueArr.append(bodyList[l])
    #                         else:
    #                             falseArr.append(bodyList[l])
    #                     elif a - 15 < 0:
    #                         aH = a + 15
    #                         aL = a + 345
    #                         if target <= aH or target >= aL:
    #                             trueArr.append(bodyList[l])
    #                         else:
    #                             falseArr.append(bodyList[l])
    #                     else:
    #                         aH = a + 15
    #                         aL = a - 15
    #                         if aL <= target <= aH:
    #                             trueArr.append(bodyList[l])
    #                         else:
    #                             falseArr.append(bodyList[l])
    # trueOut = "\n".join(trueArr)
    # outTrue = open(results + "true_cases_" + stations[i] + "_30.txt", 'w')
    # outTrue.write(trueOut)
    # falseOut = "\n".join(falseArr)
    # outFalse = open(results + "false_cases_" + stations[i] + "_30.txt", 'w')
    # outFalse.write(falseOut)
##############################
##############################
#+-22.5/45degree range
                    if a + 22.5 >= 360:
                            aH = a - 337.5
                            aL = a - 22.5
                            if target <= aH or target >= aL:
                                trueArr.append(bodyList[l])
                            else:
                                falseArr.append(bodyList[l])
                    elif a - 22.5 < 0:
                        aH = a + 22.5
                        aL = a + 337.5
                        if target <= aH or target >= aL:
                            trueArr.append(bodyList[l])
                        else:
                            falseArr.append(bodyList[l])
                    else:
                        aH = a + 22.5
                        aL = a - 22.5
                        if aL <= target <= aH:
                            trueArr.append(bodyList[l])
                        else:
                            falseArr.append(bodyList[l])

    trueOut = "\n".join(trueArr)
    outTrue = open(results + "true_cases_" + stations[i] + "_45_degrees_12_7_test2.txt", 'w')
    outTrue.write(trueOut)
    falseOut = "\n".join(falseArr)
    outFalse = open(results + "false_cases_" + stations[i] + "_45_degrees_12_7_test2.txt", 'w')
    outFalse.write(falseOut)
##############################