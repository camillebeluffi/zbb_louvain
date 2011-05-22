## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.2 $'),
    annotation = cms.untracked.string('PAT tuple for Z+b analysis'),
    name = cms.untracked.string('$Source: /cvs/CMSSW/UserCode/zbb_louvain/test/patTuple_llbb_413_data_cfg.py,v $')
)

# for the latest reprocessed samples. You can find it here : https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions
#process.GlobalTag.globaltag = cms.string('FT_R_39X_V4A::All')
#process.GlobalTag.globaltag = cms.string('GR_R_39X_V6::All')
#process.GlobalTag.globaltag = cms.string('GR_P_V14::All')
#process.GlobalTag.globaltag = cms.string('GR_P_V16::All')
#process.GlobalTag.globaltag = cms.string('GR_R_311_V2::All')
#process.GlobalTag.globaltag = cms.string('GR_R_42_V14::All')
#process.GlobalTag.globaltag = cms.string('FT_R_42_V13A::All')


## Geometry and Detector Conditions (needed for a few patTuple production steps)
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string( 'GR_R_42_V14::All' )


# running on data, remove genparticle references in objects
from PhysicsTools.PatAlgos.tools.coreTools import *
removeMCMatching(process, ['All'])

# scrapingveto:
process.scrapingVeto = cms.EDFilter("FilterOutScraping",
                                    applyfilter = cms.untracked.bool(True),
                                    debugOn = cms.untracked.bool(False),
                                    numtrack = cms.untracked.uint32(10),
                                    thresh = cms.untracked.double(0.2)
                                    )

#---------------------------- Trigger
#------------------------------------------------------------------------------------------------------------------------------------------------

# electron triggers are taken accroding to https://twiki.cern.ch/twiki/bin/viewauth/CMS/VbtfZeeBaselineSelection

muontriggers      = cms.vstring("HLT_DoubleMu6_v*")

electrontriggers  = cms.vstring("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*", "HLT_Ele17_CaloIdL_CaloIsoVL_Ele15_HFL_v*")

alltriggers       = muontriggers + electrontriggers

process.hlt = cms.EDFilter( "TriggerResultsFilter",
                            triggerConditions = alltriggers ,
                            #triggerConditions = cms.vstring("HLT_*"),         #test
                            hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
                            l1tResults = cms.InputTag( "gtDigis" ),
                            l1tIgnoreMask = cms.bool( False ),
                            l1techIgnorePrescales = cms.bool( False ),
                            daqPartitions = cms.uint32( 1 ),
                            throw = cms.bool( False )
                          )

# compute weight from prescale
process.WeightFromTrigger = cms.EDProducer('WeightFromTrigger',
    HLTLabel = cms.InputTag("TriggerResults::HLT"),
    UseCombinedPrescales = cms.bool(False),
    TriggerNames = alltriggers 
)

# add trigger information (trigTools)
from PhysicsTools.PatAlgos.tools.trigTools import *
switchOnTrigger(process)

# trigger matchers for various collections

# base matcher to define default values
defaultTriggerMatch = cms.EDProducer(
  "PATTriggerMatcherDRDPtLessByR"                 # match by DeltaR only, best match by DeltaR
, src     = cms.InputTag( "selectedPatMuons" )
, matched = cms.InputTag( "patTrigger" )          # default producer label as defined in PhysicsTools/PatAlgos/python/triggerLayer1/triggerProducer_cfi.py
, matchedCuts = cms.string( 'path( "HLT_DoubleMu6_v*" )' )
, maxDPtRel = cms.double( 0.5 )
, maxDeltaR = cms.double( 0.3 )
, resolveAmbiguities    = cms.bool( True )        # only one match per trigger object
, resolveByMatchQuality = cms.bool( True )        # take best match found per reco object: by DeltaR here (s. above)
)

process.selectedMuonsTriggerMatch = defaultTriggerMatch.clone(
        src         = cms.InputTag( "selectedPatMuons" )
        , matchedCuts = cms.string('path("HLT_DoubleMu6_v*")')
)

process.selectedElectronsTriggerMatch = defaultTriggerMatch.clone(
        src         = cms.InputTag( "selectedPatElectrons" )
        , matchedCuts = cms.string('path("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*")|| path("HLT_Ele17_CaloIdL_CaloIsoVL_Ele15_HFL_v*")')
)

