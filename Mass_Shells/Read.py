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
	ind = lexsort((num_St_SH,num_St))
	
	num_St = num_St[ind]
	num_St_SH = num_St_SH[ind]
	Mass_St = Mass_St[ind]
	pos_St = pos_St[ind]
	return pos_St,Mass_St,num_St,num_St_SH

def Read_Haloes(sim, tag):
	Cen_Group = E.readArray("SUBFIND_GROUP", sim, tag, "FOF/GroupCentreOfPotential")
	NumOfSubhalos = E.readArray("SUBFIND_GROUP", sim, tag, "FOF/NumOfSubhalos")
	return Cen_Group,NumOfSubhalos

def Read_MainProp(sim, tag):
	boxSize = E.readAttribute("SUBFIND", sim, tag, "/Header/BoxSize")
	z = E.readAttribute("SUBFIND", sim, tag, "/Header/Redshift")
	h = E.readAttribute("SUBFIND", sim, tag, "/Header/HubbleParam")
	return boxSize,1/(1+z),h
