################################ Package ##################################################
import numpy as np
import sys
import Read as R
import Function as F

################################ Modules ##################################################


################################  Vars ##################################################

Snap = int(sys.argv[1])
Mcut = 0.01
Rad = 0.02 # 20 pkpc
NBin = 200 # dx = 100 ppc
TAGS = ['000_z020p000','001_z015p132','002_z009p993','003_z008p988','004_z008p075','005_z007p050','006_z005p971','007_z005p487','008_z005p037','009_z004p485','010_z003p984','011_z003p528','012_z003p017','013_z002p478','014_z002p237','015_z002p012','016_z001p737','017_z001p487','018_z001p259','019_z001p004','020_z000p865','021_z000p736','022_z000p615','023_z000p503','024_z000p366','025_z000p271','026_z000p183','027_z000p101','028_z000p000']

tag = TAGS[Snap]
#sim='/cosma5/data/Eagle/ScienceRuns/Planck1/L0025N0752/PE/RECALIBRATED/data/'
sim = '/cosma5/data/Eagle/ScienceRuns/Planck1/L0100N1504/PE/REFERENCE/data/'

L,a,h = Read_MainProp(sim, tag)
L *= a



################################ READ ####################################

pos_St,Mass_St,num_St,num_St_SH = R.Read_Particles(sim, tag)
Cen_Group,NumOfSubhalos = R.Read_Haloes(sim, tag)

pos_St *= a

################################  MAIN  ##################################


Index_Range = Get_PartIndexRange(num_St,num_St_SH,NumOfSubhalos)

Sel_Group 		= []
Sel_SubGroup 	= []
Sel_MStell 		= []
Sel_Shell 		= []

for gr in range(Index_Range):
	for sgr in range(Index_Range[gr]):
		IDs = (Mass_St[Index_Range[gr][sgr][0]:Index_Range[gr][sgr][1]])
		Mstell = np.sum(Mass_St[Index_Range[gr][sgr][0]:Index_Range[gr][sgr][1]])
		if (Mstell > Mcut):
			Sel_Group.append(gr+1)
			Sel_SubGroup.append(sgr)
			Sel_MStell.append(np.log10(Mstell)+10)
			Sel_Shell.append(Shell(pos_St[Index_Range[gr][sgr][0]:Index_Range[gr][sgr][1]],gr_Pos, Mass_St[Index_Range[gr][sgr][0]:Index_Range[gr][sgr][1]], Rad, L,NBin))
