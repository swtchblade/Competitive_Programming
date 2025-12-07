class DSU:
	def __init__(self,n): self.p = list(range(n)); self.s = [1]*n
	def get(self,x):
		if self.p[x] == x:return x
		self.p[x] = self.get(self.p[x])
		return self.p[x]
	def uni(self,x,y):
		xr, yr = self.get(x),self.get(y)
		if xr == yr:return False
		if self.s[xr] < self.s[yr]:xr, yr = yr, xr
		self.p[yr] = xr; self.s[xr] += self.s[yr]
		return True
	def same(self,x,y):return self.get(x) == self.get(y)
