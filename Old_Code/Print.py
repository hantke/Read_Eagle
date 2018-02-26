####################### Package ############################
from random 			 import random as rand
import Mate as M
######################## Functions #########################
def Print_Idit_GroupV1(GroupID_DM,M_Group,Cen_Group,Vel_Group,Vmean_DM,Vdisp_DM,Vmean_Full,Vdisp_Full,Particle_ID_DM,FileName):
	File= open(FileName,'w')
	print >>File,'#GroupID','GroupMass','Cen_x','Cen_y','Cen_z','<Vel_x>','<Vel_y>','<Vel_z>','<Vel_x(DM)>','<Vel_y(DM)>','<Vel_z(DM)>','<V2_DM>','<Vel_x(DM+Stars)>','<Vel_y(DM+Stars)>','<Vel_z(DM+Stars)>','<V2_(DM+Stars)>','DM_Particles'
	for i in range(len(GroupID_DM)):
		print >>File,GroupID_DM[i],M_Group[GroupID_DM[i]-1],Cen_Group[GroupID_DM[i]-1][0],Cen_Group[GroupID_DM[i]-1][1],Cen_Group[GroupID_DM[i]-1][2],Vel_Group[GroupID_DM[i]-1][0],Vel_Group[GroupID_DM[i]-1][1],Vel_Group[GroupID_DM[i]-1][2],Vmean_DM[i][0],Vmean_DM[i][1],Vmean_DM[i][2],Vdisp_DM[i],Vmean_Full[i][0],Vmean_Full[i][1],Vmean_Full[i][2],Vdisp_Full[i],len(Particle_ID_DM[i])
	File.close()
	print 'Write '+FileName
	
def Print_Idit_GroupV2(GroupID_DM,M_Group,Cen_Group,Vel_Group,Vmean_DM,Vdisp_DM,Vmean_Full,Vdisp_Full,Particle_ID_DM,R_Group,CenM_Group,Nsub_Group,FileName):
	File= open(FileName,'w')
	print >>File,String_Info_Group()
	print >>File,'#GroupID','M200_Crit','R200_Crit','CoP_x','CoP_y','CoP_z','CoM_x','CoM_y','CoM_z','<Vel_x>','<Vel_y>','<Vel_z>','<Vel_x(DM)>','<Vel_y(DM)>','<Vel_z(DM)>','<V2_DM>','<Vel_x(DM+Stars)>','<Vel_y(DM+Stars)>','<Vel_z(DM+Stars)>','<V2_(DM+Stars)>','Nsub_Group','DM_Particles'
	for i in range(len(GroupID_DM)):
		print >>File,GroupID_DM[i],M_Group[GroupID_DM[i]-1],R_Group[GroupID_DM[i]-1],Cen_Group[GroupID_DM[i]-1][0],Cen_Group[GroupID_DM[i]-1][1],Cen_Group[GroupID_DM[i]-1][2],CenM_Group[GroupID_DM[i]-1][0],CenM_Group[GroupID_DM[i]-1][1],CenM_Group[GroupID_DM[i]-1][2],Vel_Group[GroupID_DM[i]-1][0],Vel_Group[GroupID_DM[i]-1][1],Vel_Group[GroupID_DM[i]-1][2],Vmean_DM[i][0],Vmean_DM[i][1],Vmean_DM[i][2],Vdisp_DM[i],Vmean_Full[i][0],Vmean_Full[i][1],Vmean_Full[i][2],Vdisp_Full[i],Nsub_Group[GroupID_DM[i]-1],len(Particle_ID_DM[i])
	File.close()
	print 'Write '+FileName
		
	
def Print_Idit_SubGroupV1(GroupID_SH,SubGroupID_SH,StellMass030_SH,Cen_SH,Vel_SH,M_Group,Vmean_St_030,Xmean_St_030,ShIndex_St,FileName):
	File= open(FileName,'w')
	print >>File,String_Info_Subhalo()
	print >>File,'#GroupID','SubGroupID','M200_Crit','StellMass030_SH','CoP_x','CoP_y','CoP_z','Vel_x','Vel_y','Vel_z','Vel_x(St030)','Vel_y(St030)','Vel_z(St030)','CoP_x(St030)','CoP_y(St030)','CoP_z(St030)','N_SubHalo_Sel'
	for i in range(len(ShIndex_St)):
		for j in range(len(ShIndex_St[i])):
			d = ShIndex_St[i][j]
			#print GroupID_SH[d],SubGroupID_SH[d],M_Group[GroupID_SH[d]-1],StellMass030_SH[d],Cen_SH[d][0],Cen_SH[d][1],Cen_SH[d][2],Vel_SH[d][0],Vel_SH[d][1],Vel_SH[d][2],Vmean_St_030[i][j][0],Vmean_St_030[i][j][1],Vmean_St_030[i][j][2]
			print >>File,GroupID_SH[d],SubGroupID_SH[d],M_Group[GroupID_SH[d]-1],StellMass030_SH[d],Cen_SH[d][0],Cen_SH[d][1],Cen_SH[d][2],Vel_SH[d][0],Vel_SH[d][1],Vel_SH[d][2],Vmean_St_030[i][j][0],Vmean_St_030[i][j][1],Vmean_St_030[i][j][2],Xmean_St_030[i][j][0],Xmean_St_030[i][j][1],Xmean_St_030[i][j][2],len(ShIndex_St[i])

