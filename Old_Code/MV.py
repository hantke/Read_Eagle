import numpy as np
from os import system as sys
Rad = np.array([0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0],dtype=str)
Snap = np.array([12,15,19,28],dtype=str)

for r in Rad:
	for s in Snap:
		sys('mv Rad_'+r+'AngMom_Stars_L0025N0752_REF_'+s+'_Area3.txt.npy Rad_'+r+'AngMom_Stars_L0025N0752_RECAL_'+s+'_Area3.txt.npy')
