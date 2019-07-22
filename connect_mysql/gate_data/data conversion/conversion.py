"78,13282167.00,4788340.50,0335015,0,0,Grand Hotel Qinhuang,370"
import os
import time
"13281828.00,4788836.00,0335016"
cwd = os.getcwd()




def TXTRead_Writeline():
    ms = open(r"C:\Users\zhoujialin\PycharmProjects\LT\connect_mysql\gate_data\data conversion\mkl")
    for line in ms.readlines():
        # print(line)
        # print(type(line))
        line = str(line).split()[0]
        # print(line)
        with open(r"C:\Users\zhoujialin\PycharmProjects\LT\connect_mysql\gate_data\data conversion\write","a") as mon:
            line=line
            new_line = "78,%s,0335015,0,0,Grand Hotel Qinhuang,370" % line

            mon.write(new_line)
            mon.write("\n")



if __name__ == '__main__':
    TXTRead_Writeline()











