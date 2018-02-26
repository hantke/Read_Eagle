################################################ Package ##################################################
import eagle as E
from numpy import *
#Internal libs
from Database import *
################################################ Constant ##################################################

def Read_SubHalo_Part_Paulina_V01():
        pos_St = E.readArray("PARTDATA", sim, tag, "/PartType4/Coordinates")
        vel_St = E.readArray("PARTDATA", sim, tag, "/PartType4/Velocity")
        Mass_St = E.readArray("PARTDATA", sim, tag, "/PartType4/Mass")
        num_St = E.readArray("PARTDATA", sim, tag, "/PartType4/GroupNumber")
        num_St_SH = E.readArray("PARTDATA", sim, tag, "/PartType4/SubGroupNumber")
	Ab_1_O = E.readArray("PARTDATA", sim, tag, "/PartType4/ElementAbundance/Oxygen")	
	Ab_2_O = E.readArray("PARTDATA", sim, tag, "/PartType4/SmoothedElementAbundance/Oxygen")
	Ab_1_H = E.readArray("PARTDATA", sim, tag, "/PartType4/ElementAbundance/Hydrogen")
        Ab_2_H = E.readArray("PARTDATA", sim, tag, "/PartType4/SmoothedElementAbundance/Hydrogen")



        num_St = abs(num_St)
        num_St_SH = abs(num_St_SH)

        ind = lexsort((num_St_SH,num_St))

        pos_St = pos_St[ind]
        vel_St = vel_St[ind]
        Mass_St = Mass_St[ind]
        num_St = num_St[ind]
        num_St_SH = num_St_SH[ind]
        Ab_1_O = Ab_1_O[ind]
        Ab_2_O = Ab_2_O[ind]
        Ab_1_H = Ab_1_H[ind]
        Ab_2_H = Ab_2_H[ind]
	


        return pos_St,vel_St,Mass_St,num_St,num_St_SH,Ab_1_O,Ab_2_O,Ab_1_H,Ab_2_H

def Read_SubHalo_Part_Paulina_V02():
        pos_St = E.readArray("PARTDATA", sim, tag, "/PartType0/Coordinates")
        vel_St = E.readArray("PARTDATA", sim, tag, "/PartType0/Velocity")
        Mass_St = E.readArray("PARTDATA", sim, tag, "/PartType0/Mass")
        num_St = E.readArray("PARTDATA", sim, tag, "/PartType0/GroupNumber")
        num_St_SH = E.readArray("PARTDATA", sim, tag, "/PartType0/SubGroupNumber")
        Ab_1_O = E.readArray("PARTDATA", sim, tag, "/PartType0/ElementAbundance/Oxygen")
        Ab_2_O = E.readArray("PARTDATA", sim, tag, "/PartType0/SmoothedElementAbundance/Oxygen")
        Ab_1_H = E.readArray("PARTDATA", sim, tag, "/PartType0/ElementAbundance/Hydrogen")
        Ab_2_H = E.readArray("PARTDATA", sim, tag, "/PartType0/SmoothedElementAbundance/Hydrogen")
	SFR    = E.readArray("PARTDATA", sim, tag, "/PartType0/StarFormationRate")



        num_St = abs(num_St)
        num_St_SH = abs(num_St_SH)

        ind = lexsort((num_St_SH,num_St))

        pos_St = pos_St[ind]
        vel_St = vel_St[ind]
        Mass_St = Mass_St[ind]
        num_St = num_St[ind]
        num_St_SH = num_St_SH[ind]
        Ab_1_O = Ab_1_O[ind]
        Ab_2_O = Ab_2_O[ind]
        Ab_1_H = Ab_1_H[ind]
        Ab_2_H = Ab_2_H[ind]
	SFR = SFR[ind]


        return pos_St,vel_St,Mass_St,num_St,num_St_SH,Ab_1_O,Ab_2_O,Ab_1_H,Ab_2_H,SFR



##########################################################################################
def Read_Halo_Prop_Sergio_V01():
	M_Group = E.readArray("SUBFIND_GROUP", sim, tag, "FOF/Group_M_Crit200") * 1e10
	Cen_Group = E.readArray("SUBFIND_GROUP", sim, tag, "FOF/GroupCentreOfPotential")
	R_Group = E.readArray("SUBFIND_GROUP", sim, tag, "FOF/Group_R_Crit200")
	return M_Group,Cen_Group,R_Group
	
