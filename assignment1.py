#My homework assignment 1
print("Hello world")

#List
A = [2,3]
B = [0,1,'Lewis','University',3.50]
print(A)
print(B)

#print a index of the list.
A.append(2)
A.append(4)
A.append(B)
A.append(16)
for indexPtr,iter in enumerate(B) :
	if (iter == 'University' ) :
		continue
	if indexPtr % 2 == 0 :
		print(" Values: " + str(iter) )
	else :
		print(" Index: " + str(indexPtr))

print(B[2])

#Map
C = {0:'Java',1:'Python',3:'JSON'}
C[0] = 'Testing'

print(C)
print(C[0])
