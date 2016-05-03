print ("Script open")
path = "/Users/davidchorvinsky/Desktop/School/Thesis Class/fireData/firms274291445968801_MCD14ML/firms2742914459688011_MCD14ML.txt"
finalPath = "/Users/davidchorvinsky/Desktop/School/Thesis Class/finalData/"

outarr = []
outHeader = []
varList = [2, 3, 6, 9, 12]
f = path
outName = finalPath + "fireData_11_29_1400.txt"
inf = open(f, 'r+')
data = inf.read()
inf.close()
outf = open(outName, 'w')

parts = data.partition('\n')
header = parts[0]
body = parts[2]
body2 = body
bodyList = body2.split("\n")

splitHeader = header.split(",")
newHeader = splitHeader[1]

for l in varList:
    newHeader = newHeader + "," + splitHeader[l]
newHeader = newHeader + "\n"
outHeader.append(newHeader)

for p in range(len(bodyList)):
    line = bodyList[p]
    splitLine = line.split(",")
    if len(splitLine) > 12:
        newline = splitLine[1]
        for l in varList:
            if l == 6:
                date = splitLine[6]
                time = splitLine[7]
                hr = time[0:2]
                minute = time[2:5]
                minutes = int(minute)
                sec = ":00"
                if minutes < 30:
                    minute = "00"
                    # print (hr +":"+ min + ":" + sec)
                else:
                    minute = "00"
                    hr = int(hr)
                    if hr < 23:
                        hr = hr + 1
                        hr = str(hr).zfill(2)
                    else:
                        hr = "00"
                newline = newline + "," + date + " " + hr + ":" + minute + sec
            else:
                newline = newline + "," + splitLine[l]
        outarr.append(newline)
outHeader = "\n".join(outHeader)
outstr = "\n".join(outarr)
outf.write(outHeader)
outf.write(outstr)
outf.close()

print ("Script finished")
