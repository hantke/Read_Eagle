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

def Correct_Bounds_mdx(dx,L = 100):#Module of dx in a periodic box
	dx[dx < L/2.] = L-dx
	return dx
def Center(A,M,L):
	if M == []: M = np.zeros(len(A))+1
	if A[0] < L/10.:
		A[A > 9*L/10.] = L-A[A > 9*L/10.]
	elif A[0] > 9*L/10.:
		A[A < L/10.] = L+A[A < L/10.]
	return A*M/np.sum(M)
		


def Shell(Pos, Mpart, Rad, L,NBin):
	dx = []
	Arr = np.zeros(NBin)
	for i in range(3):
		sgr_Cen = Center(Pos[:,i],Mpart,L)
		dx_tmp = abs(Pos[:,i]-sgr_Cen)
		dx.append(Correct_Bounds_mdx(dx_tmp,L = L))
	dx = np.array(dx)
	Dist  = (dx[:,0]**2+dx[:,1]**2+dx[:,2]**2)**0.5
	iDist = (Dist/Rad*NBin).astype(int)
	IDs = np.where((iDist >= 0) & (iDist < NBin))[0]
	for ID in IDs: 	Arr[ID] += Mpart[ID]
	for i in range(len(Arr)-1): Arr[-1-i:] += Arr[-2-i]
	return Arr
