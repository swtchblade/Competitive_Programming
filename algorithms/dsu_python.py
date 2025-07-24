class DSU:
	def __init__(self,n):
		self.p = list(range(n))
		self.s = [1]*n
	def find(self,x):
		if self.p[x] == x:return x
		self.p[x] = self.find(self.p[x])
		return self.p[x]
	def unite(self,x,y):
		xr = self.find(x)
		yr = self.find(y)
		if xr == yr:return False
		if self.s[xr] < self.s[yr]:xr, yr = yr, xr
		self.p[yr] = xr
		self.s[xr] += self.s[yr]
		return True
	def connected(self,x,y):return self.find(x) == self.find(y)
