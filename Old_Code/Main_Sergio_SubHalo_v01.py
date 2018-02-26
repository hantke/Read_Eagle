################################ Package ##################################################
#Main Libs
#Internal libs
import sys as s
import Database as D
Snap = int(s.argv[1])
D.Get_Sim(Snap)

import Print as P
import Read as R
import Mate as M
import Functions as F
from numpy import *#TODO ADD IN ALL F.
print "######################################################"
print "Starting the code!! Good Luck!!"
print "Package Load"
################################################ Pannel ################################################
print "Pannel load"
############################################### VARS ###################################################
print "Vars load"
Arr_Pos   = []
Arr_Vel   = []
Arr_Gnum  = []
############################################### Init ###################################################
print "Init"
############################################### Read ###################################################
print "Read"
L,a,h = R.Read_MainProp_V01()
M_Group,Cen_Group,R_Group = R.Read_Halo_Prop_Sergio_V01()
Pos_DM,Vel_DM,num_DM,mass_DM = R.Read_Part_Prop_Sergio_V04()
R_Group = array(R_Group)/a
Cen_Group = array(Cen_Group)/a
Pos_DM = array(Pos_DM)/a

############################################### Part Sel ###################################################
print "Part Sel"
ID = where(M_Group > D.Mcut)[0]+1

GroupID_DM,Particle_ID_DM = F.Get_PartGroupID(num_DM,ID)
Index  = argsort(GroupID_DM) 
Particle_ID_DM = Particle_ID_DM[Index]
GroupID_DM = GroupID_DM[Index]

#################### Calc ####################

#J = F.Get_AngularMomentum2(Particle_ID_DM,Pos_DM,Vel_DM)

IND = [] 
for i in range(20): IND.append((1+i)*0.05)

for ind in IND:
        J,M,np = F.Get_AngularMomentum_Rad(Particle_ID_DM,Pos_DM,Vel_DM,Cen_Group,R_Group*ind,GroupID_DM,MassPart = mass_DM)
        FileName = 'Rad_'+str(ind)+D.Main_Name
        J = array(J)*a*1e10
        save(FileName,array([GroupID_DM,J[:,0],J[:,1],J[:,2],M,np]))





#for ind in [0.1,0.3,0.5,0.8,1]:
#for ind in [0.9,0.7,0.6,0.4,0.2,0.05,0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.85,0.95]:
#	W = open('Rad_'+str(ind)+D.Main_Name, 'w')
#	J,M,np = F.Get_AngularMomentum_Rad(Particle_ID_DM,Pos_DM,Vel_DM,Cen_Group,R_Group*ind,GroupID_DM,MassPart = mass_DM)
#	J = array(J)*a*1e10
#	for i in range(len(GroupID_DM)):
#		print >>W,GroupID_DM[i],M_Group[GroupID_DM[i]-1],len(Pos_DM[Particle_ID_DM[i]]),J[i][0],J[i][1],J[i][2],M[i],np[i]
#	W.close()




	
#J = F.Get_AngularMomentum2_MP(Particle_ID_DM,Pos_DM,Vel_DM,MassPart = mass_DM)
#J *= sqrt(3)*a*1e10
#W = open(D.Main_Name, 'w')
#for i in range(len(GroupID_DM)):
	#print >>W,GroupID_DM[i],M_Group[GroupID_DM[i]-1],len(Pos_DM[Particle_ID_DM[i]]),J[i][0],J[i][1],J[i][2]
#W.close()

