################################################ Package ##################################################
#Main Libs
from numpy import *
import numpy as np
#Internal libs
import Mate as M
import Database as D
######################## Functions #########################

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
	#Last_id
	

def Get_PartGroupID(num,ID):#Num are the GroupID of the particles to be located in the ID 
	count = 0#Count Particles per Halo or Subhalo
	Last_Status = M.Locate_Partner(num[0],ID,0,len(ID)-1) >=0#First Particle is in a select Group? (True or False)
	Last_Gid = num[0] #Group ID of the first Particle
	##
	Particle_ID = []
	tmp_Particle_ID = []
	GroupID = []
	Len = len(num)
	##
	for i in range(Len):#We go in all the particle GroupID (Gid)
		Gid = num[i]
		#if i % (Len/1000) == 0:	print '...',i/float(Len)*100,'% ...' #Just to count, no necesary!
		if Last_Gid == Gid and Last_Status:#Is also part of an acepted Halo
			tmp_Particle_ID.append(i)
		elif Last_Gid != Gid:#New Halo TODO Read last halo!
			if Last_Status:#If Last Halo was acepted
				Particle_ID.append(tmp_Particle_ID)
				GroupID.append(Last_Gid)
			tmp_Particle_ID = []
			Last_Gid = Gid
			Last_Status = M.Locate_Partner(Gid,ID,0,len(ID)-1) >=0
	return array(GroupID),array(Particle_ID)

def Get_PartGroupID2(Gnum,SHnum,ID,GroupID_SH,SubGroupID_SH):#Num are the GroupID of the particles to be located in the ID 
	count = 0#Count Particles per Halo or Subhalo
	Last_Status = M.Locate_Partner(Gnum[0],ID,0,len(ID)-1) >=0#First Particle is in a select Group? (True or False)
	Last_Gid = Gnum[0] #Group ID of the first Particle
	Last_SHid = SHnum[0] #Group ID of the first Particle
	##
	
	tmp_Particle_ID = []
	Particle_ID = [[]]
	GroupID = []
	SHID = [[]]
	SHIndex = [[]]
	
	Group_Index = 0
	SH_Index = 0
	
	Len = len(Gnum)
	##
	for i in range(Len):#We go in all the particle GroupID (Gid)
		Gid = Gnum[i]
		SHid = SHnum[i]
		
		#if i % (Len/1000) == 0:	print '...',i/float(Len)*100,'% ...' #Just to count, no necesary!
		if Last_Gid == Gid and Last_SHid == SHid and Last_Status:#Is also part of an acepted Halo
			tmp_Particle_ID.append(i)
		elif Last_Gid != Gid or Last_SHid != SHid:#New Halo TODO Read last halo!
			if Last_Status:#If Last Halo was acepted
				#print '# ',len(Particle_ID),len(Particle_ID[0]),SH_Index,Group_Index
				#if TODO  #len(tmp_Particle_ID) > 100
				Particle_ID[Group_Index].append(tmp_Particle_ID)
				SHID[Group_Index].append(Last_SHid)
				if Last_SHid < 1e9:	SHIndex[Group_Index].append(where((GroupID_SH == Last_Gid) & (SubGroupID_SH == Last_SHid)  )[0][0])
				else:	SHIndex[Group_Index].append(-99)
				if Last_Gid != Gid:
					Particle_ID.append([])
					SHID.append([])
					SHIndex.append([])
					GroupID.append(Last_Gid)
					Group_Index += 1
			tmp_Particle_ID = []
			tmp_Particle_ID.append(i)
			Last_Gid = Gid
			Last_SHid = SHid
			Last_Status = M.Locate_Partner(Gid,ID,0,len(ID)-1) >=0
	return array(GroupID),array(SHID),array(Particle_ID),array(SHIndex)


def Get_AngularMomentum(Particle_ID,pos,vel):
	J = []
	Len = len(Particle_ID)
	for gr in range(Len):
		#if gr % (Len/1000) == 0:	print 'J Calculated...',gr/float(Len)*100,'% ...' #Just to count, no necesary!
		#tmp_vel = transpose(vel[Particle_ID[gr]])
		#tmp_pos = transpose(pos[Particle_ID[gr]])
		J.append(M.Angular_Momentum2(pos[Particle_ID[gr]],vel[Particle_ID[gr]],1))
	return J

