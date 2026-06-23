import FWCore.ParameterSet.Config as cms
from Validation.RecoTau.ticlTauValidator_cfi import ticlTauValidator as _ticlTauValidator

# RECO: default
recoTiclTauValidator = _ticlTauValidator.clone(
    folder = cms.string("Tau/ticlTauValidator"),
    checkhlt = cms.bool(False),
    hltProcessName = cms.string("HLT")
)

# HLT
hltTiclTauValidator = _ticlTauValidator.clone(
    folder = cms.string("HLT/Tau/ticlTauValidator"),
    simTaus     = cms.InputTag("SimTauProducer"),
    TauProducer = cms.InputTag("hltHpsPFTauProducer"),
    pf          = cms.InputTag("hltParticleFlowTmp"),
    pfTmpBarrel = cms.InputTag("hltParticleFlowTmpBarrel"),
    jets        = cms.InputTag("hltAK4PFJets"),
    #ticlCandidates = cms.InputTag("hltTiclTrackstersMerge"),
    ticlCandidates = cms.InputTag("hltTiclCandidate"),
    simTracksters  = cms.InputTag("hltTiclSimTracksters","fromCPs"),
    simToRecoTracksterAssocByLCs = cms.InputTag(
        "hltAllTrackstersToSimTrackstersAssociationsByLCs",
        "hltTiclSimTrackstersfromCPsTohltTiclCandidate"
    ),
    #simToRecoTracksterAssocByLCs =
    #    cms.InputTag("hltAllTrackstersToSimTrackstersAssociationsByLCs",
    #                 "hltTiclSimTrackstersfromCPsTohltTiclTrackstersMerge"),
    recoToSimTracksterAssocByLCs = cms.InputTag(
        "hltAllTrackstersToSimTrackstersAssociationsByLCs",
        "hltTiclCandidateTohltTiclSimTrackstersfromCPs"
    ),
    #recoToSimTracksterAssocByLCs =
    #    cms.InputTag("hltAllTrackstersToSimTrackstersAssociationsByLCs",
    #                    "hltTiclTrackstersMergeTohltTiclSimTrackstersfromCPs"),
    genVisTaus = cms.InputTag("genVisTaus"),
    genParticles = cms.InputTag("genParticles"),
    hltProcessName = cms.string("HLT"),
    maxAssocScore = 0.6
)

