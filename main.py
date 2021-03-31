
'''
    alphabet function recive in input a string and return a list with a graphics rappresentation
    of all char in a string. The i-element of list is a list with five element where the list in 
    position 0 is the first line of the terminal, in position 1 is the second line of the therminal etc.
'''
def alphabet(word):
    a1 =  " _____ "
    a2 =  "|     |"
    a3 =  "|_____|"
    a4 =  "|     |"
    a5 =  "|     |"
    a =[a1,a2,a3,a4,a5]
    b1 =  " _____ "
    b2 =  "|     |"
    b3 =  "|____/ "
    b4 =  "|    \ "
    b5 =  "|_____|"
    b = [b1,b2,b3,b4,b5]
    c1 =  " _____ "
    c2 =  "|      "
    c3 =  "|      "
    c4 =  "|      "
    c5 =  "|_____ "
    c =[c1,c2,c3,c4,c5]
    d1 =  " _____ "
    d2 =  "|     \\"
    d3 =  "|     |"
    d4 =  "|     |"
    d5 =  "|_____/"
    d =[d1,d2,d3,d4,d5]
    e1 =  " _____ "
    e2 =  "|      "
    e3 =  "|_____ "
    e4 =  "|      "
    e5 =  "|_____ "
    e =[e1,e2,e3,e4,e5]
    f1 =  " _____ "
    f2 =  "|      "
    f3 =  "|_____ "
    f4 =  "|      "
    f5 =  "|      "
    f =[f1,f2,f3,f4,f5]
    g1 =  " _____ "
    g2 =  "|      "
    g3 =  "|  ___ "
    g4 =  "|     |"
    g5 =  "|_____|"
    g =[g1,g2,g3,g4,g5]
    h1 =  "       "
    h2 =  "|     |"
    h3 =  "|_____|"
    h4 =  "|     |"
    h5 =  "|     |"
    h =[h1,h2,h3,h4,h5]
    i1 =  "|"
    i2 =  "|"
    i3 =  "|"
    i4 =  "|"
    i5 =  "|"
    i =[i1,i2,i3,i4,i5]
    j1 =  "_______"
    j2 =  "    |  "
    j3 =  "    |  "
    j4 =  "    |  "
    j5 =  "____|  "
    j =[j1,j2,j3,j4,j5]
    k1 =  "|    / "
    k2 =  "|   /  "
    k3 =  "|__/   "
    k4 =  "|  \   "
    k5 =  "|   \  "
    k =[k1,k2,k3,k4,k5]
    l1 =  "       "
    l2 =  "|      "
    l3 =  "|      "
    l4 =  "|      "
    l5 =  "|______"
    l =[l1,l2,l3,l4,l5]
    m1 =  " |\  /| "
    m2 =  " | \/ | "
    m3 =  " |    | "
    m4 =  " |    | "
    m5 =  " |    | "
    m =[m1,m2,m3,m4,m5]
    n1 =  " |\   | "
    n2 =  " | \  | "
    n3 =  " |  \ | "
    n4 =  " |   \| "
    n5 =  " |    | "
    n =[n1,n2,n3,n4,n5]
    o1 =  " _____ "
    o2 =  "|     |"
    o3 =  "|     |"
    o4 =  "|     |"
    o5 =  "|_____|"
    o =[o1,o2,o3,o4,o5]
    p1 =  "  ____  "
    p2 =  " |    | "
    p3 =  " |____| "
    p4 =  " |      "
    p5 =  " |      "
    p =[p1,p2,p3,p4,p5]
    q1 =  " _____  "
    q2 =  "|     | "
    q3 =  "|     | "
    q4 =  "|    \| "
    q5 =  "|_____|\\"
    q =[q1,q2,q3,q4,q5]
    r1 =  "  ____  "
    r2 =  " |    | "
    r3 =  " |____| "
    r4 =  " |   \  "
    r5 =  " |    \ "
    r =[r1,r2,r3,r4,r5]
    s1 =  "   _____   "
    s2 =  "  |        "
    s3 =  "   \__     "
    s4 =  "      \    "
    s5 =  "  _____|   "
    s =[s1,s2,s3,s4,s5]
    t1 =  "_______"
    t2 =  "   |   "
    t3 =  "   |   "
    t4 =  "   |   "
    t5 =  "   |   "
    t =[t1,t2,t3,t4,t5]
    u1 =  "         "
    u2 =  "|      | "
    u3 =  "|      | "
    u4 =  "|      | "
    u5 =  "|______| "
    u =[u1,u2,u3,u4,u5]
    v1 =  "        "
    v2 =  "\      /"
    v3 =  " \    / "
    v4 =  "  \  /  "
    v5 =  "   \/   "
    v =[v1,v2,v3,v4,v5]
    w1 =  "          "
    w2 =  "\ \    / /"
    w3 =  " \ \  / / "
    w4 =  "  \ \/ /  "
    w5 =  "   \/\/  "
    w =[w1,w2,w3,w4,w5]
    x1 =  "      "
    x2 =  "\  /  "
    x3 =  " \/   "
    x4 =  " /\   "
    x5 =  "/  \  "
    x =[x1,x2,x3,x4,x5]
    y1 =  "      "
    y2 =  "\   / "
    y3 =  " \ /  "
    y4 =  "  |   "
    y5 =  "  |   "
    y =[y1,y2,y3,y4,y5]
    z1 =  "_____  "
    z2 =  "    /  "
    z3 =  "   /   "
    z4 =  " /    "
    z5 =  "/____ "
    z =[z1,z2,z3,z4,z5]
    virgola = [" ", " ", " ", " ", ","]
    spazio =[ " ", " ", " ", " "," "]
    alp= {
        'a' : a, 
        'b' : b, 
        'c' : c, 
        'd' : d, 
        'e' : e, 
        'f' : f, 
        'g' : g, 
        'h' : h, 
        'i' : i, 
        'j' : j, 
        'k' : k, 
        'l' : l, 
        'm' : m, 
        'n' : n, 
        'o' : o, 
        'p' : p, 
        'q' : q, 
        'r' : r, 
        's' : s, 
        't' : t, 
        'u' : u, 
        'v' : v, 
        'w' : w, 
        'x' : x, 
        'y' : y, 
        'z' : z,
        ' ' : spazio,
        ',' : virgola
    }
    lista = []
    for el in range(0,len(word)):
            lista.append(alp[word[el].lower()])
    return lista

