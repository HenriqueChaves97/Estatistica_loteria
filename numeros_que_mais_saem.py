s = []
data = []
f  = (
    "1..10", 
    "11..20", 
    "21..30", 
    "31..40", 
    "41..50", 
    "51..60", 
    "61..70", 
    "71..80", 
    "81..90", 
    "91..99",
)
tabela = {
    0:[1,25,37,45,69,78,6,23,45,67,89,6,43,45,72,12],
    1:[72,23,32,14,56,55,75,43,25,2,34,57,48,8,3],
    2:[5,26,36,46,66,78,1,63,45,67,89,0,33,49,76,45],
    3:[12,23,32,14,56,55,66,43,25,2,34,57,55,8,2],
    4:[61,27,53,25,65,78,2,63,45,67,89,0,67,78,62,23],
    5:[12,23,32,14,57,55,44,43,25,2,34,57,76,8,5],
    6:[14,28,43,95,75,78,3,23,45,67,89,0,43,5,54,24],
}

def main(s,tabela):        
    for line in tabela:
        s += tabela[line]    
    for value in s:
        if value in range(1,11):
            data.append(f[0])
        elif value in range(11,21):
            data.append(f[1])
        elif value in range(21,31):
            data.append(f[2])
        elif value in range(31,41):
            data.append(f[3])
        elif value in range(41,51):
            data.append(f[4])
        elif value in range(51,61):
            data.append(f[5])
        elif value in range(61,71):
            data.append(f[6])
        elif value in range(71,81):
            data.append(f[7])
        elif value in range(81,91):
            data.append(f[8])
        elif value in range(91,100):
            data.append(f[9])

main(s,tabela)
for k in f:
    print("{} : {}".format(k, data.count(k)))