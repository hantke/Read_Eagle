################################ Package ##################################################
import numpy as np
import sys
import Read as R
import Functions as F
from os import system as s

################################ Modules ##################################################


################################  Vars ##################################################

Snap = int(sys.argv[1])
h = 0.6777
Mcut = 0.0
Rad = 0.05 # 30 pkpc
NBin = 50 # dx = 100 ppc
TAGS = ['000_z020p000','001_z015p132','002_z009p993','003_z008p988','004_z008p075','005_z007p050','006_z005p971','007_z005p487','008_z005p037','009_z004p485','010_z003p984','011_z003p528','012_z003p017','013_z002p478','014_z002p237','015_z002p012','016_z001p737','017_z001p487','018_z001p259','019_z001p004','020_z000p865','021_z000p736','022_z000p615','023_z000p503','024_z000p366','025_z000p271','026_z000p183','027_z000p101','028_z000p000']

tag = TAGS[Snap]
#SIMREF = 
sim='/cosma5/data/Eagle/ScienceRuns/Planck1/L0025N0376/PE/REFERENCE/data/'
#sim = '/cosma5/data/Eagle/ScienceRuns/Planck1/L0100N1504/PE/REFERENCE/data/'
sim_name = 'L0025N0376_ref'
#sim_name = 'L0100N1504_ref'

L,a,h = R.Read_MainProp(sim, tag)
L *= (a/h)



################################ READ ####################################

pos_St,Mass_St,num_St,num_St_SH = R.Read_Particles(sim, tag)
NumOfSubhalos = R.Read_Haloes(sim, tag)
SubHalo_gr,SubHalo_sgr,SubHalo_pos = R.Read_Subhaloes(sim, tag)

################################  MAIN  ##################################


Index_Range = F.Get_PartIndexRange(num_St,num_St_SH,NumOfSubhalos)
CenterOfPotential = F.Get_SubHaloCenter(SubHalo_gr,SubHalo_sgr,NumOfSubhalos, SubHalo_pos)

Sel_Group 		= []
Sel_SubGroup 	= []
Sel_MStell 		= []
Sel_Shell 		= []

for gr in range(len(Index_Range)):
	for sgr in range(len(Index_Range[gr])):
		#IDs = (Mass_St[Index_Range[gr][sgr][0]:Index_Range[gr][sgr][1]])
		Mstell = np.sum(Mass_St[Index_Range[gr][sgr][0]:Index_Range[gr][sgr][1]])
		if (Mstell > Mcut):
			Sel_Group.append(gr+1)
			Sel_SubGroup.append(sgr)
			Sel_MStell.append(np.log10(Mstell)+10)
			Sel_Shell.append(F.Shell(pos_St[Index_Range[gr][sgr][0]:Index_Range[gr][sgr][1]], Mass_St[Index_Range[gr][sgr][0]:Index_Range[gr][sgr][1]], Rad, L,NBin,CenterOfPotential[gr][sgr]))

Sel_Shell = np.array(Sel_Shell)

try: s('mkdir '+sim_name)
except: pass

np.save(sim_name+'/'+sim_name+'_sn'+str(Snap)+'_Shell_cop',Sel_Shell)
np.save(sim_name+'/'+sim_name+'_sn'+str(Snap)+'_SubGroup_cop',Sel_SubGroup)
np.save(sim_name+'/'+sim_name+'_sn'+str(Snap)+'_MStell_cop',Sel_MStell)
np.save(sim_name+'/'+sim_name+'_sn'+str(Snap)+'_Group_cop',Sel_Group)

