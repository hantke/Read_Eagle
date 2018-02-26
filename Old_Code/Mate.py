####################### Package ############################
from random 			 import random as rand
import numpy as np
from numpy import sqrt
from scipy import integrate
from numpy import log10
######################## Functions Math #########################

def Histogram(Xmin,Xmax,NBin,X,Norm = False,dx = False):
	Axis = []
	Histo = []
	Add = 1
	if Norm:
		Sum = float(len(X))
		Add /= (Sum+1e-10)
	if dx:
		DX = (Xmax-Xmin)/float(NBin)
		Add /= (DX+1e-10)
	if len(X) < 2 or abs(Xmax-Xmin) < 1e-10:	return [],[]
	for i in range(NBin):	
		Histo.append(0)
		Axis.append(Xmin + i*(Xmax-Xmin)/float(NBin))
	for x in X:
		index = int(NBin*(x-Xmin)/(Xmax-Xmin))
		if index >= 0 and index < NBin:	Histo[index] += Add
	return Axis,Histo


def Bars(Xmin,Xmax,NBin,X,Y):
	Axis = []
	Data = []
	for i in range(NBin):	
		Data.append([])
		Axis.append(Xmin + (i+0.5)*(Xmax-Xmin)/float(NBin))
	for i in range(len(X)):
		index = int(NBin*(X[i]-Xmin)/(Xmax-Xmin))
		if index >= 0 and index < NBin:	Data[index].append(Y[i])
	for i in range(NBin):	Data[i].sort()
	Data2 = [[],[],[]]
	for i in range(NBin):	
		if len(Data[i]) > 4:
			Data2[1].append(Data[i][int(len(Data[i])/5.)])
			Data2[0].append(Data[i][int(len(Data[i])/2.)])
			Data2[2].append(Data[i][int(4.*len(Data[i])/5.)])
		else:
			Data2[1].append(-99)
			Data2[0].append(-99)
			Data2[2].append(-99)
	return Axis,Data2

def Int1(F,x1,x2,N):
	Sum = 0
	dx = (x2-x1)/float(N)
	for i in range(N):
		x = x1 + (i+0.5)*dx
		Sum += F(x)*dx
	return Sum
def Max(a,b):
	if a > b:	return a
	return b
def Min(a,b):
	if a > b:	return b
	return a
def AMax(A):
	MAX = -1e50
	for a in A:
		if a > MAX:	MAX = a
	return MAX
def AMin(A):
	MIN = 1e50
	for a in A:
		if a < MIN:	MIN = a
	return MIN
def AMinMax(A):
	MAX = -1e50
	MIN = 1e50
	for a in A:
		if a < MIN:	MIN = a
		if a > MAX:	MAX = a
	return MIN,MAX
def ANorm(A):
	MAX = AMax(A)
	for i in range(len(A)):
		A[i] /= float(MAX)
	return A
def AMedian(A):
	Len = len(A)
	if Len == 0:	return -99
	if Len == 1:	return A[0]
	A.sort()
	if Len % 2 == 1:	return A[int(Len/2)]
	return (A[int(Len/2)]+A[int(Len/2)-1])/2.
def Locate_Partner(x,Ytab,Ymin,Ymax):#Look for x in Y-Table, initial Ymin,Ymax = 0, len(Ytab-1)
	if Ymax - Ymin < 3:
		t = Ymin
		while t <= Ymax and t < len(Ytab):
			if x == Ytab[t]:	return t
			t += 1
		return -99	
	med = (Ymax+Ymin)/2
	if x < Ytab[med]:	return Locate_Partner(x,Ytab,Ymin,med)
	if x > Ytab[med]:	return Locate_Partner(x,Ytab,med,Ymax)
	return med
		
		
def Between(x,Xmin,Xmax):
	if x >= Xmin and x < Xmax:	return True
	return False
def Between2(x,Xmin,Xmax):
	if x >= Xmin and x <= Xmax:	return True
	return False
def Locate_Main_Des(x,Ytab1,Ytab2,Ymin,Ymax):#Look for x in Y-Table, initial Ymin,Ymax = 0, len(Ytab-1)
	if Ymax - Ymin < 4:
		t = Ymin
		while t <= Ymax and t < len(Ytab1):
			if Between2(x,Ytab1[t],Ytab2[t]):	return t
			t += 1
		return -99	
	med = (Ymax+Ymin)/2
	if x < Ytab2[med]:	return Locate_Main_Des(x,Ytab1,Ytab2,Ymin,med)
	if x > Ytab2[med]:	return Locate_Main_Des(x,Ytab1,Ytab2,med,Ymax)
	return med
		

def Line(x,X1,X2,Y1,Y2):
	m = (Y2-Y1)/(X2-X1)
	return Y1+m*(x-X1)

def Inv(Y,Ax,Ay):
	if len(Ax) != len(Ay) or len(Ax) < 2:
		print 'WARNING in M.Inv, len(X),len(Y)	', len(Ax), len(Ay) 
		return -99
	if Ay[0] >= Y:	return Line(Y,Ay[0],Ay[1],Ax[0],Ax[1])
	if Ay[-1] <= Y:	return Line(Y,Ay[-2],Ay[-1],Ax[-2],Ax[-1])
	for i in range(len(Ax)-1):
		if Y <= Ay[i+1]:	return Line(Y,Ay[i],Ay[i+1],Ax[i],Ax[i+1])