# trigger object embedders for the same collections
process.selectedMuonsMatched = cms.EDProducer( "PATTriggerMatchMuonEmbedder",
        src     = cms.InputTag(  "selectedPatMuons" ),
        matches = cms.VInputTag( cms.InputTag('selectedMuonsTriggerMatch') )
    )

process.selectedElectronsMatched = cms.EDProducer( "PATTriggerMatchElectronEmbedder",
        src     = cms.InputTag(  "selectedPatElectrons" ),
        matches = cms.VInputTag( cms.InputTag('selectedElectronsTriggerMatch') )
    )

#---------------------------- MET
#------------------------------------------------------------------------------------------------------------------------------------------------

# add MET (for PF objects)
from PhysicsTools.PatAlgos.tools.metTools import *
addPfMET(process, 'PF')

#---------------------------- JET
#------------------------------------------------------------------------------------------------------------------------------------------------
#
from PhysicsTools.PatAlgos.tools.jetTools import *
# add kt4calo for comparison (should switch to some cone thing)
#addJetCollection(process,cms.InputTag('ak7PFJets'),
#                 'AK7', 'PF',
#                 doJTA        = True,
#                 doBTagging   = True,
#                 # for MC, use only L2Relative', 'L3Absolute', 'L5Flavor', 'L7Parton'
#                 #jetCorrLabel = ('AK7PF',['L1Offset','L2Relative', 'L3Absolute','L2L3Residual','L5Flavor','L7Parton']),  #   'L2L3Residual' as default
#                 jetCorrLabel = ('AK7PF',['L1Ofset','L2Relative', 'L3Absolute','L5Flavor','L7Parton']),  
#                 doType1MET   = False,
#                 doL1Cleaning = True,                 
#                 doL1Counters = False,
#                 genJetCollection=cms.InputTag("ak7GenJets"),
#                 doJetID      = True,
#                 jetIdLabel   = "ak7"
#
#                 )


# Use ak5PF instead of ak5Calo
##-------------------- Import the JEC services -----------------------
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
##-------------------- Import the Jet RECO modules -----------------------
process.load('RecoJets.Configuration.RecoPFJets_cff')
##-------------------- Turn-on the FastJet density calculation -----------------------
process.kt6PFJets.doRhoFastjet = True
##-------------------- Turn-on the FastJet jet area calculation for your favorite algorithm -----------------------
process.ak5PFJets.doAreaFastjet = True


switchJetCollection(process,cms.InputTag('ak5PFJets'),
                    doJTA  = True,
                    doBTagging   = True,
                    # for MC, use only L2Relative', 'L3Absolute', 'L5Flavor', 'L7Parton'
                    #jetCorrLabel = ('AK5PF',['L1Offset', 'L2Relative', 'L3Absolute','L2L3Residual','L5Flavor','L7Parton']),  #  'L2L3Residual' as default #
                    jetCorrLabel = ('AK5PF',['L1FastJet', 'L2Relative', 'L3Absolute','L5Flavor','L7Parton']), # 
                    doType1MET   = False,
                    genJetCollection=cms.InputTag("ak5GenJets"),
                    doJetID      = True,
                    #jetIdLabel   = "ak5"
                    )

#switchJetCollection(usePF2PAT(process, runPF2PAT=True, jetAlgo='AK5', runOnMC=False, postfix = "1", jetCorrections=('AK5PFchs', ['L1FastJet','L2Relative','L3Absolute']) ))
    
# selected Jets
process.selectedPatJets.cut      = 'pt > 15. & abs(eta) < 2.4 '
#process.selectedPatJetsAK7PF.cut = 'pt > 15. & abs(eta) < 2.4 '

process.patJets.addTagInfos = cms.bool( True )

#---------------------------- Leptons
#------------------------------------------------------------------------------------------------------------------------------------------------

from PhysicsTools.PatAlgos.cleaningLayer1.muonCleaner_cfi import *
from PhysicsTools.PatAlgos.cleaningLayer1.electronCleaner_cfi import *


