input_expression = "a = b * c + -d * e + f + g"
# input_expression = "a = b + c + -d + e + f * g"
print("\nInput Expression:-")
print(input_expression)
print()

operators = {
    "^": 0,
    "*": 1,
    "/": 1,
    "+": 2,
    "-": 2
}

res = []
id = 1
expression = input_expression


def handle_uminus(idx):
    global id, res, x
    temp = "T" + str(id) + " = " + x[idx]
    res.append(temp)
    del x[idx]
    x.insert(idx, "T" + str(id))
    id += 1


def convert_part_of_exp(start_idx):
    global id, res, x
    temp = "T" + str(id) + " = " + x[start_idx] + " " + x[start_idx + 1] + " " + x[start_idx + 2]
    res.append(temp)
    for j in range(3):
        del x[start_idx]
    x.insert(start_idx, "T" + str(id))
    id += 1


x = expression.split()

i = 2
while True:
    x_len = len(x)
    if i == x_len - 2:
        break
    if x[i].startswith("-"):
        handle_uminus(i)
        i += 1
    elif x[i] in operators:
        if i + 2 < x_len - 1 and operators[x[i + 2]] < operators[x[i]]:
            if x[i + 1].startswith("-"):
                handle_uminus(i + 1)
            if x[i + 3].startswith("-"):
                handle_uminus(i + 3)
            convert_part_of_exp(i + 1)
        else:
            if x[i - 1].startswith("-"):
                handle_uminus(i - 1)
            if x[i + 1].startswith("-"):
                handle_uminus(i + 1)
            convert_part_of_exp(i - 1)
    else:
        i += 1

temp = ""
for i in x:
    temp += str(i) + " "

res.append(temp)

print("Generated Three Address Code:-")
for i in res:
    print(i)

f = open("output1.txt", "w")
f.write("\n".join(res))
f.close()
