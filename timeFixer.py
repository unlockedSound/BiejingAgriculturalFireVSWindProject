path = "/Users/davidchorvinsky/Desktop/School/Thesis Class/currentCore/results/"

stations = ["ZBAA", "ZBTJ", "ZBSJ"]
true_false =  ["true", "false"]

for a in range(0,3):
    for b in range (0,2):

        inPath = path + true_false[b] + "_cases_" + stations[a] + "_45_degrees_1129_1830.txt"

        inf = open(inPath, 'r+')
        data = inf.read()
        inf.close()

        parts = data.partition('\n')
        header = parts[0]
        body = parts[2]
        body2 = body.replace(" ",",")
        body3 = body2.replace(":00:00","")

        header = "latitude,longitude,brightness,acq_date,acq_time,confidence,frp"

        # outArr = []
        outString = header + "\n" + body3
        OutFile = open(path + true_false[b] + "_cases_" + stations[a] + "_45_degrees_with_time_added.txt", 'w')
        OutFile.write(outString)
        OutFile.close()
