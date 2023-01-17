version = "4"
ip_file = "input" + version + ".txt"
op_file = "output" + version + ".txt"

f = open(ip_file, "r")
lines = (f.read()).split("\n")
f.close()

print("\nInput Three Address Code:-")
for line in lines:
    print(line)
print()

linesList = []
for line in lines:
    linesList.append(line.split())
del lines


def convert_operation_to_opcode(op):
    if op == "+":
        return "ADD"
    elif op == "-":
        return "SUB"
    elif op == "*":
        return "MUL"
    elif op == "/":
        return "DIV"


def convert_two_elements(ip_line, file_handler):
    # Lines of the form
    # goto ABC
    print("JMP " + ip_line[1])
    file_handler("JMP " + ip_line[1] + "\n")


def convert_three_elements(ip_line, free_reg, file_handler):
    # Lines of the form
    # x = op z
    # x = z
    # x = A[i]
    # x = *p
    # x = &y
    ip_string = " ".join(ip_line)
    if "[" in ip_string:
        print("MOV " + ip_line[2][0] + ", " + free_reg)
        file_handler.write("MOV " + ip_line[2][0] + ", " + free_reg + "\n")
        print("ADD " + ip_line[2].split("[")[-1].strip("]") + ", " + free_reg)
        file_handler.write("ADD " + ip_line[2].split("[")[-1].strip("]") + ", " + free_reg + "\n")
        print("MOV *" + free_reg + ", " + ip_line[0])
        file_handler.write("MOV *" + free_reg + ", " + ip_line[0] + "\n")
    else:
        print("MOV " + ip_line[2].strip("-") + ", " + free_reg)
        file_handler.write("MOV " + ip_line[2].strip("-") + ", " + free_reg + "\n")
        if ip_line[2].startswith("-"):
            print("NEG " + free_reg)
            file_handler.write("NEG " + free_reg + "\n")
        print("MOV " + free_reg + ", " + ip_line[0])
        file_handler.write("MOV " + free_reg + ", " + ip_line[0] + "\n")


def convert_five_elements(ip_line, free_reg, file_handler):
    # Lines of the form
    #   x = y op z
    print("MOV " + ip_line[2] + ", " + free_reg)
    file_handler.write("MOV " + ip_line[2] + ", " + free_reg + "\n")
    print(convert_operation_to_opcode(ip_line[3]) + " " + ip_line[4] + ", " + free_reg)
    file_handler.write(convert_operation_to_opcode(ip_line[3]) + " " + ip_line[4] + ", " + free_reg + "\n")
    print("MOV " + free_reg + ", " + ip_line[0])
    file_handler.write("MOV " + free_reg + ", " + ip_line[0] + "\n")


def get_jump_opcode(rel_op):
    if rel_op == ">":
        return "JG"
    elif rel_op == ">=":
        return "JGE"
    elif rel_op == "<":
        return "JL"
    elif rel_op == "<=":
        return "JLE"
    elif rel_op == "==":
        return "JE"
    elif rel_op == "!=":
        return "JNE"


def convert_six_elements(ip_line, free_reg, file_handler):
    # Lines of the form
    # if x rel_op y goto ABC
    print("MOV " + ip_line[1] + ", " + free_reg)
    file_handler.write("MOV " + ip_line[1] + ", " + free_reg + "\n")
    print("CMP " + ip_line[3] + ", " + free_reg)
    file_handler.write("CMP " + ip_line[3] + ", " + free_reg + "\n")
    print(get_jump_opcode(ip_line[2]) + " " + ip_line[-1])
    file_handler.write(get_jump_opcode(ip_line[2]) + " " + ip_line[-1] + "\n")


f = open(op_file, "w")
R0 = ""
R1 = ""
for line in linesList:
    print(" ".join(line))
    print("Generated ASSEMBLY for this line:-")

    if len(line) == 2:
        convert_two_elements(line, f)
        print()
        print()
    elif len(line) == 3:
        if R0 == "":
            R0 = line[2].strip("-")
            convert_three_elements(line, "R0", f)
        else:
            R1 = line[2].strip("-")
            convert_three_elements(line, "R1", f)
        if R0 != "" and R1 != "":
            R0 = ""
            R1 = ""
        print()
        print()
    elif len(line) == 5:
        if R0 == "":
            R0 = line[2]
            convert_five_elements(line, "R0", f)
        else:
            R1 = line[2]
            convert_five_elements(line, "R1", f)
        if R0 != "" and R1 != "":
            R0 = ""
            R1 = ""
        print()
        print()
    elif len(line) == 6:
        if R0 == "":
            R0 = line[1]
            convert_six_elements(line, "R0", f)
        else:
            R1 = line[1]
            convert_six_elements(line, "R1", f)
        if R0 != "" and R1 != "":
            R0 = ""
            R1 = ""
        print()
        print()
f.close()

f = open(op_file, "r")
print("Generated Assembly Code:-")
for line in (f.read()).split("\n"):
    print(line)
f.close()
