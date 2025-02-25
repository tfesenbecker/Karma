import FWCore.ParameterSet.Config as cms


dijetNtupleProducer = cms.EDProducer(
    "NtupleProducer",
    cms.PSet(
        # -- input sources
        dijetEventSrc = cms.InputTag("dijetEvents"),
        dijetVertexCollectionSrc = cms.InputTag("dijetVertices"),
        dijetGeneratorQCDInfoSrc = cms.InputTag("dijetGeneratorQCDInfos"),
        dijetRunSrc = cms.InputTag("dijetEvents"),
        dijetJetCollectionSrc = cms.InputTag("dijetCorrectedJets"),
        dijetMETCollectionSrc = cms.InputTag("dijetCorrectedMETs"),
        dijetGenParticleCollectionSrc = cms.InputTag("dijetGenParticles"),
        dijetGenJetCollectionSrc = cms.InputTag("dijetGenJets"),
        dijetJetTriggerObjectMapSrc = cms.InputTag("dijetJetTriggerObjectMaps"),

        # -- other configuration

        #triggerEfficienciesFile = cms.string("trigger_efficiencies.root"),
        npuMeanFile = cms.string("npumean.txt"),
        minBiasCrossSection = cms.double(69.2),  # in mb

        pileupWeightFile = cms.string("nPUMean_ratio.root"),
        pileupWeightHistogramName = cms.string("pileup"),

        weightForStitching = cms.double(1.0),

        # YAML files specifying analysis binning
        flexGridFileDijetPtAve = cms.string("flexgrid_ys_yb_ptave.yml"),
        flexGridFileDijetMass = cms.string("flexgrid_ys_yb_mass.yml"),

        #: vector of PSets, one for each trigger path to consider
        # each PSet contains the following keys:
        #   - name (string):          the (unversioned) name of the trigger path, as it appears in the skim
        #   - hltThreshold (double):  value to use as HLT-level pT/pTave threshold when emulating this trigger
        #   - l1Threshold (double):   value to use as L1-level pT/pTave threshold when emulating this trigger
        #       NOTE: an event is considered to contain a trigger match for Reco-Level objects (i.e. jets) if
        #             *both* HLT and L1-level matches exist. An exception to this is when the HLT or L1 threshold
        #             is set to zero. In that case, an event is considered to contain a trigger match even if there
        #             are no matched objects on HLT or L1 levels, respectively.
        hltPaths = cms.VPSet(
            cms.PSet(name=cms.string("HLT_IsoMu24"),        hltThreshold=cms.double(0),   l1Threshold=cms.double(0)),
            #
            cms.PSet(name=cms.string("HLT_PFJet40"),        hltThreshold=cms.double(40),  l1Threshold=cms.double(0)),
            cms.PSet(name=cms.string("HLT_PFJet60"),        hltThreshold=cms.double(60),  l1Threshold=cms.double(35)),
            cms.PSet(name=cms.string("HLT_PFJet80"),        hltThreshold=cms.double(80),  l1Threshold=cms.double(60)),
            cms.PSet(name=cms.string("HLT_PFJet140"),       hltThreshold=cms.double(140), l1Threshold=cms.double(90)),
            cms.PSet(name=cms.string("HLT_PFJet200"),       hltThreshold=cms.double(200), l1Threshold=cms.double(120)),
            cms.PSet(name=cms.string("HLT_PFJet260"),       hltThreshold=cms.double(260), l1Threshold=cms.double(170)),
            cms.PSet(name=cms.string("HLT_PFJet320"),       hltThreshold=cms.double(320), l1Threshold=cms.double(170)),
            cms.PSet(name=cms.string("HLT_PFJet400"),       hltThreshold=cms.double(400), l1Threshold=cms.double(170)),
            cms.PSet(name=cms.string("HLT_PFJet450"),       hltThreshold=cms.double(450), l1Threshold=cms.double(170)),
            cms.PSet(name=cms.string("HLT_PFJet500"),       hltThreshold=cms.double(500), l1Threshold=cms.double(170)),
            #
            cms.PSet(name=cms.string("HLT_AK8PFJet40"),     hltThreshold=cms.double(40),  l1Threshold=cms.double(0)),
            cms.PSet(name=cms.string("HLT_AK8PFJet60"),     hltThreshold=cms.double(60),  l1Threshold=cms.double(35)),
            cms.PSet(name=cms.string("HLT_AK8PFJet80"),     hltThreshold=cms.double(80),  l1Threshold=cms.double(60)),
            cms.PSet(name=cms.string("HLT_AK8PFJet140"),    hltThreshold=cms.double(140), l1Threshold=cms.double(90)),
            cms.PSet(name=cms.string("HLT_AK8PFJet200"),    hltThreshold=cms.double(200), l1Threshold=cms.double(120)),
            cms.PSet(name=cms.string("HLT_AK8PFJet260"),    hltThreshold=cms.double(260), l1Threshold=cms.double(170)),
            cms.PSet(name=cms.string("HLT_AK8PFJet320"),    hltThreshold=cms.double(320), l1Threshold=cms.double(170)),
            cms.PSet(name=cms.string("HLT_AK8PFJet400"),    hltThreshold=cms.double(400), l1Threshold=cms.double(170)),
            cms.PSet(name=cms.string("HLT_AK8PFJet450"),    hltThreshold=cms.double(450), l1Threshold=cms.double(170)),
            cms.PSet(name=cms.string("HLT_AK8PFJet500"),    hltThreshold=cms.double(500), l1Threshold=cms.double(170)),
            #
            cms.PSet(name=cms.string("HLT_DiPFJetAve40"),   hltThreshold=cms.double(40),  l1Threshold=cms.double(0)),
            cms.PSet(name=cms.string("HLT_DiPFJetAve60"),   hltThreshold=cms.double(60),  l1Threshold=cms.double(0)),
            cms.PSet(name=cms.string("HLT_DiPFJetAve80"),   hltThreshold=cms.double(80),  l1Threshold=cms.double(60)),
            cms.PSet(name=cms.string("HLT_DiPFJetAve140"),  hltThreshold=cms.double(140), l1Threshold=cms.double(90)),
            cms.PSet(name=cms.string("HLT_DiPFJetAve200"),  hltThreshold=cms.double(200), l1Threshold=cms.double(120)),
            cms.PSet(name=cms.string("HLT_DiPFJetAve260"),  hltThreshold=cms.double(260), l1Threshold=cms.double(170)),
            cms.PSet(name=cms.string("HLT_DiPFJetAve320"),  hltThreshold=cms.double(320), l1Threshold=cms.double(170)),
            cms.PSet(name=cms.string("HLT_DiPFJetAve400"),  hltThreshold=cms.double(400), l1Threshold=cms.double(170)),
            cms.PSet(name=cms.string("HLT_DiPFJetAve500"),  hltThreshold=cms.double(500), l1Threshold=cms.double(170)),
        ),

        jetIDSpec = cms.string("2016"),
        jetIDWorkingPoint = cms.string("TightLepVeto"),
    )
)
