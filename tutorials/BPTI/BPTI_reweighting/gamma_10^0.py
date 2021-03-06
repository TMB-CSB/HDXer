#!/usr/bin/env python

import os

# Import the Maximum Entropy reweighting class
from HDXer.reweighting import MaxEnt

### Inputs ###

# A list of folders that contain the 'Contacts_' and 'Hbonds_' files from calc_hdx
folders = [ os.path.expandvars("$HDXER_PATH/tutorials/BPTI/BPTI_calc_hdx") ]
# The path to the target experimental data file
expt = os.path.expandvars("$HDXER_PATH/tutorials/BPTI/BPTI_expt_data/BPTI_expt_dfracs.dat")
# The path to the file containing intrinsic rates for each residue in your protein, generated by calc_hdx
rates = os.path.expandvars("$HDXER_PATH/tutorials/BPTI/BPTI_calc_hdx/BPTI_Intrinsic_rates.dat")
# A list of timepoints in the experimental data (in minutes)
times = [ 0.167, 1.0, 10.0, 120.0 ]


### Running reweighting ###

# This loop will run reweighting for gamma values from 1 x 10^0 to 9 x 10^0
# Adapt it as necessary
exponent = 0
basegamma = 10**exponent

for multiplier in range(1, 10):
    reweight_object = MaxEnt(do_reweight=True, do_params=False, stepfactor=0.001)
    reweight_object.run(gamma=(multiplier * basegamma), data_folders=folders, kint_file=rates, exp_file=expt, times=times, restart_interval=100, out_prefix=f'reweighting_gamma_{multiplier}x10^{exponent}_')
    print(f'Reweighting for gamma = {multiplier}x10^{exponent} completed')
    
# Help text describing options and how to call the reweighting functions
# is available in the docstrings of the MaxEnt class, e.g.:
#help(MaxEnt)
#help(MaxEnt.run)