'''
    maxLenStringList recive in input a list of string and return the most longe string
'''
def maxLenStringList(lista):
    max = 0
    for i in lista:
        if(len(i)>max):
            max = len(i)
    return max


'''
    replaceMultiple recive three paramiters: the first is mainString, the second is a list with the chars that you would replace
    and the third is a new char you want insert. return a string with a new char insert
'''
def replaceMultiple(mainString, toBeReplaces, newString): 
    for elem in toBeReplaces :   
        if elem in mainString :
            mainString = mainString.replace(elem, newString)
    
    return  mainString

'''
    aggiungere funzione che divide la stringa in più string di max 30 caratteri
'''

''' 
    aggiungere funzione che stampa (algoritmo nel main)
'''
if __name__ == "__main__":
    name = "io sono male questi giorni e t" 
    '''max num caratteri: 30 '''
    a = alphabet(name)
    for i in range(0,5):
        for j in range(0,len(name)):
            if (len(a[j][i])<7) and ( i == max(a[j])): 
                '''coreggere con  i == max lunghezze di a[j]'''
                print(end="")
            else:
                print(replaceMultiple(a[j][i],["|","_","\\","/"],"/"),end=' ') 
                '''replaceMultiple(a[j][i],["|","_","\\","/"],"@")'''
        print()
