from fractions import Fraction

def det(matrix):
	#Returns the determinant of the given matrix, so long as the input matrix is square.
	m=len(matrix) 
	n=len(matrix[0])
	if (m!=n): #Makes sure input is square
		return "Input matrix must be square." 
	if(m==1): #If 1x1 then return inner value
		return matrix[0][0]
	output = 0 #Initialize output
	for k in range(0,n): #Iterate through each item in the first row
		inner=[]
		for i in range(1,m): #Iterate through each row other than the first
			inRow=[] 
			for j in range(0,n): #Iterate through each value in the current row
				if (j != k): #Set aside all values not in the same column as the current row 1 value for recursive calculation
					inRow.append(matrix[i][j])
			inner.append(inRow)
		if(k%2==0): #We will multiply each first row value by the determinant of its corresponding inner matrix and add/subtract these new values. Starting at 0, even valued indexes are added and odds are subtracted.
			output += matrix[0][k] * det(inner)
		else:
			output -= matrix[0][k] * det(inner)
	return output 
	
def transpose(matrix):
	#Returns the transpose of a given matrix.
	m=len(matrix)
	n=len(matrix[0])
	output = []
	for i in range(0,n): #Iterates through each column
		row = []
		for j in range(0,m): #Converts current column into a row by iterating through each value
			row.append(matrix[j][i])
		output.append(row)	#Puts these new rows into the output
	return output
		
def zeroMatrix(m, n=0):
	#Returns a zero matrix of specified size.
	if(n==0): n=m #If number of columns is not specified then make the matrix square.
	output = []
	for i in range(0,m): #Create m rows
		row=[]
		for j in range(0,n): #Each row should have n values/columns
			row.append(0) #Append necessary 0 values
		output.append(row)
	return output

def identityMatrix(order):
	#Returns the identity matrix of specified size.
	output= zeroMatrix(order) #Begin with a zero matrix
	for i in range(0,order):
		output[i][i] = 1 #Puts values of 1 along the main diagonal.
	return output
	
def matrify(vector, format="col"):
	#Convert a vector in list (1d list array) format into a matrix (2d list array) for the purposes of vector algebra functions which assume matrix-format. Specify either row (1xn) or column (mx1) vector format for conversion; column is default.
	s=len(vector)
	if (format == "row"):
		output = [[]] #Initializes output as 1xn
		for i in range(0,s): #Iterate through values to create matrix adaptation in row vector format
			output[0].append(vector[i])
		return output
	elif(format == "col" or format == "column"):
		output = [] #Initializes output as mx1
		for i in range(0,s): #Iterate through values to create matrix adaptation in column vector format
			output.append([vector[i]])
		return output
	else:
		return(format+ " is not a valid format.") #Catches formats which are not either row or column.	

def dot(vec1,vec2):
	#Returns the dot product of two vectors. Input vectors should both be of the same orientation (row or column) and the same size, and in matrix format.
	m1,n1,m2,n2=len(vec1),len(vec1[0]),len(vec2),len(vec2[0])	
	if (not (m1==m2 and n1==n2) or not(m1==1 or n1==1)): #Test for size and formatting
		return "Vectors must be of equal size and properly formatted."
	output = 0 #Initialize constant output value
	if(m1==1): #If the vectors are row vectors:
		for i in range(0,n1): #Iterate through values and multiply correspondingly
			output+=(vec1[0][i]*vec2[0][i])
		return output
	if(n1==1): #If the vectors are column vectors:
		for i in range(0,m1): #Iterate through values and multiply correspondingly
			output+=(vec1[i][0]*vec2[i][0])	
		return output

def multiplyMatrices(matrix1, matrix2):
	#Multiplies two matrices and returns the resulting matrix.
	m1,n1,m2,n2=len(matrix1),len(matrix1[0]),len(matrix2),len(matrix2[0])
	if (n1 != m2): #Confirms that the number of columns in the first matrix is equal to the number of rows in the second.
		return "Matrices are not of compatible sizes."
	output = zeroMatrix(m1,n2) #Initializes output matrix as a blank/zero matrix, with the number of rows from the first matrix and columns from the second.
	for i in range(0,m1): #Iterate through each row of the first matrix.
		rowV=matrix1[i]
		for j in range(0,n2): #Iterate through each column of the second matrix.
			colV=[]
			for k in range(0,m2): #Set aside all values of a column into a vector
				colV.append(matrix2[k][j])
			output[i][j]=dot(matrify(rowV),matrify(colV)) #Take the dot product of these vectors, converted into corresponding matrix formats, and put it into the proper position in the resulting matrix.
	return output

