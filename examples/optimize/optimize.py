#!/usr/bin/env python3

import re
import os
import subprocess

import numpy as np

from ngsim import *


outputdir   = "data"
outputfile  = "output.csv"
circuitfile = "netlist/netlist.sp"

tf_sim = Simulation( cmd=tf("v(out,0)", "V0"), prints="transfer_function" )

sim = [tf_sim]

ctl = ControlSectionLogical(sim, outputfile=outputfile, outputdir=outputdir)
cir = CircuitSection(circuitfile)


def costfunc(result, pars):
    gain  = result["tf"]["transfer_function"] 
    gain_nom  = lim_bound(gain,  48,   52)
    cost =  gain_nom
    return cost
 

bound_lut = {"w":  (0.5, 5), "r":  (1e3, 100e3)}


instances = [ {"variable": "var1", "bound": "w", "instances": ["xm1", "xm2"]}, 
              {"variable": "var2", "bound": "r", "instances": ["rf1", "rf2"]},] 


bounds = create_bounds(instances, bound_lut)
optimizer = Optimizer(costfunc, bounds, cir, ctl, instances)
result = optimizer.opt_de()
