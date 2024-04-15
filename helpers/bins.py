from array import array
import itertools

jetEtaBins = [0., 1.3, 2.5, 3., 3.5, 4., 5.]
egEtaBins = [0., 1.479, 2.5]
muEtaBins = [0., 0.83, 1.24, 2.4]
muEMTFBins = [1.24, 1.6, 2.1, 2.4]
# tauEtaBins = [0., 1.5, 2.1]


ht_bins = array('f', [ i*10 for i in range(50) ] + [ 500+ i*20 for i in range(25) ] + [1000 + i*50 for i in range(10)] +[1500,1600,1700,1800,2000,2500,3000,4000,6000,8000])
#leptonpt_bins = array('f',[ i for i in range(50) ] + [ 50+2*i for i in range(10) ] + [ 70+3*i for i in range(10) ] + [100+10*i for i in range(10) ] + [200, 250, 300, 400, 500])
jetmetpt_bins = array('f',[ i*5 for i in range(50) ] +  [250+10*i for i in range(25) ]  + [500+20*i for i in range(10) ] + [700, 800, 900, 1000, 1200, 1500, 2000, 3000 ])

# Finer binning:
leptonpt_bins = array('f',[i * .2 for i in range(15 * 5)] + [ 15 + i * .5 for i in range(5 * 2)] + [20 + i for i in range(30)] + [ 50+2*i for i in range(10) ] + [ 70+3*i for i in range(10) ] + [100+10*i for i in range(10) ] + [200, 250, 300, 400, 500])

coarse_leptonpt_bins = array('f',[ i for i in range(50) ] + [ 50+2*i for i in range(10) ] + [ 70+3*i for i in range(10) ] + [100+10*i for i in range(10) ] + [200, 250, 300, 400, 500])
coarse2_leptonpt_bins = array('f',[ i for i in range(20) ] + [20, 25, 30, 35, 45, 60, 75, 100, 140, 200, 250, 300, 400, 500])

# bins used for dqm offline eg plots -----------
dqmoff_egpt_bins = list( 
	itertools.chain(
		range(2, 42, 2), range(42, 45, 3), 
		range(45, 50, 5), range(50, 70, 10), 
		range(70, 101, 30)
	)
)
dqmoff_egpt_bins = array('f', dqmoff_egpt_bins)
dqmoff_egphi_bins = array('f', [(-3.2 + i * 0.2) for i in range(33)])
dqmoff_egeta_bins = array('f', [(-2.5 + i * 0.1) for i in range(51)])
dqmoff_egnvtx_bins = array('f', [i for i in range(0, 61, 2)])
dqmoff_egresolution_pt_bins = array('f', [-1.0 + i * 0.05 for i in range(51)])
dqmoff_egresolution_eta_bins = array('f', [-0.3 + i * 0.005 for i in range(121)])
dqmoff_egresolution_phi_bins = array('f', [-0.3 + i * 0.005 for i in range(121)])

# bins used for dqm offline muon plots -----------
dqmoff_muonpt_bins = list( 
	itertools.chain(
		range(0, 30, 1), range(30, 50, 2), 
		range(50, 70, 5), range(70, 100, 10), 
		range(100, 200, 25), range(200, 300, 50), 
		range(300, 500, 100), range(500, 700, 200), 
		range(700, 1000, 300)
	)
)
dqmoff_muonpt_bins.append(1000)
dqmoff_muonpt_bins = array('f', dqmoff_muonpt_bins)
dqmoff_muonphi_bins = array('f', [(-3.4 + i * 0.2) for i in range(35)])
dqmoff_muoneta_bins = array('f', [(-2.5 + i * 0.1) for i in range(51)])
dqmoff_muonnvtx_bins = array('f', [i for i in range(0, 101)])
dqmoff_muonresolution_pt_bins = array('f', [-2.0 + i * 0.08 for i in range(51)])
dqmoff_muonresolution_eta_bins = array('f', [-0.1 + i * 0.002 for i in range(101)])
dqmoff_muonresolution_phi_bins = array('f', [-0.2 + i * 0.0041666 for i in range(97)])

# bins used for dqm offline tau plots -----------
dqmoff_taupt_bins = list( 
	itertools.chain(
		range(0, 50, 1), range(50, 60, 2), 
		range(60, 80, 5), range(80, 200, 10), 
		range(200, 300, 20), range(300, 400, 50), 
		range(400, 600, 100), range(600, 1200, 200)
	)
)
dqmoff_taupt_bins = array('f', dqmoff_taupt_bins)
dqmoff_tauphi_bins = array('f', [(-3.4 + i * 0.2) for i in range(35)])
dqmoff_taueta_bins = array('f', [(-2.5 + i * 0.1) for i in range(51)])
dqmoff_taunvtx_bins = array('f', [i for i in range(0, 76)])
dqmoff_tauresolution_pt_bins = array('f', [-1.0 + i * 0.05 for i in range(51)])
dqmoff_tauresolution_eta_bins = array('f', [-0.3 + i * 0.005 for i in range(121)])
dqmoff_tauresolution_phi_bins = array('f', [-0.3 + i * 0.005 for i in range(121)])

# bins used for dqm offline jet plots -----------
dqmoff_jetpt_bins = list( 
	itertools.chain(
		range(0, 120, 10), range(120, 180, 20), 
		range(180, 300, 40), range(300, 401, 100)
	)
)
dqmoff_jetpt_bins = array('f', dqmoff_jetpt_bins)
dqmoff_jetresolution_pt_bins = array('f', [-1.0 + i * 0.05 for i in range(51)])
dqmoff_jetresolution_eta_bins = array('f', [-0.3 + i * 0.005 for i in range(121)])
dqmoff_jetresolution_phi_bins = array('f', [-0.3 + i * 0.005 for i in range(121)])

# bins used for dqm offline etsum plots -----------
dqmoff_etsum_bins = list( 
	itertools.chain(
		range(0, 40, 4), range(40, 70, 2), range(70, 100, 5),
		range(100, 160, 10), range(160, 261, 20)
	)
)
dqmoff_etsum_bins = array('f', dqmoff_etsum_bins)
dqmoff_etsumresolution_met_bins = array('f', [-1.0 + i * 0.05 for i in range(71)])
dqmoff_etsumresolution_metphi_bins = array('f', [-1.0 + i * 0.01 for i in range(201)])

dqmoff_prefire_ptbins = coarse_leptonpt_bins
dqmoff_prefire_etabins = array('f', [-2.5, -1.479, 0., 1.479, 2.5])