def Read_Part_Prop_Sergio_V01():	
	pos = E.readArray("PARTDATA", sim, tag, "/PartType1/Coordinates")
	vel = E.readArray("PARTDATA", sim, tag, "/PartType1/Velocity")
	num = E.readArray("PARTDATA", sim, tag, "/PartType1/GroupNumber")
	num = abs(num)
	indices = argsort(num)
	num = num[indices]
	pos = pos[indices]
	vel = vel[indices]
	return pos,vel,num
def Read_Part_Prop_Sergio_V00():	
	pos = E.readArray("PARTDATA", sim, tag, "/PartType0/Coordinates")
	vel = E.readArray("PARTDATA", sim, tag, "/PartType0/Velocity")
	num = E.readArray("PARTDATA", sim, tag, "/PartType0/GroupNumber")
	mass = E.readArray("PARTDATA", sim, tag, "/PartType0/Mass")
	temp = E.readArray("PARTDATA", sim, tag, "/PartType0/Temperature")
	num = abs(num)
	indices = argsort(num)
	num = num[indices]
	pos = pos[indices]
	vel = vel[indices]
	mass = mass[indices]
	temp = mass[indices]
	return pos,vel,num,mass,temp
def Read_Part_Prop_Sergio_V04():	
	pos = E.readArray("PARTDATA", sim, tag, "/PartType4/Coordinates")
	vel = E.readArray("PARTDATA", sim, tag, "/PartType4/Velocity")
	num = E.readArray("PARTDATA", sim, tag, "/PartType4/GroupNumber")
	mass = E.readArray("PARTDATA", sim, tag, "/PartType4/Mass")
	num = abs(num)
	indices = argsort(num)
	num = num[indices]
	pos = pos[indices]
	vel = vel[indices]
	mass = mass[indices]
	return pos,vel,num,mass
def Read_Halo_Prop_Idit_V01():
	M_Group = E.readArray("SUBFIND_GROUP", sim, tag, "FOF/Group_M_Crit200") * 1e10
	Cen_Group = E.readArray("SUBFIND_GROUP", sim, tag, "FOF/GroupCentreOfPotential")
	CenM_Group = E.readArray("FOF", sim, tag, "FOF/CentreOfMass")
	Vel_Group = E.readArray("FOF", sim, tag, "FOF/Velocity")
	R_Group = E.readArray("SUBFIND_GROUP", sim, tag, "FOF/Group_R_Crit200")
	Nsub_Group = E.readArray("SUBFIND_GROUP", sim, tag, "FOF/NumOfSubhalos")
	return M_Group,Cen_Group,Vel_Group,R_Group,CenM_Group,Nsub_Group


def Read_Part_Prop_Idit_V01():	
	vel_DM = E.readArray("PARTDATA", sim, tag, "/PartType1/Velocity")
	num_DM = E.readArray("PARTDATA", sim, tag, "/PartType1/GroupNumber")
	
	num_DM = abs(num_DM)
	indices = argsort(num_DM)
	vel_DM = vel_DM[indices]
	num_DM = num_DM[indices]

	###################

	vel_St = E.readArray("PARTDATA", sim, tag, "/PartType4/Velocity")
	Mass_St = E.readArray("PARTDATA", sim, tag, "/PartType4/Mass")
	num_St = E.readArray("PARTDATA", sim, tag, "/PartType4/GroupNumber")
	
	num_St = abs(num_St)
	indices = argsort(num_St)
	vel_St = vel_St[indices]
	Mass_St = Mass_St[indices]
	num_St = num_St[indices]
	return vel_DM,num_DM,vel_St,Mass_St,num_St
	###################
	
def Read_SubHalo_Prop_Idit_V01():
	StellMass030_SH = E.readArray("SUBFIND", sim, tag, "Subhalo/ApertureMeasurements/Mass/030kpc")[:,4]*1e10
	M_Group = E.readArray("SUBFIND_GROUP", sim, tag, "FOF/Group_M_Crit200") * 1e10
	Cen_SH = E.readArray("SUBFIND", sim, tag, "Subhalo/CentreOfPotential")
	Vel_SH = E.readArray("SUBFIND", sim, tag, "Subhalo/Velocity")
	GroupID_SH = E.readArray("SUBFIND", sim, tag, "Subhalo/GroupNumber")
	SubGroupID_SH = E.readArray("SUBFIND", sim, tag, "Subhalo/SubGroupNumber")
	return StellMass030_SH,Cen_SH,Vel_SH,GroupID_SH,SubGroupID_SH,M_Group

