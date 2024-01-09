import copy
from fractions import Fraction

def lcm(x, y):
    prod = x*y
    while y != 0:
        (x, y) = (y, x % y)
    # Prod // GCD = LCM
    return prod//x

#Clean data so that fractions are reduced
def cleanCycle(ans, add):
    for a in add:
        included = False
        for b in ans:
            if len(a) == len(b):
                x = 0
                failed = False
                while x < len(a)-1:
                    if not a[x] == b[x]:
                        failed = True
                        break
                    x+=1
                if failed == False:
                    included = True
                    b[x] = a[x] + b[x]
        if included == False:
            ans.append(a)

# Multiply Previous Polynomial Term by Each Monomial Term (DP)
def multiplyCycle(mono, cycle, ans):
    for el in cycle:
        i = 0
        sub = 0
        changed = False
        el[len(el)-1] *= Fraction(1,mono[0])
        #If term already exists in monomial add 1 to exponent
        #Else add term to the monomial
        while i < len(el)-1:
            if el[i][1] == mono[1]:
                el[i][0]+=1
                changed = True
                break
            if el[i][1] < mono[1]:
                sub+=1
            i+=1
        if changed == False:
            el.insert(sub, [1,mono[1]])
    if len(cycle) == 0:
        cycle.append([[1,mono[1]], Fraction(1,mono[0])])
    cleanCycle(ans, cycle)

#Cycle Index Calculation (Symmetric Group)
def cycleIndex(x, memo):
    if x in memo:
        return copy.deepcopy(memo[x])
    ans = []
    for l in range(1,x+1):
        multiplied = multiplyCycle([x,l], cycleIndex(x-l, memo), ans)
    memo[x] = ans
    return copy.deepcopy(ans)
    
#Add Width and Height cycles together
#Plug in S to the final Polynomials to get final answer
def addCycle(a, b, s):
    total = 0
    for j in a:
        for k in b:
            x, tempTotal = 0,1
            fract = j[len(j)-1]*k[len(k)-1]
            while x < len(j)-1:
                y = 0
                # Textbook formula for getting Cartesian Product of Cycle Indexes 
                while y < len(k)-1:
                    l = lcm(j[x][1], k[y][1])
                    g = (j[x][1]*k[y][1]*j[x][0]*k[y][0])//l
                    tempTotal*=s**g
                    y+=1
                x+=1
            total += tempTotal*fract
    return total
    
def solution(w,h,s):
    memo = dict()
    memo[0] = []
    cycleW = cycleIndex(w, memo)
    cycleH = cycleIndex(h, memo)
    return str(addCycle(cycleW, cycleH, s))
