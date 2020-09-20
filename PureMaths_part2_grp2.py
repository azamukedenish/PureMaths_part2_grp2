#-------------------------------------------------------------------------------
#Group 2:       
# Purpose: AIMS Pre-Masters Course
#
# Students:   Mulumba Denis
#                      Uwitonze Daniel
#                      Germaine Neza Hozana
#                      Akimana Jean Irénée  
#                      Azamuke Denish
#
# Created:     20/09/2020
# 
# Question 1 (c)
#-------------------------------------------------------------------------------

f=2
m=[]
M=[]
n=[]
m.append(f+1)
m.append(3*f+1)

# Here m = [3,7], values from part (a)

j = 1

while j<4:
    for i in range(0,len(m)):
        a = 3*m[i]+1
        b = m[i]+1
        if a%3 == 1:
            M.append(a)
        if b%3 != 1:
            M.append(b)
    m = M
    M=[]
    j=j+1
n = m
# The values of n are:
print(n)