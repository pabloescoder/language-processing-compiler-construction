# Reading file and storing contents
f = open("sample2.asm", 'r')
file = (f.read()).split("\n")
f.close()
SC = []
for i in file:
    a = i.split("\t")
    SC.append(a)
del file
# displaying file
f = open("sample2.asm", 'r')
print("Source Code : \n")
print(f.read())


# Macro function
def macro(a):
    # macro name
    mname = SC[a][1]
    MNT[0].append(mname)
    # macro parameters
    if SC[a][2] != '':
        para = list(SC[a][2].split(","))
        Parameter[mname] = {}
        for i in range(0, len(para)):
            Parameter[mname][para[i]] = "#" + str(i + 1)
    else:
        para = []
    num_para = len(para)
    MNT[1].append(num_para)
    # starting index for macro
    MNT[2].append(len(MDT) + 1)
    # macro definition Table
    a += 1
    while SC[a][0] != "MEND":
        while SC[a][0] == '':
            del (SC[a][0])
        if SC[a][0] in MNT[0]:
            i = MNT[0].index(SC[a][0])
            i = MNT[2][i] - 1
            t_para = list(SC[a][1].split(","))
            if SC[a][0] not in actual_para.keys():
                actual_para[SC[a][0]] = {}
            while MDT[i] != "MEND":
                b = MDT[i]
                for j in range(0, len(t_para)):
                    temp = str("#" + str(j + 1))
                    if b.find(temp) != -1:
                        b = b.replace(temp, t_para[j])
                        actual_para[SC[a][0]][t_para[j]] = temp
                    # if "#"+str(j) is present in b:
                    #   replace with para(j)
                MDT.append(b)
                i += 1
        else:
            b = SC[a]
            if b[1] in para:
                b[1] = Parameter[mname][b[1]]
            MDT.append(" ".join(b))
        a += 1
    MDT.append("MEND")


MDT = []
MNT = [[], [], []]
Parameter = {}
actual_para = {}
# Intermediate Code
print("---------------------")
print("Intermediate Code : ")
print("---------------------\n")
i = 0
while i < len(SC):
    if SC[i][0] == 'MACRO':
        macro(i)
        while SC[i][0] != "MEND":
            i += 1
    else:
        if SC[i][0] == "":
            del (SC[i][0])
        print(" ".join(SC[i]))
    i += 1
# MNT
print("\n\n---------------------")
print("MNT : ")
print("---------------------\n")
a = len(MNT[0])
print("Name\tNo. Para\tStart index")
for i in range(0, a):
    print(MNT[0][i], "\t", MNT[1][i], "\t\t", MNT[2][i])
# MDT
print("\n\n---------------------")
print("MDT : ")
print("---------------------\n")
for i in MDT:
    print(i)
# Formal Parameters
print("\n\n-------------------------------")
print("Formal Vs Positional Parameters : ")
print("------------------------------\n")
for i in Parameter:
    print(i)
    print("Formal\tPositional Parameter")
    for j in Parameter[i]:
        print(j, "\t", Parameter[i][j])
    print("")
# Actual Parameters
print("\n\n-------------------------------")
print("Actual Vs Positional Parameters : ")
print("-------------------------------\n")
for i in actual_para:
    print(i)
    print("Actual\tPositional Parameter")
    for j in actual_para[i]:
        print(j, "\t", actual_para[i][j])
    print("")
