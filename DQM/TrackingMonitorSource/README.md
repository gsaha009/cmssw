cmsrel CMSSW_X_Y_Z \\
cd src/; cmsenv \\
git cms-init \\
git remote add ppalit-cmssw git@github.com:pritampalit/cmssw.git \\
git remote -v \\
git pull ppalit-cmssw branchName \\
git cms-addpkg DQM/TrackingMonitorSource \\
scram b