#*************************************** Muons
#*******************************************************
# clean pat muons should be isolated for cleaning purpose
#process.cleanPatMuons.src = "selectedMuonsMatched"
process.cleanPatMuons.preselection = ('isGlobalMuon & isTrackerMuon & (trackIso+caloIso)/pt < 0.15')

# aditional collection of muons with no cuts
process.allMuons = process.cleanPatMuons.clone( preselection = 'pt > 5' )

# clean muons for direct analysis
process.looseMuons = process.cleanPatMuons.clone(preselection =
                                                 'isGlobalMuon & isTrackerMuon &'
                                                 'innerTrack.numberOfValidHits > 10 &'
                                                 '(trackIso+caloIso)/pt < 0.15 &'  # Z+jet choice 
                                                 #' trackIso < 3 &'                # VBTF choice
                                                 'pt > 10 &'
                                                 'abs(eta) < 2.4'
                                                 )
process.looseMuons.src = "selectedMuonsMatched"

process.tightMuons = process.cleanPatMuons.clone(preselection =
                                                 'isGlobalMuon & isTrackerMuon &'
                                                 'innerTrack.numberOfValidHits > 10 &'
                                                 'abs(dB) < 0.02 &' # why not 0.2 for 2mm ???
                                                 'normChi2 < 10 &'
                                                 'innerTrack.hitPattern.numberOfValidPixelHits > 0 &'
                                                 'numberOfMatches>1 &' # segments matched in at least two muon stations 
                                                 'globalTrack.hitPattern.numberOfValidMuonHits > 0 &' # one muon hit matched to the global fit
                                                 '(trackIso+caloIso)/pt < 0.15 &'  # Z+jet choice
                                                 #' trackIso < 3 &'                # VBTF choice
                                                 'pt > 20 &'
                                                 'abs(eta) < 2.1'
                                                 )
process.tightMuons.src = "selectedMuonsMatched"

process.matchedMuons = process.cleanPatMuons.clone(preselection =
                                                 'isGlobalMuon & isTrackerMuon &'
                                                 'innerTrack.numberOfValidHits > 10 &'
                                                 'abs(dB) < 0.02 &' # why not 0.2 for 2mm ???
                                                 'normChi2 < 10 &'
                                                 'innerTrack.hitPattern.numberOfValidPixelHits > 0 &'
                                                 'numberOfMatches>1 &' # segments matched in at least two muon stations 
                                                 'globalTrack.hitPattern.numberOfValidMuonHits > 0 &' # one muon hit matched to the global fit
                                                 '(trackIso+caloIso)/pt < 0.15 &'  # Z+jet choice
                                                 #' trackIso < 3 &'                # VBTF choice
                                                 'pt > 20 &'
                                                 'abs(eta) < 2.1 &'
                                                 'triggerObjectMatches.size > 0' #Trigger Match DeltaR and DeltapT/pT to be really tight

                                                 )
process.matchedMuons.src = "selectedMuonsMatched"

process.Ztighttight = cms.EDProducer("CandViewShallowCloneCombiner",
                                     decay = cms.string("matchedMuons@+ tightMuons@-"),
                                     cut = cms.string("mass > 12.0"), 
                                     name = cms.string('ztighttight'),
                                     roles = cms.vstring('matched', 'tight'),
                                     )

process.Ztightloose = cms.EDProducer("CandViewShallowCloneCombiner", 
                                     decay = cms.string("matchedMuons@+ looseMuons@-"), 
                                     cut = cms.string("60.0 < mass < 120.0"), 
                                     name = cms.string('ztightloose'),
                                     roles = cms.vstring('matched', 'loose')
                                     )

process.Zcleanclean = cms.EDProducer("CandViewShallowCloneCombiner", 
                                     decay = cms.string("cleanPatMuons@+ cleanPatMuons@-"), 
                                     cut = cms.string("60.0 < mass < 120.0"), 
                                     name = cms.string('zcleanclean'),
                                     roles = cms.vstring('clean1', 'clean2')
                                     )

#*************************************** Electrons
#*******************************************************
## Working point and electron id
#process.load("RecoEgamma.ElectronIdentification.electronIdSequence_cff")
#process.load("ElectroWeakAnalysis.WENu.simpleEleIdSequence_cff")
process.load("ZJetsAnalysis.ZJetsAnalysisV1.simpleEleIdSequence_cff")