def Get_AngularMomentum_Rad(Particle_ID,pos,vel,center,R,GroupID_DM,MassPart = D.DM_Mass,Lbox = D.LBOX):
	J = []
	Len = len(Particle_ID)
	Mass = []
	NP = []
	for gr in range(Len):
		tmp_pos = pos[Particle_ID[gr]]
		if len(tmp_pos[:,0]) != 0: 
			tmp_pos[:,0] = Correct_Bounds(tmp_pos[:,0],L=D.LBOX,crit = 0.2)
			tmp_pos[:,1] = Correct_Bounds(tmp_pos[:,1],L=D.LBOX,crit = 0.2)
			tmp_pos[:,2] = Correct_Bounds(tmp_pos[:,2],L=D.LBOX,crit = 0.2)
			ID = where(DisBox(tmp_pos[:,0],center[GroupID_DM[gr]-1][0],Lbox)**2+DisBox(tmp_pos[:,1],center[GroupID_DM[gr]-1][1],Lbox)**2+DisBox(tmp_pos[:,2],center[GroupID_DM[gr]-1][2],Lbox)**2 < R[GroupID_DM[gr]-1]**2)#0.0009Mpc**2 == 30 Kpc**2 
			#print gr,R[GroupID_DM[gr]-1]**2,DisBox(tmp_pos[:,0],center[GroupID_DM[gr]-1][0],Lbox)**2+DisBox(tmp_pos[:,1],center[GroupID_DM[gr]-1][1],Lbox)**2+DisBox(tmp_pos[:,2],center[GroupID_DM[gr]-1][2],Lbox)**2
			if len(ID[0]) > 1:
				J.append(M.Angular_Momentum2(tmp_pos[ID],vel[Particle_ID[gr]][ID],MassPart[Particle_ID[gr]][ID]))
				Mass.append(np.sum(MassPart[Particle_ID[gr]][ID]))
				NP.append(len(MassPart[Particle_ID[gr]][ID]))
			else:
				J.append([1e-20,1e-20,1e-20])
				Mass.append(1e-20)
				NP.append(0)
		else:
			J.append([1e-20,1e-20,1e-20])
			Mass.append(1e-20)
			NP.append(0)
	return J,Mass,NP
def Get_AngularMomentum2(Particle_ID,pos,vel,MassPart = D.DM_Mass):
	J = [] 
	Len = len(Particle_ID)
	for gr in range(Len): 
		#if gr % (Len/1000) == 0:	print 'J Calculated...',gr/float(Len)*100,'% ...' #Just to count, no necesary!
		#tmp_vel = transpose(vel[Particle_ID[gr]])
		tmp_pos = pos[Particle_ID[gr]]
		tmp_pos[:,0] = Correct_Bounds(tmp_pos[:,0],L=D.LBOX,crit = 0.2)
		tmp_pos[:,1] = Correct_Bounds(tmp_pos[:,1],L=D.LBOX,crit = 0.2)
		tmp_pos[:,2] = Correct_Bounds(tmp_pos[:,2],L=D.LBOX,crit = 0.2)
		J.append(M.Angular_Momentum2(tmp_pos,vel[Particle_ID[gr]],MassPart))
	return J
def Get_AngularMomentum2_MP(Particle_ID,pos,vel,MassPart = D.DM_Mass):
	J = [] 
	Len = len(Particle_ID)
	for gr in range(Len): 
		#if gr % (Len/1000) == 0:	print 'J Calculated...',gr/float(Len)*100,'% ...' #Just to count, no necesary!
		#tmp_vel = transpose(vel[Particle_ID[gr]])
		tmp_pos = pos[Particle_ID[gr]]
		if len(tmp_pos[:,0]) != 0:
			tmp_pos[:,0] = Correct_Bounds(tmp_pos[:,0],L=D.LBOX,crit = 0.2)
			tmp_pos[:,1] = Correct_Bounds(tmp_pos[:,1],L=D.LBOX,crit = 0.2)
			tmp_pos[:,2] = Correct_Bounds(tmp_pos[:,2],L=D.LBOX,crit = 0.2)
			J.append(M.Angular_Momentum2(tmp_pos,vel[Particle_ID[gr]],MassPart[Particle_ID[gr]]))
		else:
			J.append([1e-20,1e-20,1e-20])
	return J
def Get_Vdisp(Particle_ID,v,m = False):
	Vd = []
	if isinstance(m,bool) and m == False:
		for gr in range(Len): 
			#if gr % (Len/100) == 0:	print 'J Calculated...',int(gr/float(Len)*100.01),'% ...' #Just to count, no necesary!
			Vd.append(Vdisp(v[Particle_ID[gr]]))
	else:
		for gr in range(Len): 
			#if gr % (Len/100) == 0:	print 'J Calculated...',int(gr/float(Len)*100.01),'% ...' #Just to count, no necesary!
			Vd.append(Vdisp(v[Particle_ID[gr]],m[Particle_ID[gr]]))
	return array(Vd)