def Sup_Sort2(A,B,Rev = False):#minor to major
	a,b =zip(*sorted(zip(A,B)))
	if Rev:
		a1 = []
		b1 = []
		N = len(a)
		for i in range(1,N+1):
			a1.append(a[N-i])
			b1.append(b[N-i])
		return a1,b1	
	return a,b
	
def Sup_Sort3(A,B,C,Rev = False):
	a,b,c  =zip(*sorted(zip(A,B,C)))
	if Rev:
		a1 = []
		b1 = []
		c1 = []
		N = len(a)
		for i in range(1,N+1):
			a1.append(a[N-i])
			b1.append(b[N-i])
			c1.append(c[N-i])
		return a1,b1,c1	
	return a,b,c	
def is_Sort(A):
	for i in range(1,len(A)):
		if A[i-1] > A[i]:	return False
	return True
def Table(x,Ax,Ay):
	for i in range(1,len(Ax)):
		if x < Ax[i]:	return Line(x,Ax[i-1],Ax[i],Ay[i-1],Ay[i])
	return Line(x,Ax[-2],Ax[-1],Ay[-2],Ay[-1])
def N_Dist_PerBox(A,B,Box_Size = 500):
	Len = len(A)
	if len(B) != Len:
		print 'WARNING in M.N_Dist, len A,B',Len,len(B)
		return -99
	Sum = 0
	for i in range(Len):
		Dist = abs(A[i] - B[i])
		if Dist > Box_Size/2.:	Dist = Box_Size - Dist
		Sum += Dist**2
	return sqrt(Sum)
######################## Functions AstroPhysic #########################

def Dcosm_Disct(z,Ho,Om,Ol):
	c = 3e5
	return c/(Ho*sqrt(Om*(1+z)**3+Ol))

def Dcosm(z,Ho,Om,Ol):
	Sum = 0
	N = 100000
	dx = (z)/float(N)
	for i in range(N):
		x = (i+0.5)*dx
		Sum += Dcosm_Disct(x,Ho,Om,Ol)*dx
	return Sum
def Dist_Core(z,Ho,Om,Ol):	return 1./np.sqrt(Om*(1+z)**3+Ol)
def Dist(z,Ho,Om,Ol):
	Ho *= (3.24e-20) #1/s
	c    = 3e8  * (3.24e-17)#pc/s
	return c/Ho*integrate.quad(lambda z: Dist_Core(z,Ho,Om,Ol),0,z)[0]
def Dist_Lum(z,Ho,Om,Ol):	return Dist(z,Ho,Om,Ol)*(z+1)


def M2m(M,d):#Mpc (REVISAR EL FACTOR h)
	return M - 5*(1-log10(d))
def m2M(m,d):#Mpc (REVISAR EL FACTOR h)
	return m + 5*(1-log10(d))
def M2m2(M,d):#Mpc (REVISAR EL FACTOR h)
	return M - 5*(1-log10(d)-6)
def m2M2(m,d):#Mpc (REVISAR EL FACTOR h)
	return m + 5*(1-log10(d)-6)
#def Dcosm()

def Center(X,Y,Z,Mp = 1,Same_MP = True):
	if Same_MP:
		x0 = np.average(X, weights=None)	
		y0 = np.average(Y, weights=None)	
		z0 = np.average(Z, weights=None)	
	else:
		x0 = np.average(X, weights=Mp)	
		y0 = np.average(Y, weights=Mp)	
		z0 = np.average(Z, weights=Mp)	
	return x0,y0,z0
def Center2(v,m):
	 v, m = [np.asarray(a) for a in v, m]
	 Center(X,Y,Z,Mp = 1,Same_MP = True)

def Angular_Momentum2(rs,vs,ms):
    #"""Angular momentum per unit mass for a set of particles.""" ORIGINAL FROM https://pypi.python.org/pypi/gsn_numpy_util/0.1.0
    rs, vs, ms = [np.asarray(a) for a in rs, vs, ms]
    x0,y0,z0 =  Center(rs[:,0],rs[:,1],rs[:,2])
    rs[:,0] = rs[:,0] - x0
    rs[:,1] = rs[:,1] - y0
    rs[:,2] = rs[:,2] - z0
    return ((ms*np.cross(rs, vs).T).T).sum(axis=0)

def Angular_Momentum(X,Y,Z,Vx,Vy,Vz,Mp = 1,Same_MP = True):
	x0,y0,z0 =  Center(X,Y,Z,Mp = Mp,Same_MP = Same_MP)
	J = np.array([0,0,0])
	if Same_MP:
		for i in range(len(X)): 
			r = np.array([X[i]-x0,Y[i]-y0,Z[i]-z0])
			v = np.array([Vx[i],Vy[i],Vz[i]])
			J = J + np.cross(r,v)
		return J*Mp
	else:
		for i in range(len(X)):
			r = np.array([X[i]-x0,Y[i]-y0,Z[i]-z0])
			p = Mp[i]*np.array([Vx[i],Vy[i],Vz[i]])
			J = J + np.cross(r,p)
		return J

def Join_String(A):
	Str = ''
	for a in A:	Str += str(a)+'	'
	return Str

def Join_String2(A):
	Str = ''
	for a in A:	Str += Join_String(a)
	return Str
				
