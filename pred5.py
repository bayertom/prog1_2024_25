n = 5
fn = 1

#V1
while n > 1:
    fn = n * fn
    n = n - 1
    
print(fn)

#V2
n = 5
fn = 1
i = 2

while i <= n:
    fn = i * fn
    i = i + 1

print(fn)

#Find maximum
M = [2.5, 3.4, 1.9, 5.1, 3.9, 2.6]
m_max = M[0]

#Repeat for each m in M
for m in M:
    
    #Actualize maximum
    if m > m_max:
        m_max = m
        
print(m_max)

#Find maximum and minimum
m_max = M[0]
m_min = M[0]

#Repeat for each m in M
for m in M:
    
    #Actualize maximum
    if m > m_max:
        m_max = m
        
    #Actualize minimum
    if m < m_min:
        m_min = m

print(m_min, m_max)

#Range
I = range(1,60,3)
I = range(1,60)
I = range(60)
for i in I:
    print(i)
    
I = range(0, len(M))
for i in I:
    print(i)
    
#Find maximum and minimum using index
m_max = M[0]
m_min = M[0]

#Repeat for each m in M
#I = range(0, len(M))
#for i in I:

for i in range(len(M)):
    
    #Actualize maximum
    if M[i] > m_max:
        m_max = M[i]
        
    #Actualize minimum
    if M[i] < m_min:
        m_min = M[i]

print(m_min, m_max)

#Find maximum and minimum and their indices
i_max = 0
i_min = 0
m_max = M[i_max]
m_min = M[i_min]

for i in range(len(M)):
    
    #Actualize maximum
    if M[i] > m_max:
        m_max = M[i]
        i_max = i
        
    #Actualize minimum
    if M[i] < m_min:
        m_min = M[i]
        i_min = i

print(m_min, m_max, i_min, i_max)

#Find specific m
m_s = 5.1

for i in range(len(M)):
    if M[i] == m_s:
        print('Index: ', i)
        break

#Find first m
m_s = 5.1
i_m = -1

for i in range(len(M)):
    if M[i] == m_s:
        i_m = i
        break

if i_m < 0:
    print('No item in M')
else:
    print('Index: ', i_m)

#Find last m
M = [2.5, 3.4, 1.9, 5.1, 3.9, 2.6, 5.1]

for i in range(len(M)):
    if M[i] == m_s:
        i_m = i

if i_m < 0:
    print('No item in M')
else:
    print('Index: ', i_m)