def norm(vector,nrm=2):
	#Returns the nth norm of a vector. If norm is not specified, 2 is used as default, which is the same as the vector's magnitude. The vector must be in matrix list format.
	m=len(vector)
	n=len(vector[0])
	if not (m==1 or n==1): #Make sure the vector is of proper size and format.
		return "Input must be a vector."	
	vec = []	#Initialize a list which is easy to iterate through.
	if(m==1): #If it's a row vector then just use the one row as the list.
		vec = vector[0]
	else: #If it's a column vector then iterate to create the list.
		for i in range(0,m):
			vec.append(vector[i][0])
	value = 0
	if (nrm=="inf"): #Support for inf-norm
		for j in range(0,len(vec)): #Iterate to find max value.
			if (vec[j] > value):
				value = vec[j]
		return value
	else:	#For regular n-norms, calculate the norm value through iteration.
		for j in range(0,len(vec)):
			value += (vec[j] ** nrm)
		return (value**(1/nrm))
	
def scale(matrix,alpha):
	#Returns the matrix scaled by the given constant value.
	m=len(matrix)
	n=len(matrix[0])
	output=matrix
	for i in range(0,m): #Iterate through rows
		for j in range(0,n): #Iterate through values in these rows
			output[i][j] *= alpha #Perform individual scalar multiplication
	return output
	
def addMatrices(matrix1,matrix2):
	#Adds two matrices and returns the resulting matrix.
	m1,n1,m2,n2=len(matrix1),len(matrix1[0]),len(matrix2),len(matrix2[0])
	if not (m1==m2 and n1==n2): #Confirms that the matrices are the same size.
		return "Matrices must be the same sizes."
	output=matrix1
	for i in range(0,m1): #Iterate through rows
		for j in range(0,n1): #Iterate through values in these rows
			output[i][j]+=matrix2[i][j]	#Add corresponding values.
	return output

def axpy(x,y,a):
	#Performs the AXPY operation, or single-scaled addition, on two matrices; returning the resulting matrix.
	return addMatrices(scale(x,a),y)
	
def linComb(x,y,a,b):
	#Returns the linear combination of two scaled matrices.
	return addMatrices(scale(x,a),scale(y,b))
	
def rowSwap(matrix,r1,r2):
	#Performs the operation R1<->R2. Inputs should be the 0-indices of the desired rows to swap. Returns resulting matrix.
	output=matrix
	output[r1],output[r2]=output[r2],output[r1]
	return output
	
def rowAddition(matrix,r1,r2):
	#Performs the operation R1+R2->R1. Inputs should be the 0-indices of the desired rows to add. Returns resulting matrix.
	output=matrix
	for i in range(0,len(output[r1])): #Iterative addition
		output[r1][i]+=output[r2][i]
	return output

def rowScale(matrix,row,alpha):
	#Performs the operation AR1->R1. Input the 0-index of the desired row and the scalar Alpha. Returns resulting matrix.
	output=matrix
	for i in range (0,len(output[row])): #Iterative scaling
		output[row][i]*=alpha
	return output
	
def scaledRowAddition(matrix,r1,r2,alpha):
	#Performs the operation R1+AR2->R1. Inputs should be the 0-indices of the desired rows to add, as well as the scalar Alpha. Returns resulting matrix.
	output=matrix
	for i in range(0,len(output[r1])): #Iterative scaled addition
		output[r1][i]+=alpha*output[r2][i]
	return output
	
