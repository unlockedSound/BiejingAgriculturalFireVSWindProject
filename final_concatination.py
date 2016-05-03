path = "/Users/davidchorvinsky/Desktop/School/Thesis Class/currentCore/results/final_txt_versions/"

# stations = ["ZBAA", "ZBTJ", "ZBSJ"]
# true_false = ["true", "false"]
#
# for a in range(0,3):
#     for b in range (0,2):
#         inPath = path + true_false[b] + "_" + stations[a] + "_45_degrees_final.txt"
#
#         inf = open(inPath, 'r+')
#         data = inf.read()
#         inf.close()


inf1 = open(path + "true_ZBAA_45_degrees_final.txt", 'r')
data1 = inf1.read()

inf1.close()

parts1 = data1.partition('\n')
header = parts1[0]
body1 = parts1[2]

inf2 = open(path + "true_ZBSJ_45_degrees_final.txt", 'r')
data2 = inf2.read()
inf2.close()

parts2 = data2.partition('\n')
print parts2[0]
body2 = parts2[2]

inf3 = open(path + "true_ZBTJ_45_degrees_final.txt", 'r')
data3 = inf3.read()
inf3.close()

parts3 = data3.partition('\n')
body3 = parts3[2]

inf4 = open(path + "false_ZBAA_45_degrees_final.txt", 'r')
data4 = inf4.read()
inf4.close()

parts4 = data4.partition('\n')
body4 = parts4[2]

inf4 = open(path + "false_ZBSJ_45_degrees_final.txt", 'r')
data4 = inf4.read()
inf4.close()

parts4 = data4.partition('\n')
body4 = parts4[2]

inf5 = open(path + "false_ZBAA_45_degrees_final.txt", 'r')
data5 = inf5.read()
inf5.close()

parts5 = data5.partition('\n')
body5 = parts5[2]

inf6 = open(path + "false_ZBTJ_45_degrees_final1.txt", 'r')
data6 = inf6.read()
inf6.close()

parts6 = data6.partition('\n')
body6 = parts6[2]


outString1 = header + "\n" + body1 + "\n" + body2 + "\n" + body3
OutFile1 = open(path + "all_true_cases1.txt", 'w')
OutFile1.write(outString1)
OutFile1.close()

outString2 = header +"\n" + body4 + "\n" + body5 + "\n" + body6
OutFile2 = open(path + "all_false_cases1.txt", 'w')
OutFile2.write(outString2)
OutFile2.close()
