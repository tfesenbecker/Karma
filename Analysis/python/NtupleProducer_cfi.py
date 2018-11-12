import FWCore.ParameterSet.Config as cms


dijetNtupleProducer = cms.EDProducer(
    "NtupleProducer",
    cms.PSet(
        # -- input sources
        dijetEventSrc = cms.InputTag("dijetEvents"),
        dijetRunSrc = cms.InputTag("dijetEvents"),
        dijetJetCollectionSrc = cms.InputTag("dijetCorrectedJets"),
        dijetMETCollectionSrc = cms.InputTag("dijetCorrectedMETs"),
        dijetGenParticleCollectionSrc = cms.InputTag("dijetGenParticles"),
        dijetJetTriggerObjectMapSrc = cms.InputTag("dijetJetTriggerObjectMaps"),

        # -- other configuration

        triggerEfficienciesFile = cms.string("trigger_efficiencies.root"),
        weightForStitching = cms.double(1.0),

        hltPaths = cms.vstring(
            "HLT_PFJet40",
            "HLT_PFJet60",
            "HLT_PFJet80",
            "HLT_PFJet140",
            "HLT_PFJet200",
            "HLT_PFJet260",
            "HLT_PFJet320",
            "HLT_PFJet400",
            "HLT_PFJet450",
            "HLT_PFJet500",
        ),

        jetIDSpec = cms.string("2016"),
        jetIDWorkingPoint = cms.string("TightLepVeto"),
    )
)