def hAppend(matrix1,matrix2):
	#Appends matrix2 to the right of matrix, and returns the resulting matrix.
	m1 = len(matrix1)
	m2 = len(matrix2)
	if not (m1==m2): #Confirms that the matrices have the same number of rows.
		return "Matrices must have the same number of rows."
	aC = len(matrix2[0])
	output = matrix1
	for i in range(0,m1): #Iterates through each row
		for j in range(0,aC): #Appends each value of this row from the second matrix into the first.
			output[i].append(matrix2[i][j])
	return output
	
def trace(matrix):
	#Returns the trace of a square matrix (the sum of elements along the main diagonal).
	m,n=len(matrix),len(matrix[0])
	if (m!=n): #Confiems that matrix is square.
		return "Input matrix must be square."
	output=0
	for i in range(0,m): #Iterates through and sums the main diagonal.
		output+=matrix[i][i]
	return output

#def rref(matrix):
	#Computes the Reduced Row Echelon Form of a matrix and returns this as a new matrix.
	#Not yet created.
	#output=matrix
	
	#return output

def mPrint(matrix, s=1, l=0):
	#Prints the values of a matrix or vector in a specific format designed for readability. 
	#There will be s spaces between each entry of a row, and l lines between rows.
	m,n=len(matrix),len(matrix[0])
	for i in range(0,m):
		str=""
		spaces = ""
		for a in range(0,s):
			spaces += " "
		for j in range(0,n):
			str+=("%s%s") % (matrix[i][j], spaces)
		print(str)
		for k in range(0,l):
			print
	return "Complete"
	
def ratMPrint(matrix, s=1, l=0):
	#Prints the values of a matrix or vector in a specific format designed for readability, in rational (fractional) format rather than decimal.
	#There will be s spaces between each entry of a row, and l lines between rows.
	m,n=len(matrix),len(matrix[0])
	for i in range(0,m):
		str=""
		spaces = ""
		for a in range(0,s):
			spaces += " "
		for j in range(0,n):
			str+=("%s%s") % (Fraction(matrix[i][j]).limit_denominator(), spaces)
		print(str)
		for k in range(0,l):
			print(" ")
	return "Complete"

def line(n=1):
	#Prints n blank lines.
	for i in range(0,n):
		print(" ")
	return "Complete"
	
def cutLeftSquare(matrix):
	#Cuts a non square matrix into a square, focused on the upper left side, by removing rows or columns from the bottom or right as needed.
	m,n=len(matrix),len(matrix[0])
	output=[]
	if (m>n): #If there are too many rows, just recreate the matrix with fewer.
		for i in range (0,n):
			output.append(matrix[i])
	else: #Otherwise, iterate through each row and only allow the proper number of values in
		for i in range(0,m):
			row=[]
			for j in range(0,m):
				row.append(matrix[i][j])
			output.append(row)
	return output
	
def cutRightSquare(matrix):
	#Cuts a non square matrix into a square, focused on the upper right side, by removing rows or columns from the bottom or left as needed.
	m,n=len(matrix),len(matrix[0])
	output=[]
	if (m>n): #If there are too many rows, just recreate the matrix with fewer.
		for i in range (0,n):
			output.append(matrix[i])
	else: #Otherwise, iterate through each row and only allow the proper values in.
		for i in range(0,m):
			row=[]
			for j in range(n-m,m+1): #Make sure to iterate only on right-side values.
				row.append(matrix[i][j])
			output.append(row)
	return output
	
#def rrefInverse(matrix):
	#Returns the inverse of a matrix.
	#Uses Gauss-Jordan RREF method for such calculation -- NOT YET WORKING
	#if (det(matrix)==0 or len(matrix)!=len(matrix[0])):
		#return("Matrix must be invertible.")
	#return cutRightSquare(rref(hAppend(matrix,identityMatrix(len(matrix)))))

def cofactor(matrix):
	#Returns the cofactor matrix associated with the given matrix.
	m,n=len(matrix),len(matrix[0])
	if (m!=n):
		return("Matrix must be square.")
	output = zeroMatrix(m) #Initialize the output matrix
	for i in range(0,m): #iterate through all rows
		for j in range(0,n): #iterate through all entries in a row
			subMtx = [] #Initialize the associated submatrix for each entry
			for r in range(0,m):
				if (r!=i):
					subRow=[]
					for c in range(0,n):
						if (c!=j): #Append the proper entries to the submatrix
							subRow.append(matrix[r][c])
					subMtx.append(subRow)
			output[i][j]=((-1)**(i+j) * det(subMtx)) #Calculate the minor and then the cofactor for the entry
	return output
		