def Print_Idit_OnlyDMV1(GroupID_DM,M_Group,Cen_Group,Vmean_DM,Vdisp_DM,Vcore_Array,Ncore_Array,Particle_ID_DM,Vmean2_DM,FileName):
	File= open(FileName,'w')
	print >>File,String_Info_OnlyDM()
	print >>File,'#GroupID','M200_Crit','CoP_x','CoP_y','CoP_z','<Vel_x>','<Vel_y>','<Vel_z>','<Vel2_x>','<Vel2_y>','<Vel2_z>','<v2>','N_Particle','v,n for 10 radius'
	for i in range(len(GroupID_DM)):
		print >>File,GroupID_DM[i],M_Group[GroupID_DM[i]-1],Cen_Group[GroupID_DM[i]-1][0],Cen_Group[GroupID_DM[i]-1][1],Cen_Group[GroupID_DM[i]-1][2],Vmean_DM[i][0],Vmean_DM[i][1],Vmean_DM[i][2],Vmean2_DM[GroupID_DM[i]-1][0],Vmean2_DM[GroupID_DM[i]-1][1],Vmean2_DM[GroupID_DM[i]-1][2],Vdisp_DM[i],len(Particle_ID_DM[i]),M.Join_String2(Vcore_Array[:,i]),M.Join_String(Ncore_Array[:,i])


def String_Info_Group():
	Str = ''
	Str += '#\n'
	Str += '#(1) GroupID: ID of the FOF.\n'
	Str += '#(2) M200_Crit: Mass within Rcrit200. (Msun) \n'
	Str += '#(3) R200_Crit: Radius within which density is 200 times critical density. (Mpc)\n'
	Str += '#(4,5,6) CoP_x,y,z: Position of the center of potential. (Mpc)\n'
	Str += '#(7,8,9) CoM_x,y,z: Position of the center of mass. (Mpc)\n'
	Str += '#(10,11,12) <Vel_x,y,z>: Velocity given by Eagle. (Km/s)\n'
	Str += '#(13,14,15) <Vel_x,y,z(DM)>: Velocity for dark matter particles. (Km/s)\n'
	Str += '#(16) <V2_DM>: Mean of the velocity square for dark matter particles. (Km/s)^2\n'
	Str += '#(17,18,19) <Vel_x,y,z(DM+Stars)>: Mean weight Velocity for dark matter+Stellar particles. (Km/s)\n'
	Str += '#(20) <V2_(DM+Stars)>: Mean weight of the velocity square for dark matter+Stellar particles. (Km/s)^2\n'
	Str += '#(21) Nsub_Group: Number of Subhaloes (All of them). \n'
	Str += '#(22) DM_Particles: Number of dark matter particles.'
	return Str
def String_Info_Subhalo():
	Str = ''
	Str += '#\n'
	Str += '#(1) GroupID: ID of the FOF.\n'
	Str += '#(2) SubGroupID: ID of the Subhalo (0 the first subhalo of each FOF). \n'
	Str += '#(3) M200_Crit: Mass within Rcrit200. (Msun) \n'
	Str += '#(4) StellMass030_SH: Total stellar mass in a radius of 30 kpc. (Msun)\n'
	Str += '#(5,6,7) CoP_x,y,z: Position of the center of potential. (Mpc)\n'
	Str += '#(8,9,10) <Vel_x,y,z>: Velocity given by Eagle. (Km/s)\n'
	Str += '#(11,12,13) <Vel_x,y,z(St030)>: Velocity stars in a radius of 30 kpc (Km/s)\n'
	Str += '#(14,15,16) <CoM_x,y,z(St030)>: Mass Center stars in a radius of 30 kpc (Km/s)\n'
	Str += '#(17) N_SubHalo_Sel: Number of subhaloes with stellar mass'
	#GroupID','SubGroupID','M200_Crit','StellMass030_SH','CoP_x','CoP_y','CoP_z','Vel_x','Vel_y','Vel_z','Vel_x(St030)','Vel_y(St030)','Vel_z(St030)','CoP_x(St030)','CoP_y(St030)','CoP_z(St030)','N_SubHalo_Sel'
	return Str

def String_Info_OnlyDM():
	Str = ''
	Str += '#\n'
	Str += '#(1) GroupID: ID of the FOF.\n'
	Str += '#(2) M200_Crit: Mass within Rcrit200. (Msun)\n'
	Str += '#(3,4,5) CoP_x,y,z: Position of the center of potential. (Mpc)\n'
	Str += '#(6,7,8) <Vel_x,y,z>: Mean Velocity (Km/s)\n'
	Str += '#(9,10,11) <Vel2_x,y,z>: Velocity given by Eagle. (Km/s)\n'
	Str += '#(12) <V2>: Mean squere velocity (Km/s)^2\n'
	Str += '#(13) N_Particle: Number of dark matter particles.\n'
	Str += '#(N) v,n for N radius: Velocity (x,y,z) and number of particles for different radius as define in Database.py'
	#GroupID','M_Group','CoP_x','CoP_y','CoP_z','<Vel_x>','<Vel_y>','<Vel_z>','<v2>','N_Particle','v,n for N radius'
	return Str
	
	
##################################################################################################################################################


	