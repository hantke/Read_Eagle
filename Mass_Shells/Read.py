import eagle as E
import numpy as np


def Read_Particles(sim, tag):
	pos_St = E.readArray("PARTDATA", sim, tag, "/PartType4/Coordinates")
	num_St = E.readArray("PARTDATA", sim, tag, "/PartType4/GroupNumber")
	num_St_SH = E.readArray("PARTDATA", sim, tag, "/PartType4/SubGroupNumber")
	Mass_St = E.readArray("PARTDATA", sim, tag, "/PartType4/Mass")
		###
	num_St = abs(num_St)
	num_St_SH = abs(num_St_SH)
	ind = np.lexsort((num_St_SH,num_St))
	
	num_St = num_St[ind]
	num_St_SH = num_St_SH[ind]
	Mass_St = Mass_St[ind]
	pos_St = pos_St[ind]
	return pos_St,Mass_St,num_St,num_St_SH

def Read_Haloes(sim, tag):
	#Cen_Group = E.readArray("SUBFIND_GROUP", sim, tag, "FOF/GroupCentreOfPotential")
	NumOfSubhalos = E.readArray("SUBFIND_GROUP", sim, tag, "FOF/NumOfSubhalos")
	return NumOfSubhalos

def Read_Subhaloes(sim, tag):
	#Cen_Group = E.readArray("SUBFIND_GROUP", sim, tag, "FOF/GroupCentreOfPotential")
	SubHalo_gr = E.readArray("SUBFIND", sim, tag, "Subhalo/GroupNumber")
	SubHalo_sgr = E.readArray("SUBFIND", sim, tag, "Subhalo/SubGroupNumber")
	SubHalo_pos = E.readArray("SUBFIND", sim, tag, "Subhalo/CentreOfPotential")
	
	SubHalo_gr = abs(SubHalo_gr)
	SubHalo_sgr = abs(SubHalo_sgr)
	ind = np.lexsort((SubHalo_sgr,SubHalo_gr))
	
	SubHalo_gr = SubHalo_gr[ind]
	SubHalo_sgr = SubHalo_sgr[ind]
	SubHalo_pos = SubHalo_pos[ind]
	
	return SubHalo_gr,SubHalo_sgr,SubHalo_pos

def Read_MainProp(sim, tag):
	boxSize = E.readAttribute("SUBFIND", sim, tag, "/Header/BoxSize")
	z = E.readAttribute("SUBFIND", sim, tag, "/Header/Redshift")
	h = E.readAttribute("SUBFIND", sim, tag, "/Header/HubbleParam")
	return boxSize,1/(1+z),h

####################### V2

def Read_Particles_v2(sim, tag):
	pos_St = E.readArray("PARTDATA", sim, tag, "/PartType4/Coordinates")
	num_St = E.readArray("PARTDATA", sim, tag, "/PartType4/GroupNumber")
	num_St_SH = E.readArray("PARTDATA", sim, tag, "/PartType4/SubGroupNumber")
	Mass_St = E.readArray("PARTDATA", sim, tag, "/PartType4/Mass")
	ParticleIDs_St = E.readArray("PARTDATA", sim, tag, "/PartType4/ParticleIDs")
		###
	num_St = abs(num_St)
	num_St_SH = abs(num_St_SH)
	ind = np.lexsort((num_St_SH,num_St))
	
	num_St = num_St[ind]
	num_St_SH = num_St_SH[ind]
	Mass_St = Mass_St[ind]
	pos_St = pos_St[ind]
	ParticleIDs_St = ParticleIDs_St[ind]
	return pos_St,Mass_St,num_St,num_St_SH,ParticleIDs_St

def Read_Particles_ID(sim, tag):
	ParticleID = E.readArray("SUBFIND_PARTICLES", sim, tag, "/IDs/ParticleID")
	Particle_Binding_Energy = E.readArray("SUBFIND_PARTICLES", sim, tag, "/IDs/Particle_Binding_Energy")
	
	ind = np.argsort(ParticleID)
	ParticleID = ParticleID[ind]
	Particle_Binding_Energy = Particle_Binding_Energy[ind]
	
	return ParticleID,Particle_Binding_Energy
