# Reading file and storing contents
f = open("sample.asm", 'r')
file = (f.read()).split("\n")
f.close()
SC = []
for i in file:
    a = i.split("\t")
    SC.append(a)
del file

# Displaying File Content
f = open("sample.asm", 'r')
print("Source Code : \n")
print(f.read())

# Creating MOT table
MOT = {
    "STOP": ("IS", "00"),
    "ADD": ("IS", "01"),
    "SUB": ("IS", "02"),
    "MULT": ("IS", "03"),
    "MOVER": ("IS", "04"),
    "MOVEM": ("IS", "05"),
    "COMP": ("IS", "06"),
    "BC": ("IS", "07"),
    "DIV": ("IS", "08"),
    "READ": ("IS", "09"),
    "PRINT": ("IS", "10"),
    "LOAD": ("IS", "11"),
    "START": ("AD", "01"),
    "END": ("AD", "02"),
    "ORIGIN": ("AD", "03"),
    "EQU": ("AD", "04"),
    "LTORG": ("AD", "05"),
    "DS": ("DL", "01"),
    "DC": ("DL", "02"),
    "AREG": ("RG", "01"),
    "BREG": ("RG", "02"),
    "CREG": ("RG", "03"),
    "DREG": ("RG", "04"),
    "EQ": ("CC", "01"),
    "LT": ("CC", "02"),
    "GT": ("CC", "03"),
    "LE": ("CC", "04"),
    "GE": ("CC", "05"),
    "ANY": ("CC", "06")
}

# Display table
print()
print("Displaying MOT Table")
for i in MOT:
    print(i, "\t", MOT[i])

ST = {}
LT = []
PT = {}
er = []
LC = 0
flag = 1

print("---------------------")
print("Intermediate Code : ")
print("---------------------\n")
for i in SC:
    label = i[0]
    opcode = i[1]
    operand = i[2]
    if opcode != 'EQU' and opcode != 'END' and opcode != 'LTORG' and opcode != 'ORIGIN':
        print("LC=", LC, end='\t\t')
    else:
        print('', end="\t\t\t")
    if label.isalpha():
        if label not in ST.keys():
            ST[label] = LC
        elif ST[label] == '':
            ST[label] = LC
        else:
            temp = label + " is already declared"
            er.append(temp)
    if opcode == 'START':
        LC = int(operand) - 1
    if opcode != '':
        if opcode in MOT.keys():
            print(MOT[opcode], end='\t')
        else:
            print("**", end="\t")
            temp = opcode + ":Invalid mnemonic"
            er.append(temp)
    else:
        print("\t", end='\t')
    if opcode == 'ORIGIN':
        if operand.isnumeric():
            LC = int(operand)
        else:
            LC = int(ST[operand[0]]) + int(operand[2:])
    if opcode == 'EQU':
        ST[label] = ST[operand]
    if operand.isnumeric():
        print("(C,", operand, ")", end="\t")
    if operand.isalpha():
        if operand not in ST.keys():
            ST[operand] = ''
        a = list(ST.keys()).index(operand) + 1
        print("(S,", a, ")", end="\t")
    if operand != '' and operand[0] == '=':
        if label == '' and opcode == '':
            for j in LT:
                if j[0] == operand and len(j) == 1:
                    j.append(LC)
                    a = LT.index(j) + 1
            if flag == 1:
                PT[a] = ''
        else:
            LT.append(list(operand.split(" ")))
            a = len(LT)
        print("(L,", a, ")")
    if opcode == '':
        flag = 0
    else:
        flag = 1
    if opcode != 'EQU' and opcode != 'END' and opcode != 'LTORG' and opcode != 'ORIGIN':
        LC += 1
    print("\n")
temp = list(PT.keys())
for j in range(0, (len(temp) - 1)):
    PT[temp[j]] = temp[j + 1] - temp[j]
    PT[temp[-1]] = len(LT) - temp[-1] + 1

# Printing Output
print("\n\n---------------------")
print("Symbol Table :")
print("---------------------\n")
print("Symbol\tAddress")
for i in ST:
    print(i, "\t", ST[i])
    if ST[i] == '':
        temp = i + " is not declared"
        er.append(temp)
print("\n\n---------------------")
print("Literal Table :")
print("---------------------\n")
print("Literal\tAddress")
for i in LT:
    print(i[0], "\t", i[1])
print("\n\n---------------------")
print("Pool Table : ")
print("---------------------\n")
print("#P\t#L")
for i in PT:
    print(i, "\t", PT[i])
print("\n\nErrors : ")
for i in er:
    print(i)
