file = open("nfa4.txt","r")
states = []
alphabet = []
transitions = []
b = 0
for i in file:
    if i == 'Estados\n':
        b = 1
        continue
        
    if i == 'Alfabeto\n':
        b = 2
        continue
    if i == 'Transiciones\n':
        b = 3
        continue


    if b == 1:
        states.append(i.strip())
    if b == 2:
        alphabet.append(i.strip())
    if b == 3:
        transitions.append(i.strip())


file.close()

result = {}
for i in states:
    i = i.replace("\n","")
    i = i.replace(">","")
    i = i.replace("*","")
    result[i] = {}
    for j in alphabet:

        result[i][j] = []

for i in transitions:
    i = i.replace(" ","")
    i = i.split("->")
    result[i[0][0]][i[0][1]].append(i[1])
            
constant_transitions = result
new_dicc = {}

for i in result:
    for j in alphabet:
        t = result[i][j]
        t = ','.join(t)
        if t not in new_dicc and t != "":
            new_dicc[t] = {}
for i in new_dicc:
    for j in alphabet:
        new_dicc[i][j] = []
        for k in i.split(","):
            new_dicc[i][j] += result[k][j]


def loop_nfa(result,alphabet,constant_transitions):
    new_dicc = {}
    for i in result:
        for j in alphabet:
            t = result[i][j]
            t = ','.join(t)
            if t not in new_dicc and t != "":
                new_dicc[t] = {}

    for i in new_dicc:
        for j in alphabet:
            new_dicc[i][j] = []

    for i in constant_transitions:
        for j in alphabet:
            t = constant_transitions[i][j]
            for k in new_dicc:
                if i in k:
                    new_dicc[k][j] += t
    return new_dicc
            
        
dic = loop_nfa(new_dicc,alphabet,constant_transitions)

while dic != new_dicc:
    new_dicc = dic
    dic = loop_nfa(new_dicc,alphabet,constant_transitions)

def txt_wright(dic,state):
    file = open("dfa.txt","w")
    file.write("Estados\n")
    for i in dic:
        for j in state:
            if ">" in j and i == j.replace(">",""):
                file.write(">")
            k = j.replace(">","")
            if "*" in k and k.replace("*","") in i:
                file.write("*")
        file.write("{"+i+"}"+"\n")
    file.write("Alfabeto\n")
    for i in alphabet:
        file.write("{"+i+"}"+"\n")
    file.write("Transiciones\n")
    for i in dic:
        for j in alphabet:
            if dic[i][j] != []:
                file.write("{"+i+"}"+" "+j+" -> "+"{"+','.join(dic[i][j])+"}"+"\n")
    file.close()
txt_wright(dic,states)
            

            










