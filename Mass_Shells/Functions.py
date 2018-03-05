 ################################ Package ##################################################
import numpy as np

################################ Modules ##################################################

def Get_PartIndexRange(GroupID,SubGroupID,NumOfSubhalos):
	Len = len(GroupID)#Carefull point 0
	LGroup = len(NumOfSubhalos)
	MaxSubGroup = max(NumOfSubhalos)
	Range_id = []
	for i in range(LGroup):	Range_id.append(np.zeros((NumOfSubhalos[i],2),dtype=int))
	Last_Group = GroupID[0]
	Last_SubGroup = SubGroupID[0]
	for i in range(1,Len):
		if  SubGroupID[i] > MaxSubGroup:
			pass
		elif i == Len-1:
			Range_id[Last_Group-1][Last_SubGroup][1]=i
		elif GroupID[i] != Last_Group or SubGroupID[i] != Last_SubGroup:
			Range_id[Last_Group-1][Last_SubGroup][1]=i
			Range_id[GroupID[i]-1][SubGroupID[i]][0]=i
			Last_Group = GroupID[i]
			Last_SubGroup = SubGroupID[i]
	return Range_id

def Get_SubHaloCenter(GroupID,SubGroupID,NumOfSubhalos, SHCenter):
	LSubGroup = len(GroupID)#Carefull point 0
	LGroup = len(NumOfSubhalos)
	CenterOfPotential = []
	for i in range(LGroup):	CenterOfPotential.append(np.zeros((NumOfSubhalos[i],3),dtype=float))
	for i in range(LSubGroup):
		if  GroupID[i] >= LGroup or SubGroupID[i] >= NumOfSubhalos[GroupID[i]]:	pass
		else:
			CenterOfPotential[GroupID[i]-1][SubGroupID[i]]  =  SHCenter[i]
	return CenterOfPotential

def Correct_Bounds_mdx(dx,L = 100):#Module of dx in a periodic box
	dx[dx > L/2.] = L-dx[dx > L/2.]
	return dx
def Center(A,M,L):
	if M == []: M = np.zeros(len(A))+1
	if A[0] < L/10.:
		A[A > 9*L/10.] = L-A[A > 9*L/10.]
	elif A[0] > 9*L/10.:
		A[A < L/10.] = L+A[A < L/10.]
	return np.sum(A*M)/np.sum(M)
		


def Shell(Pos, Mpart, Rad, L,NBin, CenterOfPotential = []):
	dx = []
	Arr = np.zeros(NBin)
	for i in range(3):
		if len(CenterOfPotential) == 0: sgr_Cen = Center(Pos[:,i],Mpart,L)
		else: sgr_Cen = CenterOfPotential
		dx_tmp = abs(Pos[:,i]-sgr_Cen[i])
		dx.append(Correct_Bounds_mdx(dx_tmp,L = L))
	dx = np.array(dx)
	Dist  = (dx[0,:]**2+dx[1,:]**2+dx[2,:]**2)**0.5
	iDist = (Dist/Rad*NBin).astype(int)
	IDs = np.where((iDist >= 0) & (iDist < NBin))[0]
	for ID in IDs: 	Arr[iDist[ID]] += Mpart[ID]
	#for i in range(len(Arr)-1): Arr[-1-i:] += Arr[-2-i]
	return Arr

def Find_AinB(A, B):# Only if A is complete in B
	a=0
	b=0
	index = []
	while( a<len(A)):
	if (A[a] < B[b]) or (len(B)<b):
		print 'warning', a, b, A[a], B[b]
		return -1
	#if b%1000000==0: print a, b, A[a], B[b]
	if A[a]== B[b]:
		index.append(b)
		a+=1
	b+=1
	
def Most_Bound_Part(sh_IDs,sh_Pos,part_IDs,part_Pot):
	ind1 = np.argsort(sh_IDs)
	sh_IDs = sh_IDs[ind1]
	sh_Pos = sh_Pos[ind1]
	
	ind2 = Find_AinB(sh_IDs, part_IDs)
	tmp_part_Pot = part_Pot[ind2]
	
	ind3 = np.argsort(tmp_part_Pot)
	return sh_Pos[ind3[0]]
