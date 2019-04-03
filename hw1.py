#How many times does AGGT or its reverse complement (ACCT) occur in the lambda virus genome? E.g. if 
#AGGT occurs 10 times and ACCT occurs 12 times, you should report 22.
file = open("lambda_virus.txt","r")
file.readline()
genome = ''
for line in file:
    genome+=line.strip()


def genereverse(x):
    rev=''
    diction = {'A':'T','C':'G','T':'A','G':'C','N':'N'}
    for i in range(len(x)):
        rev=diction[x[i]]+rev
    return rev

def naive(p,t):
    occurence = []
    for i in range(len(t)-len(p)+1):
        match = True
        for j in range(len(p)):
            if p[j] !=t[i+j]:
                match = False             
                break
        if match:
            occurence.append(i)
    return occurence

#Question 1
#How many time AGGT or reverse complement occure in the lambda virus

p = 'AGGT'
prev = genereverse(p)
print(len(naive(p,genome)+naive(prev,genome)))

#Question 2
#how many times TTAA or its reverse complement occure
p='TTAA'
print(len(naive(p,genome)))

#Question 3
#what's the leftmost occurance of ACTAAGT
p = 'ACTAAGT'
prev = genereverse(p)
print(min(naive(p,genome)+naive(prev,genome)))


#Question4 
#what's the leftmost occurance of AGTCGA
p='AGTCGA'
prev = genereverse(p)
print(min(naive(p,genome)+naive(prev,genome)))


#Question 5
#Allow two mismatches

def naive_2mm(p,t):
    occurence = []

    for i in range(len(t)-len(p)+1):
        match = True
        esum=0
        for j in range(len(p)):
            if p[j] !=t[i+j]:
                esum+=1
                if esum>2:
                    match=False
                    break
        if match:
            occurence.append(i)
    return occurence

len(naive_2mm('TTCAAGCC',genome))

#Question 6
#leftmost offset of AGGAGGTT
naive_2mm('AGGAGGTT',genome)[0]

#Question 7 
#check which position is abnormal

file = open("first1000.txt")
done = False
sequence=[]
quality=[]
while True:
    file.readline()
    seq = file.readline().rstrip()
    file.readline()
    qual = file.readline().rstrip()
    if len(seq)==0:
        break
    sequence.append(seq)
    quality.append(qual)

    

def getquality(read):
    score=[0]*len(quality[0])    
    for line in quality:       
        for j in range(len(line)):
            score[j]+= (ord(line[j])-33)/len(quality)
    return score

lst = getquality(quality)
print([i for i in range(len(lst)) if lst[i]<5])