from Karma.Common.karmaPrelude_cff import *


# -- override CLI options for test
options.inputFiles="file://{}/{}".format(os.getenv("CMSSW_BASE"), "src/Karma/Skimming/test/FullMCSkim/testFullMCSkim_out.root")
options.isData=0
options.globalTag="80X_mcRun2_asymptotic_2016_TrancheIV_v6"
#options.edmOut="testFullAnalysis_out.root"  # no EDM output
options.maxEvents=-1 #10 #000
options.dumpPython=1
options.jecVersion = "Summer16_07Aug2017_V11"


# -- must be called at the beginning
process = createProcess("DIJETANA", num_threads=1)


from Karma.DijetAnalysis.dijetAnalysis_cff import DijetAnalysis

# -- configure output ROOT file used by TFileService
process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string("output.root"),
    closeFileFast = cms.untracked.bool(True),
)

ana = DijetAnalysis(process, is_data=options.isData, jec_version=options.jecVersion)

ana.configure()



# -- must be called at the end
finalizeAndRun(process, outputCommands=['drop *'])


## selective writeout based on path decisions
#process.edmOut.SelectEvents = cms.untracked.PSet(
#    SelectEvents = cms.vstring('path')
#)
