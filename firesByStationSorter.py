path = "/Users/davidchorvinsky/Desktop/School/Thesis Class/currentCore/arcTextFiles/fires/"
allFires = "/Users/davidchorvinsky/Desktop/School/Thesis Class/finalData/fireData_11_29_1400.txt"
inf = open(allFires,'r')
fData = inf.read()
inf.close()
parts = fData.partition('\n')
header = parts[0]

stations = ["ZBSJ_fires","ZBTJ_fires","ZBAA_fires"]



for i in range(0,3):
    fpath = path + stations[i] + ".txt"

    inf2 = open(fpath, 'r')
    data = inf2.read()
    inf2.close()

    parts2 = data.partition('\n')
    body = parts2[2]
    body2 = body
    bodyList = body2.split('\n')

    arrLatLon = []

    for l in bodyList:
        line = l.split(',')
        lat = float(line[2])
        lon = float(line[3])
        arrLatLon.append(str(lat)+","+str(lon))

    outFires = []
    outFires.append(header)
    for v in arrLatLon:
        i1 = 0
        while i1 > -1:
            i1 = fData.find(v, i1)
            i2 = fData.find("\n", i1)
            outline = fData[i1:i2]
            if len(outline) >= 5:
                outFires.append(outline)
            i1 = i2

    outFireString = "\n".join(outFires)
    outFireString2 = outFireString.replace("\n\n","\n")
    outF = open("/Users/davidchorvinsky/Desktop/School/Thesis Class/currentCore/cleanedFires/" + stations[i] + "11_29_1452.txt", 'w')
    outF.write(outFireString)
    outF.close()


