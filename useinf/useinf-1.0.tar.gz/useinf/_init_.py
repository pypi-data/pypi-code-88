def convint(num, base):
	if base < 2 or base > 9:
		return 0
	newNum = ''

	while num > 0:
		newNum = str(num % base) + newNum
		num //= base
	return newNum

def getDevs(num):
	a = []
	for i in range(2, num):
		if num % i == 0:
			a.append(i)
	return a

def doUsers(s, n, a):
	for i in range(len(a)):
		a[i] = int(a[i])
	
	a.sort()
	
	sum = 0
	maxi = 1
	
	for i in range(n):
		if sum + a[i] <= s:
			sum += a[i]
			maxi = i
	
	t = a[maxi]
	
	for i in range(maxi, n):
		if ((sum - t) + a[i]) <= s:
			sum = sum - t + a[i]
			t = a[i]
	return str(maxi + 1) + ' ' + str(t)

def doGoods(s, n, p, f):
	sum = 0
	a = []
	for i in f.readlines():
		if int(i) <= s:
			sum += int(i)
		else:
			a.append(int(i))
	a.sort()
	
	for i in range(len(a) - 1):
		if i <= (len(a) - 1) // n:
			sum = sum + a[i]*(1 - p)
			maxPrice = round(a[i])
		else:
			sum = sum + a[i]
	return str(round(sum+0.5) + 999) + ' ' + str(maxPrice)

def oneChar(s, char):
	maxLen = 1
	curLen = 1
	for i in range(len(s) - 1):
		if s[i] == s[i - 1] and s[i] == char:
			curLen += 1
			if curLen > maxLen:
				maxLen = curLen
		else:
			curLen = 1
	return maxLen

def rangeChars(s, chars):
	count = 0
	maxCount = 0
	for i in range(len(s)):
		if(s[i] == chars[0] and count % 3 == 0) or (s[i] == chars[1] and count % 3 == 1) or (s[i] == chars[2] and count % 3 == 2):
			count += 1
			if count > maxCount:
				maxCount = count
		elif s[i] == chars[0]:
			count = 1
		else:
			count = 0
	return maxCount