def Get_Vanaly2(Particle_ID_DM,vel_DM,Particle_ID_Star,vel_Star,mass_Star):
	Vd = []
	Vm = []
	Len = len(Particle_ID_DM)
	vel_DM,Particle_ID_Star,vel_Star,mass_Star = [asarray(a) for a in vel_DM,Particle_ID_Star,vel_Star,mass_Star]
	for gr in range(Len): 
		#if gr % (Len/100) == 0:	print 'Get Velocity 2 ...',int(gr/float(Len)*100.01),'% ...' #Just to count, no necesary!
		Sel_mass_DM = zeros(len(Particle_ID_DM[gr]))+D.DM_Mass
		Sel_vel_DM = vel_DM[Particle_ID_DM[gr]]
	
		Sel_mass_Star = mass_Star[Particle_ID_Star[gr]]
		Sel_vel_Star = vel_Star[Particle_ID_Star[gr]]
	
		Mass = concatenate((Sel_mass_DM,Sel_mass_Star), axis=0)
		Vel = concatenate((Sel_vel_DM,Sel_vel_Star), axis=0)
		Vd.append(V2(Vel,Mass))
		Vm.append(Avg_Vel(Vel,Mass))
	return array(Vm),array(Vd)
def Get_Vanaly(Particle_ID,v,m):
	Vd = []
	Vm = []
	Len = len(Particle_ID)
	#v, m = [asarray(a) for a in v, m]
	if isinstance(m,bool) and m == False:
		for gr in range(Len): 
			#if gr % (Len/100) == 0:	print 'Get Velocity...',int(gr/float(Len)*100.01),'% ...' #Just to count, no necesary!
			v_tmp = v[Particle_ID[gr]]
			Vm.append(Avg_Vel(v_tmp,False))
			Vd.append(V2(v_tmp,False))
	else:
		for gr in range(Len): 
			#if gr % (Len/100) == 0:	print 'Get Velocity...',int(gr/float(Len)*100.01),'% ...' #Just to count, no necesary!
			v_tmp = v[Particle_ID[gr]]
			Vm.append(Avg_Vel(v_tmp,m))
			Vd.append(V2(v_tmp,m))
	return array(Vm),array(Vd)

def Get_Vmean(Particle_ID,v,m):
	Vm = []
	Len = len(Particle_ID)
	if isinstance(m,bool) and m == False:
		for gr in range(Len): 
			#if gr % (Len/100) == 0:	print 'J Calculated...',int(gr/float(Len)*100.01),'% ...' #Just to count, no necesary!
			Vm.append(Avg_Vel(v[Particle_ID[gr]],False))
	else:
		for gr in range(Len): 
			#if gr % (Len/100) == 0:	print 'J Calculated...',int(gr/float(Len)*100.01),'% ...' #Just to count, no necesary!
			Vm.append(Avg_Vel(v[Particle_ID[gr]],m[Particle_ID[gr]]))
	return array(Vm)	
def Avg_Vel(v,m):
	if isinstance(m,bool) and m == False:
		v = array(v)
		return M.Center(v[:,0],v[:,1],v[:,2])
	v, m = [asarray(a) for a in v, m]
	return M.Center(v[:,0],v[:,1],v[:,2],Mp = m,Same_MP = False)
def Correct_Bounds(X,L = 100,crit = 0.1):
	if M.Between2(X[0],L*crit,L*(1-crit)):	return X
	elif X[0] < L*crit:	Status = X[:] > L*(1-crit)
	else:	Status = X[:] < L*crit
	return (-1*Status*L + X[:])*(1-2*Status)
def Vdisp(v,m):
	if isinstance(m,bool) and m == False:
		v = array(v)
		av_Vx,av_Vy,av_Vz = Avg_Vel(v,False)
		av_V2x,av_V2y,av_V2z = Avg_Vel(v**2,False)
		
	else:
		v, m = [asarray(a) for a in v, m]
		av_Vx,av_Vy,av_Vz = Avg_Vel(v,m)
		av_V2x,av_V2y,av_V2z = Avg_Vel(v**2,m)
	return array([av_V2x-av_Vx**2,av_V2y-av_Vy**2,av_V2z-av_Vz**2])
def V2(v,m):
	if isinstance(m,bool) and m == False:
		v = array(v)
		v2 = v[:,0]**2+v[:,1]**2+v[:,2]**2
		v2_av = average(v2)
		
	else:
		v, m = [asarray(a) for a in v, m]
		v2 = v[:,0]**2+v[:,1]**2+v[:,2]**2
		v2_av = average(v2, weights=m)
	return v2_av

def DisBox_Old(a,b,L):
	d = abs(a-b)
	if d > L/2.:	return L-d
	return d
def DisBox(a,b,L):
	d = abs(a-b)
	Status = d > L/2.
	return L*(Status)+d*(1-2*Status)
