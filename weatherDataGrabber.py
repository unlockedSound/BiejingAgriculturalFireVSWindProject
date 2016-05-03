# import urllib
# print('Set Station Data')

station1 = 'ZBAA'
lat1 = 40.07
lon1 = 116.59

station2 = 'ZBTJ'
lat2 = 39.12
lon2 = 117.35

station3 = 'ZBSJ'
lat3 = 38.28
lon3 = 114.70

print ('Set variables\n\n')
n = 1

stations = [station1, station2, station3]
lats = [lat1, lat2, lat3]
lons = [lon1, lon2, lon3]

index = [0, 1, 2]

months = range(1,13)
years = range(2004, 2015)

print ('Indexes built\n\n')

print ('Run looping script\n\n')
for i in index:
    print ('itteration {i}\n'.format(i=i + 1))
    station = stations[i]
    lat = lats[i]
    lon = lons[i]
    # for y in years:
    #     if y == 2004:
    #         months = range(2,13)
    #     else:
    #         months = range(1,13)
    #
    #     for m in months:
    #         if y == 2004 or y == 2008 or y == 2012:
    #             days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #             days = range(1,days[m-1]+1)
    #
    #         else:
    #             days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #             days = range(1,days[m-1]+1)
    #
    #         for d in days:
    #             theURL ='http://www.wunderground.com/history/airport/{ws}/{y}/{m}/{d}/DailyHistory.html?req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1'.format(ws=station, m=str(m), y=str(y), d=str(d))
    #             infile = urllib.urlopen(theURL)
    #             data = infile.read()
    #             outfile = open("/Users/davidchorvinsky/Desktop/School/Thesis Class/weatherData/workspaceX/{ws}_{yyyy}{mm}{dd}.txt".format(ws=station, yyyy=str(y), mm=(str(m)).zfill(2), dd=(str(d).zfill(2))), 'w+')
    #             outfile.write(data)
    #             outfile.close()
    #             infile.close


    path = "/Users/davidchorvinsky/Desktop/School/Thesis Class/weatherData/workspaceX/"

    OUTfile = path + "weather_data.txt"

    for y in years:
        if y == 2004:
            months = range(2,13)
        else:
            months = range(1,13)
        for m in months:
            if y == 2004 or y == 2008 or y == 2012:
                days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                days = range(1,days[m-1]+1)
            else:
                days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                days = range(1,days[m-1]+1)
            for d in days:
                infile = path + "{ws}_{year}{mm}{dd}.txt".format(ws = station, year = y, mm = (str(m)).zfill(2), dd = (str(d)).zfill(2))
                inf = open(infile, 'r')
                data = inf.read()
                data2 = data.replace("<br />","").replace("\r", "").strip()
                # data3 = data2.strip()
                # data4 = data3.replace("\n\n","")
                parts = data2.partition("\n")
                header = parts[0]


                if n == 1:
                    varList = ['Time', 'Tempurature', 'Dew Point', 'Humidity', 'Sea Level Pressure', 'Visibility',
                               'Wind Direction', 'Wind Speed', 'Gust Speed', 'Precipitation', 'Events', 'Conditions',
                               'Full METAR', 'Wind Direction', 'UTC']
                    shortVarList = ['Time', 'Temp', 'DP', 'Hum', 'Pressure', 'V', 'WD', 'WS', 'GS', 'Precip', 'Ev', 'Con',
                                    'METAR', 'Wind Direction', 'UTC']

                    for i in range(len(varList)):
                        newheader = header.replace(varList[i], shortVarList[i])
                        header = newheader
                        outf = open(OUTfile, 'w')
                        outf.write(newheader + ",lat,lon,stn\n")
                        outf.close()
                    n = n + 1
                    print ('Header created.')

                body = parts[2]
                body2 = body
                bodyList = body2.split("\n")
                outf = open(OUTfile, 'a')


                for p in range(len(bodyList)):
                    line = bodyList[p]

                    if line != "":
                        newLine = line + ',{lat},{lon},{stn}\n'.format(lat=str(lat), lon=str(lon), stn=str(station))
                        outf.write(newLine)
                outf.close()

    print "Finished cleaning the files.\n\n"
print "Finish script. Check txt files."