process.patElectrons.addElectronID = cms.bool(True)

process.patElectrons.electronIDSources = cms.PSet(
    simpleEleId95relIso= cms.InputTag("simpleEleId95relIso"),
    simpleEleId90relIso= cms.InputTag("simpleEleId90relIso"),
    simpleEleId85relIso= cms.InputTag("simpleEleId85relIso")
    )

#process.patElectrons.electronIDSources = cms.PSet(
#    eidRobustLoose= cms.InputTag("RobustLoose"),
#    eidRobustTight= cms.InputTag("RobustTight"),
#    eidRobustHighEnergy= cms.InputTag("RobustHighEnergy")
#    )

process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)
#process.patElectronIDs = cms.Sequence(process.eIdSequence)
process.makePatElectrons = cms.Sequence(process.patElectronIDs*process.patElectronIsolation*process.patElectrons)

# clean pat Electrons should be isolated for cleaning purpose
#process.cleanPatElectrons.src = "selectedElectronsMatched"

process.cleanPatElectrons.preselection = 'electronID("simpleEleId85relIso") == 7 '
#process.cleanPatElectrons.preselection = 'electronID("RobustHighEnergy") == 7 '

# aditional collection of electrons with no cuts 
process.allElectrons = process.cleanPatElectrons.clone( preselection = 'pt > 5' ) 

# clean electrons for direct analysis
process.tightElectrons = cleanPatElectrons.clone( preselection =
                                                 'electronID("simpleEleId85relIso") == 7 &' # temp
                                                 #'electronID("RobustHighEnergy") == 7 &' # temp
                                                  # abs(eta)< 1.442 || 1.566 <abs(eta)<2.50 & included in WP85
                                                 'pt > 10. &'
                                                 'abs(eta) < 2.5 &'
                                                 #'abs(superCluster.energy * sin(2 * atan(exp(-1 *abs(superCluster.eta))))) > 20 &'
                                                 'abs(dB) < 0.02'
                                                 )
process.tightElectrons.src = "selectedElectronsMatched"

process.matchedElectrons = cleanPatElectrons.clone(preselection =
                                                   'electronID("simpleEleId85relIso") == 7 &' # temp
                                                   # abs(eta)< 1.442 || 1.566 <abs(eta)<2.50 & included in WP85
                                                   'pt > 25. &'
                                                   'abs(eta) < 2.5 &'
                                                   #'abs(superCluster.energy * sin(2 * atan(exp(-1 *abs(superCluster.eta))))) > 20 &'
                                                   'abs(dB) < 0.02 &'
                                                  'triggerObjectMatches.size > 0' #Trigger Match DeltaR and DeltapT/pT to be really tight

                                                   )
process.matchedElectrons.src = "selectedElectronsMatched"

process.Zelel = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("tightElectrons@+ matchedElectrons@-"),
                               cut = cms.string("mass > 12.0"),
                               name = cms.string('zelel'), 
                               roles = cms.vstring('tight', 'matched')
                              )

#-----------------tracks
process.patMuons.embedTrack = True
process.patElectrons.embedTrack = True

#------------------------------ Vertices 
#------------------------------------------------------------------------------------------------------------------------------------------------		
# vertex filter

from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import *
process.goodPV= offlinePrimaryVertices.clone()
process.goodPV.cut=cms.string('ndof > 4&'
                              'abs(z) <24&'
                              '!isFake &'
                              ' position.Rho <2 '
                              )


# additional collections and candidates
process.bjets = process.cleanPatJets.clone( preselection = 'bDiscriminator("simpleSecondaryVertexHighEffBJetTags") > 1.74' )

process.bbbar = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("bjets bjets"),
                               cut = cms.string("mass > 0"),
                               name = cms.string('bbar'),
                               roles = cms.vstring('b1', 'b2'),
                               checkCharge = cms.bool(False)
                              )

process.Zeej = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("Zelel selectedPatJets"),
                               cut = cms.string("mass > 0"),
                               name = cms.string('Zb'),
                               roles = cms.vstring('Z', 'j'),
                               checkCharge = cms.bool(False)
                              )

