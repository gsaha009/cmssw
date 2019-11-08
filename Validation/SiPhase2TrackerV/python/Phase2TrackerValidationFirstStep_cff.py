import FWCore.ParameterSet.Config as cms
from Validation.SiPhase2TrackerV.Phase2TrackerValidateDigi_cff import *

trackerphase2ValidationSource = cms.Sequence(pixDigiValid  + otDigiValid )
