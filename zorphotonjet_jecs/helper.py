import ROOT


## Importing stuff from other python files 
from trigger import *
from binning import *
from corrections import *


## C++ function for alpha calculation
ROOT.gInterpreter.Declare('''
inline float Alpha_func(const ROOT::VecOps::RVec<float> &pt_jet, const float pt_ref){

      return pt_jet.size()>1 ? pt_jet[1]/pt_ref : 0.0;

}
''')


def SinglePhotonSelection(df, triggers):
    '''
    Select events with exactly one photon with pT>20 GeV.
    The event must pass a photon trigger (for now 120 GeV trigger only)
    '''
    df = df.Filter(TriggerFired(triggers),'trigger single photon')

    df = df.Define('photonsptgt20','Photon_pt>20&&Photon_pfChargedIsoPFPV<0.2')
    df = df.Filter('Sum(photonsptgt20)==1','=1 photon with p_{T}>20 GeV')

    df = df.Define('isRefPhoton','Photon_mvaID_WP80&&Photon_electronVeto&&Photon_pfChargedIsoPFPV<0.03&&Photon_pfRelIso03_all_quadratic<0.05&&abs(Photon_eta)<1.479&&'+TriggerSelect(triggers))
    
    df = df.Filter('Sum(isRefPhoton)==1','Photon passes tight ID and is in EB')
    
    df = df.Define('cleanPh_Pt','Photon_pt[isRefPhoton]')
    df = df.Define('cleanPh_Eta','Photon_eta[isRefPhoton]')
    df = df.Define('cleanPh_Phi','Photon_phi[isRefPhoton]')
    
    df = df.Define('ref_Pt','cleanPh_Pt[0]')
    df = df.Define('ref_Phi','cleanPh_Phi[0]')
    
    return df
    
    
def ZEE_EleSelection(df):
    '''
    Select Z->ee events passing a double electron trigger.
    '''
    df = df.Filter('HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL')
    df = df.Define('Electron_PassTightID','Electron_Pt>25&&Electron_mvaIso_WP90')
    df = df.Filter('Sum(Electron_PassTightId)>=2')

    df = df.Define('_mll', 'mll(Electron_pt, Electron_eta, Electron_phi, PassTightID, PassTightID)')
    df = df.Filter('_mll>70&&_mll<110')
    
    return df


def ZMuMu_MuSelection(df):
    '''
    Selects Z->mumu events passing a single muon trigger. Defines probe pt/eta/phi
    '''
    df = df.Filter('HLT_IsoMu24')

    df = df.Define('Muon_PassTightId','Muon_pfIsoId>=3&&Muon_mediumPromptId') 
    df = df.Filter('Sum(Muon_PassTightId)>=2')
    df = df.Define('_mll', 'mll(Muon_pt, Muon_eta, Muon_phi, Muon_PassTightId, Muon_PassTightId)')
    df = df.Filter('_mll>70&&_mll<110')

    return df

    
def CleanJets(df):
    # List of cleaned jets (noise cleaning + lepton/photon overlap removal)
    df = df.Define('_jetPassID', 'Jet_jetId>=6')

    # Next line to make sure we remove the leptons/the photon
    # TODO: Make a flag to run on raw or corrected jet pt
    # Corrected jet pt
    df = df.Define('Jet_ptCor', 'JetEnergyCorrections(Jet_area, Jet_eta, Jet_pt, Rho_fixedGridRhoAll)')
    df = df.Define('isCleanJet_corPt','_jetPassID&&(Jet_ptCor>30||(Jet_ptCor>20&&abs(Jet_eta)<2.4))&&Jet_muEF<0.5&&Jet_chEmEF<0.5&&Jet_neEmEF<0.8')

    # Raw jet pt
    df = df.Define('isCleanJet','_jetPassID&&(Jet_pt>30||(Jet_pt>20&&abs(Jet_eta)<2.4))&&Jet_muEF<0.5&&Jet_chEmEF<0.5&&Jet_neEmEF<0.8')
    df = df.Define('cleanJet_Pt','Jet_pt[isCleanJet]')
    df = df.Define('cleanJet_Eta','Jet_eta[isCleanJet]')
    df = df.Define('cleanJet_Phi','Jet_phi[isCleanJet]')
    df = df.Filter('Sum(isCleanJet)>=1','>=1 clean jet with p_{T}>20/30 GeV')

    # For the subleading jet (alpha calculation) we do not apply any pt cut
    df = df.Define('isCleanJet_noPtcut','_jetPassID&&Jet_muEF<0.5&&Jet_chEmEF<0.5&&Jet_neEmEF<0.8')
    df = df.Define('cleanJet_Pt_noPtcut','Jet_pt[isCleanJet_noPtcut]')

    return df

    
def PtBalanceSelection(df):
    '''
    Compute pt balance = pt(jet)/pt(ref) and alpha=pt(subleading_jet)/pt(ref)
    ref can be a photon or a Z.
    '''
    # Back to back condition
    df = df.Filter('abs(acos(cos(ref_Phi-cleanJet_Phi[0])))>2.9','DeltaPhi(ph,jet)>2.9')

    # Compute Pt balance = pt(jet)/pt(ref)    
    df = df.Define('ptbalance','cleanJet_Pt[0]/ref_Pt')
    df = df.Define('probe_Eta','cleanJet_Eta[0]') 
    df = df.Define('probe_Phi','cleanJet_Phi[0]')

    # Compute alpha=pt(subleading_jet)/pt(ref) using the Alpha_func
    df = df.Define('alpha','Alpha_func(cleanJet_Pt_noPtcut,ref_Pt)')

    return df


def AnalyzePtBalance(df, suffix = ''):
    histos = {}                                 # Dictionary for histograms (one histo per eta, alpha and ref_Pt)
    df_ptBalanceBinnedInEtaAndAlphaPerPt = {}   # RDataFrame for filtering on eta, alpha and ref_Pt bins

    # Loop over eta bins
    for e in range(NetaBins):
        # Loop over alpha bins
        for a in range(NalphaBins):
            # Loop over pt bins
            for p in range(NptBins):
                # Filtering on eta, alpha and pt bins
                key = '_' + str_binetas[e] + '_' + str_binalphas[a] + '_' + str_binpts[p]
                df_ptBalanceBinnedInEtaAndAlphaPerPt[key] = df.Filter('abs(cleanJet_Eta[0])>={}&&abs(cleanJet_Eta[0])<{}'.format(jetetaBins[e], jetetaBins[e+1]))\
                                                              .Filter('alpha>={}&&alpha<{}'.format(alphaBins[a], alphaBins[a+1]))\
                                                              .Filter('ref_Pt>={}&&ref_Pt<{}'.format(jetptBins[p], jetptBins[p+1]))

                # One histogram per eta, alpha, ref_Pt bin
                histos['balancevsrefpt' + key + suffix] = df_ptBalanceBinnedInEtaAndAlphaPerPt[key]\
                                                          .Histo2D(ROOT.RDF.TH2DModel('h_BalanceVsRefPt{}'.format(key)+suffix,'ptbalance',\
                                                          NptBins, jetptBins, NptbalanceBins, ptbalanceBins), 'ref_Pt','ptbalance')

    return df, histos