def Vmean_030(Particle_ID,x,v,m,center,SH_ID,Lbox):
	Len = len(Particle_ID)
	vm = []
	for gr in range(Len):
		v_Tmp = v[Particle_ID[gr]]
		m_Tmp = m[Particle_ID[gr]]
		tmp_pos = x[Particle_ID[gr]]
		#dx = 
		ID = where(DisBox(tmp_pos[:,0],center[SH_ID[gr][0]],Lbox)**2+DisBox(tmp_pos[:,1],center[SH_ID[gr]][1],Lbox)**2+DisBox(tmp_pos[:,2],center[SH_ID[gr]][2],Lbox)**2 < 0.0009)#0.0009Mpc^3 == 30 Kpc**2 
		v_Tmp = v_Tmp[ID]
		m_Tmp = m_Tmp[ID]
		vm.append(Avg_Vel(v_Tmp,m_Tmp))
	return array(vm)

def Vmean_030v2(Particle_ID,x,v,m,center,SH_ID,Lbox):
	Len = len(Particle_ID)
	vm = []
	for gr in range(Len):
		v_Tmp = v[Particle_ID[gr]]
		m_Tmp = m[Particle_ID[gr]]
		tmp_pos = x[Particle_ID[gr]]
		#dx = 
		ID = where(DisBox(tmp_pos[:,0],center[SH_ID[gr][0]],Lbox)**2+DisBox(tmp_pos[:,1],center[SH_ID[gr]][1],Lbox)**2+DisBox(tmp_pos[:,2],center[SH_ID[gr]][2],Lbox)**2 < 0.0009)#0.0009Mpc^3 == 30 Kpc**2 
		v_Tmp = v_Tmp[ID]
		m_Tmp = m_Tmp[ID]
		vm.append(Avg_Vel(v_Tmp,m_Tmp))
	return array(vm)

def Vmean_030v3(x,v,m,center,SH_ID,Lbox):
	vm = []
	xm = []
	for gr in range(len(x)):
		vm.append([])
		xm.append([])
		for sh in range(len(x[gr])):
			v_Tmp = v[gr][sh]
			m_Tmp = m[gr][sh]
			x_Tmp = x[gr][sh]
			ID = where(DisBox(x_Tmp[:,0],center[SH_ID[gr][sh]][0],Lbox)**2+DisBox(x_Tmp[:,1],center[SH_ID[gr][sh]][1],Lbox)**2+DisBox(x_Tmp[:,2],center[SH_ID[gr][sh]][2],Lbox)**2 < 0.0009)#0.0009Mpc**2 == 30 Kpc**2 
			v_Tmp = v_Tmp[ID]
			m_Tmp = m_Tmp[ID]
			x_Tmp = x_Tmp[ID]
			if isinstance(v_Tmp,float):
				vm[gr].append(v_Tmp)
				xm[gr].append(v_Tmp)
			elif len(v_Tmp) == 0:
				vm[gr].append([0,0,0])
				xm[gr].append([0,0,0])
			elif len(v_Tmp) == 1:
				vm[gr].append(v_Tmp[0])
				xm[gr].append(x_Tmp[0])
			else:	
				vm[gr].append(Avg_Vel(v_Tmp,m_Tmp))
				xm[gr].append(Avg_Vel(x_Tmp,m_Tmp))#Avg_Vel aslo usefull for Position!
	return array(vm),array(xm)

def Vcore_Radius_DM(x,v,center,GroupID_DM,Particle_ID_DM,Radius,Lbox):#Radius in Kpc
	vm = []
	Npart = []
	R2 = (Radius/1000.)**2
	for gr in range(len(GroupID_DM)):
		v_Tmp = v[Particle_ID_DM[gr]]
		x_Tmp = x[Particle_ID_DM[gr]]
		ID = where(DisBox(x_Tmp[:,0],center[GroupID_DM[gr]-1][0],Lbox)**2+DisBox(x_Tmp[:,1],center[GroupID_DM[gr]-1][1],Lbox)**2+DisBox(x_Tmp[:,2],center[GroupID_DM[gr]-1][2],Lbox)**2 < R2)#0.0009Mpc**2 == 30 Kpc**2 
		v_Tmp = v_Tmp[ID]
		if isinstance(v_Tmp,float):	vm.append(v_Tmp)
		elif len(v_Tmp) == 0:	vm.append([0,0,0])
		elif len(v_Tmp) == 1:	vm.append(v_Tmp[0])
		else:	vm.append(Avg_Vel(v_Tmp,False))
		Npart.append(len(v_Tmp))
	return array(vm),array(Npart)
	
	
def IsEqual(a,b):
	Len = len(a)
	Status = True
	if len(b) != Len:	print '\nWARNING IN EQUAL! NO EQUAL!! Lens are:',Len,len(b),'\n\n'
	else:
		for i in range(Len):
			if a[i] != b[i]:	Status = False
		if Status:	print 'Are Equal the arrays!'
		else:	print '\nWARNING THE ARRAYS ARE NOT EQUAL!\n\n'
		