def Read_SubHalo_Part_Idit_V01():
	pos_St = E.readArray("PARTDATA", sim, tag, "/PartType4/Coordinates")
	vel_St = E.readArray("PARTDATA", sim, tag, "/PartType4/Velocity")
	Mass_St = E.readArray("PARTDATA", sim, tag, "/PartType4/Mass")
	num_St = E.readArray("PARTDATA", sim, tag, "/PartType4/GroupNumber")
	num_St_SH = E.readArray("PARTDATA", sim, tag, "/PartType4/SubGroupNumber")
	
	num_St = abs(num_St)
	num_St_SH = abs(num_St_SH)
	
	ind = lexsort((num_St_SH,num_St))
	
	pos_St = pos_St[ind]
	vel_St = vel_St[ind]
	Mass_St = Mass_St[ind]
	num_St = num_St[ind]
	num_St_SH = num_St_SH[ind]
	
	return pos_St,vel_St,Mass_St,num_St,num_St_SH

def Read_OnlyDM_Halo_V01():#TODO CHECK ME!
	M_Group = E.readArray("SUBFIND_GROUP", sim_DM, tag, "FOF/Group_M_Crit200") * 1e10
	Cen_Group = E.readArray("SUBFIND_GROUP", sim_DM, tag, "FOF/GroupCentreOfPotential")
	Vel_Group = E.readArray("FOF", sim_DM, tag, "FOF/Velocity")
	return M_Group,Cen_Group,Vel_Group
def Read_OnlyDM_Part_V01():	
	pos = E.readArray("PARTDATA", sim_DM, tag, "/PartType1/Coordinates")
	vel = E.readArray("PARTDATA", sim_DM, tag, "/PartType1/Velocity")
	num = E.readArray("PARTDATA", sim_DM, tag, "/PartType1/GroupNumber")
	num = abs(num)
	indices = argsort(num)
	num = num[indices]
	pos = pos[indices]
	vel = vel[indices]
	return pos,vel,num


def Read_MainProp_V01():
	boxSize = E.readAttribute("SUBFIND", sim, tag, "/Header/BoxSize")
	z = E.readAttribute("SUBFIND", sim, tag, "/Header/Redshift")
	h = E.readAttribute("SUBFIND", sim, tag, "/Header/HubbleParam")
	return boxSize,1/(1+z),h
def Read_MainProp_OnlyDM_V01():
	boxSize = E.readAttribute("SUBFIND", sim_DM, tag, "/Header/BoxSize")
	z = E.readAttribute("SUBFIND", sim_DM, tag, "/Header/Redshift")
	h = E.readAttribute("SUBFIND", sim_DM, tag, "/Header/HubbleParam")
	return boxSize,1/(1+z),h
############################################################################################################################

def Read_PrintPart_Group_V01(DMonly = False):
	Simu = sim
	if DMonly:	Simu = sim_DM
	M_Group = E.readArray("SUBFIND_GROUP", Simu, tag, "FOF/Group_M_Crit200") * 1e10
	return M_Group

def Read_PrintPart_Stars_V01():
	pos_St = E.readArray("PARTDATA", sim, tag, "/PartType4/Coordinates")
	vel_St = E.readArray("PARTDATA", sim, tag, "/PartType4/Velocity")
	Mass_St = E.readArray("PARTDATA", sim, tag, "/PartType4/Mass")
	num_St = E.readArray("PARTDATA", sim, tag, "/PartType4/GroupNumber")
	num_St_SH = E.readArray("PARTDATA", sim, tag, "/PartType4/SubGroupNumber")
	
	num_St = abs(num_St)
	num_St_SH = abs(num_St_SH)
	
	ind = lexsort((num_St_SH,num_St))
	
	pos_St = pos_St[ind]
	vel_St = vel_St[ind]
	Mass_St = Mass_St[ind]
	num_St = num_St[ind]
	num_St_SH = num_St_SH[ind]
	
	return pos_St,vel_St,Mass_St,num_St,num_St_SH


def Read_PrintPart_DM_V01(DMonly = False):
	Simu = sim
	if DMonly:	Simu = sim_DM
	pos_DM = E.readArray("PARTDATA", Simu, tag, "/PartType1/Coordinates")
	vel_DM = E.readArray("PARTDATA", Simu, tag, "/PartType1/Velocity")
	num_DM = E.readArray("PARTDATA", Simu, tag, "/PartType1/GroupNumber")
	num_DM_SH = E.readArray("PARTDATA", Simu, tag, "/PartType1/SubGroupNumber")
	
	num_DM = abs(num_DM)
	num_DM_SH = abs(num_DM_SH)
	
	ind = lexsort((num_DM_SH,num_DM))
	
	pos_DM = pos_DM[ind]
	vel_DM = vel_DM[ind]
	num_DM = num_DM[ind]
	num_DM_SH = num_DM_SH[ind]
	
	return pos_DM,vel_DM,num_DM,num_DM_SH