process.Zmmj = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("Ztighttight selectedPatJets"),
                               cut = cms.string("mass > 0"),
                               name = cms.string('Zbb'),
                               roles = cms.vstring('Z', 'b'),
                               checkCharge = cms.bool(False)
                              )

process.Zeeb = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("Zelel bjets"),
                               cut = cms.string("mass > 0"),
                               name = cms.string('Zb'),
                               roles = cms.vstring('Z', 'b'),
                               checkCharge = cms.bool(False)
                              )

process.Zmmb = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("Ztighttight bjets"),
                               cut = cms.string("mass > 0"),
                               name = cms.string('Zbb'),
                               roles = cms.vstring('Z', 'b'),
                               checkCharge = cms.bool(False)
                              )

process.Zeebb = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("Zelel bbbar"),
                               cut = cms.string("mass > 0"),
                               name = cms.string('Zbb'),
                               roles = cms.vstring('Z', 'b'),
                               checkCharge = cms.bool(False)
                              )

process.Zmmbb = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("Ztighttight bbbar"),
                               cut = cms.string("mass > 0"),
                               name = cms.string('Zbb'),
                               roles = cms.vstring('Z', 'b'),
                               checkCharge = cms.bool(False)
                              )

#------------------------------ E mu channel for ttbar
process.emu = cms.EDProducer("CandViewShallowCloneCombiner",
                              decay = cms.string("tightElectrons@+ tightMuons@-"),
                              cut = cms.string("mass > 12.0"),
                              name = cms.string('emu'),
                              roles = cms.vstring('tight1','tight2')
                              )



process.embb = cms.EDProducer("CandViewShallowCloneCombiner",
                             decay = cms.string("emu bbbar"),
                             cut = cms.string("mass > 0"),
                             name = cms.string('embb'),
                             roles = cms.vstring('Z', 'b'),
                             checkCharge = cms.bool(False)
                             )


#------------------------------ Filter
process.ZMuMuFilter = cms.EDFilter("CandViewCountFilter",
                                src = cms.InputTag("Ztighttight"),
                                minNumber = cms.uint32(1),
                                )

process.ZEEFilter = cms.EDFilter("CandViewCountFilter",
                                src = cms.InputTag("Zelel"),
                                minNumber = cms.uint32(1),
                                )

process.EMUFilter = cms.EDFilter("CandViewCountFilter",
                                src = cms.InputTag("emu"),
                                minNumber = cms.uint32(1),
                                )




#------------------------------ Sequence
#------------------------------------------------------------------------------------------------------------------------------------------------		
# vertex filter
# triggers based on loose leptons for skimming #in the talk
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
process.mutrigger = countPatMuons.clone(src = 'cleanPatMuons', minNumber = 2)
process.eltrigger = countPatElectrons.clone(src = 'cleanPatElectrons', minNumber = 2)
process.emutriggerp1= countPatMuons.clone(src = 'cleanPatMuons', minNumber = 1) 
process.emutriggerp2=countPatElectrons.clone(src = 'cleanPatElectrons', minNumber = 1)

#process.patDefaultSequence *= process.hltESSEcalSeverityLevel

# trigger matching and embedding should be done at the end of the sequence
process.patDefaultSequence *= process.selectedMuonsTriggerMatch
process.patDefaultSequence *= process.selectedMuonsMatched
process.patDefaultSequence *= process.selectedElectronsTriggerMatch
process.patDefaultSequence *= process.selectedElectronsMatched

# add user objects to patDefault
process.patDefaultSequence *= process.looseMuons
process.patDefaultSequence *= process.tightMuons
process.patDefaultSequence *= process.matchedMuons
process.patDefaultSequence *= process.allMuons
process.patDefaultSequence *= process.tightElectrons
process.patDefaultSequence *= process.matchedElectrons
process.patDefaultSequence *= process.allElectrons
process.patDefaultSequence *= process.goodPV

# compute weight from trigger presscale
process.patDefaultSequence *= process.WeightFromTrigger

# combine leptons to get Z candidates
process.patDefaultSequence *= process.Ztighttight
process.patDefaultSequence *= process.Ztightloose
process.patDefaultSequence *= process.Zcleanclean
process.patDefaultSequence *= process.Zelel
process.patDefaultSequence *= process.emu

