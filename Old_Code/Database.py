#################### Global Parameters ###########################

#sim='/cosma5/data/Eagle/ScienceRuns/Planck1/L0025N0752/PE/Z0p10_W1p00_E_3p0_0p3_ALPHA1p0e6_rhogas1_reposlim3p0soft_100mgas/data/'
#sim='/cosma5/data/Eagle/ScienceRuns/Planck1/L0025N0752/PE/RECALIBRATED/data/'
#sim='/cosma5/data/Eagle/ScienceRuns/Planck1/L0025N0376/PE/REFERENCE/data/'

#sim='/cosma5/data/Eagle/ScienceRuns/Planck1/L0012N0188/PE/Z0p10_W1p00_E_3p0_0p3_ALPHA1p0e6_rhogas1_reposlim3p0soft_100mgas/data'

#sim = '/cosma5/data/Eagle/ScienceRuns/Planck1/L0100N1504/PE/REFERENCE/data/' #TODO CHANGE ME BACK
sim='/cosma5/data/Eagle/ScienceRuns/Planck1/L0025N0752/PE/RECALIBRATED/data/'

#sim="/cosma5/data/Eagle/ScienceRuns/Planck1/L0025N0752/PE/REFERENCE/data/"

#LBOX = 100 #TODO CHANGE ME BACK
LBOX = 25 

#http://eagle.strw.leidenuniv.nl/wiki/doku.php?id=eagle:documentation:reading_python
#http://eagle.strw.leidenuniv.nl/wiki/doku.php?id=eagle:simulations:simulation_overview:list_of_eagle_resolution_simulations  TO SEE THE RESOLUTIONS
DM_Mass = 1211880.#High resolution
#DM_Mass = 1211880.*8#Normal Resolution #TODO CHANGE ME BACK
#################### Global Array      ###########################
Track_Snap = None
Main_Name  = None
#TAGS = ['015_z002p012','016_z001p737','017_z001p487','018_z001p259','019_z001p004','020_z000p865','021_z000p736','022_z000p615','023_z000p503','024_z000p366','025_z000p271','026_z000p183','027_z000p101','028_z000p000']
TAGS = ['000_z020p000','001_z015p132','002_z009p993','003_z008p988','004_z008p075','005_z007p050','006_z005p971','007_z005p487','008_z005p037','009_z004p485','010_z003p984','011_z003p528','012_z003p017','013_z002p478','014_z002p237','015_z002p012','016_z001p737','017_z001p487','018_z001p259','019_z001p004','020_z000p865','021_z000p736','022_z000p615','023_z000p503','024_z000p366','025_z000p271','026_z000p183','027_z000p101','028_z000p000']

#TAGS = ['028_z000p000','027_z000p101','026_z000p183','025_z000p271','024_z000p366','023_z000p503','022_z000p615','021_z000p736','020_z000p865','019_z001p004','018_z001p259','017_z001p487','016_z001p737','015_z002p012']
def Get_Sim(Snap):
	global Main_Name
	global tag
	#Main_Name = 'AngMom_Stars_L0100N1504_REF_'+str(Snap)+'_Area3.txt' #TODO CHANGE ME BACK
	Main_Name = 'AngMom_Stars_L0025N0752_RECAL_'+str(Snap)+'_Area3.txt'
	tag = TAGS[Snap]
	 



#################### OPTIONS #######################
Mcut = 3e8 #Cut on Halo mass in sollar mass unites
Rad_OnlyDM = [1,2,3,4,5,6,7,8,9,10] # Raidus in Kpc
#L0025N0188	L0050N0376	L0100N0752	L0012N0188	L0025N0376	L0050N0752	L0100N1504	L0012N0376	L0025N0752
#000_z020p000	001_z015p132	002_z009p993	003_z008p988
#004_z008p075	005_z007p050	006_z005p971	007_z005p487
#008_z005p037	009_z004p485	010_z003p984	011_z003p528
#012_z003p017	013_z002p478	014_z002p237	015_z002p012
#017_z001p487	018_z001p259	019_z001p004	020_z000p865 020_z001p737
#021_z000p736	022_z000p615	023_z000p503	024_z000p366
#025_z000p271	026_z000p183	027_z000p101	028_z000p000