def adjugate(matrix):
	#Returns the adjugate (adjoint) matrix associated with the given matrix, which is the transpose of the associated cofactor matrix.
	return transpose(cofactor(matrix))

def inverse(matrix):
	#Returns the inverse of a matrix, calculated using the determinant and adjugate of that matrix.
	return scale(adjugate(matrix),1/det(matrix))

def invSystem(A, x, b, rat=1000):
	#Calculates the solutions to the system Ax=b, using the method of inverse multiplication.
	#Returns a list, beginning with the solution matrix, followed by a series of strings expressing these solutions.
	#Only works on square systems, where there are as many coefficients in a row of A as there are unknowns in x.
	#A should be an mxm matrix. x and b both should be mx1 column vectors in matrix format.
	#A should be the matrix of coefficients, as numerical values. x should be the vector of unknowns, as string values. b should be the vector of constants, as numerical values.
	output = [] #Initialize the output list
	if not(len(A)==len(A[0])==len(x)==len(b)): #Confirms compatiblity
		output.append("Matrices are not of compatible sizes.")
	else:
		m=len(x)
		solMtx = multiplyMatrices(inverse(A), b) #Perform the actual calculation
		output.append(solMtx) #Primary element of list inserted
		strList = []
		#Will provide the solution strings in rational fraction format, unless passed a 'rat' value of 0.
		for i in range(0,m): #Iterates through each unknown
			if(rat != 0):
				st = "%s = %s" % (x[i][0], Fraction(solMtx[i][0]).limit_denominator(rat)) #Creates readable string in rational fraction form for the solution to this unknown
			else:
				st = "%s = %s" % (x[i][0], solMtx[i][0]) #Creates readable string for the solution to this unknown
			strList.append(st) #Appends this solution string into the list
		output.append(strList) #Appends the solution string list into the output
	return output

def solutionPrint(solutions):
	#Prints the solutions to a system of equations generated by another function in a readable way.
	m = len(solutions[1])
	for i in range(0,m):
		print(solutions[1][i])
	return("Complete")

def sysSign(num):
	if(num >= 0):
		return "+"
	elif(num < 0):
		return "-"
	else:
		return ""

def unityElim(num):
	if(num == 1):
		return ""
	else:
		return num

def inputSystem(rat=1000, suppress=0, readback=0):
	#Accepts input for a much more user-friendly method of solving a system of linear equations.
	print("How many unknowns?")
	m=int(input())
	x=zeroMatrix(m,1)
	for i in range(0,m):
		print("What is the unknown at index %d?" % (i))
		x[i][0]=input()
	print("When inputting coefficients separate them with spaces. For example, input 4x+3y=9 as '4 3 9'.")
	A=zeroMatrix(m)
	b=zeroMatrix(m,1)
	for j in range(0,m):
		print("What are the coefficients in the equation of index %d?" % (j))
		B=input().split()
		if (len(B)!=(m+1)):
			print ("Program failure: Incorrect number of coefficients entered.")
			return ("Failed.")
		for k in range(0,m+1):
			if (k==m):
				b[j][0] = int(B[k])
			else:
				A[j][k] = int(B[k])
	if (readback==1):
		line()
		print("Your input:")
		for row in range(0,m):
			equ = ""
			for val in range(0,m+1):
				if (val==m):
					equ += ("= %d" % (b[row][0]))
				elif (val == 0):
					equ += ("%s%s " % (unityElim(A[row][val]), x[val][0]))
				else:
					equ += ("%s %s%s " % (sysSign(A[row][val]),unityElim(abs(A[row][val])), x[val][0]))
			print(equ)
	if (det(A)==0):
		print("System dependent - method failed.")
		return("Failed.")
	output = invSystem(A,x,b,rat)
	if (suppress == 0):
		line()
		print("Solution:")
		solutionPrint(output)
		line()
		input("Press return to exit.")
	return(output)