# run additional collections and candidates
process.patDefaultSequence *= process.bjets
process.patDefaultSequence *= process.bbbar
process.patDefaultSequence *= process.Zmmj
process.patDefaultSequence *= process.Zeej
process.patDefaultSequence *= process.Zmmb
process.patDefaultSequence *= process.Zeeb
process.patDefaultSequence *= process.Zmmbb
process.patDefaultSequence *= process.Zeebb
process.patDefaultSequence *= process.embb


# Run it

process.p1 = cms.Path(process.hlt *process.scrapingVeto *process.kt6PFJets *process.ak5PFJets *process.patElectronIDs *process.patElectronIsolation *process.patDefaultSequence *process.mutrigger *process.ZMuMuFilter)
#process.p1 = cms.Path(process.hlt * process.scrapingVeto * process.kt6PFJets * process.ak5PFJets * process.patDefaultSequence * process.mutrigger * process.ZMuMuFilter)
process.p2 = cms.Path(process.hlt *process.scrapingVeto *process.kt6PFJets *process.ak5PFJets *process.patElectronIDs *process.patElectronIsolation *process.patDefaultSequence *process.eltrigger *process.ZEEFilter)
#process.p2 = cms.Path(process.hlt * process.scrapingVeto * process.kt6PFJets * process.ak5PFJets * process.patDefaultSequence * process.eltrigger * process.ZEEFilter)
process.p3 = cms.Path(process.hlt *process.scrapingVeto *process.kt6PFJets *process.ak5PFJets *process.patElectronIDs *process.patElectronIsolation *process.patDefaultSequence *process.emutriggerp1 *process.emutriggerp2 * process.EMUFilter)
#process.p3 = cms.Path(process.hlt * process.scrapingVeto * process.kt6PFJets * process.ak5PFJets * process.patDefaultSequence * process.emutriggerp1 * process.emutriggerp2 * process.EMUFilter)


process.out.SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p1', 'p2', 'p3'))


#process.out.outputCommands = cms.untracked.vstring('keep *')
tokeep_clean  = [ 
                  # keep all types of pat and Pat Jets, to access embedded PF candidates
                  'keep *_*atJets*_*_*',

                  # keep all tracks (not tracksextra)
                  'keep recoTracks_generalTracks_*_*',

                  'keep *_patMETs*_*_*',
                  'keep *_patTrigger*_*_*' ]

tokeep_clean += [
                 'keep *_tightElectrons_*_*',
                 'keep *_matchedElectrons_*_*',
                 'keep *_allElectrons*_*_*',
                 
                 'keep *_looseMuons_*_*',
                 'keep *_tightMuons_*_*',
                 'keep *_matchedMuons_*_*',
                 'keep *_allMuons*_*_*',

                 # keep the weight from trigger info
                 'keep *_WeightFromTrigger_*_*',

                 # keep candidates based on b jets
                 'keep *_bjets*_*_*',
                 'keep *_bbbar*_*_*',
                 
                 # keep Z candidates
                 'keep *_Z*_*_*',
                 
                 'keep *_emu_*_*',
                 'keep *_embb_*_*',
                 
                 'keep *_goodPV*_*_*' ]

# B-Tagging: is this needed ?
tokeep_clean += ['keep *_simpleSecondaryVertex*BJetTags*_*_PAT', 'keep *_trackCounting*BJetTags*_*_PAT']


process.out.outputCommands = cms.untracked.vstring('drop *', *tokeep_clean )
# process.out.outputCommands = cms.untracked.vstring( 'keep *' )


process.source.fileNames = [
    #"file:/scratch/lceard/store/dataset/data/DiLeptonMu-Dec22Skim_v2_0029_142EFD78-F010-E011-933A-003048D15D04.root"
    #"file:/home/fynu/lceard/storage/test/Run2011ADoubleMu_AOD_PromptReco/local.root"
    "file:/storage/data/cms/users/lceard/test/DoubleMuRun2011A_May10ReReco-v1_AOD_1.root"
    ]                                     

process.maxEvents.input = 100

process.out.fileName = 'LocalTestMu2011.root'

#process.out.dropMetaData = cms.untracked.string("ALL")

#process.out.fileName = 'Mu_2011A_153pb.root'
#process.out.fileName = 'Ele_2011A_153pb.root'

process.options.wantSummary = False