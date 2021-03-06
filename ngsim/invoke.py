# Ngsim - A ngspice simulation interface using python
# Copyright (C) 2022 Christoph Weiser
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import subprocess

def run_simulation(netlist):
    """ Run a spice netlist straight into ngspice

    Required inputs:
    ----------------
    netlist(str, list):     netlist to be run


    Returns
    ----------------
    output(list):           list of string with the output
                            generated by ngpsice.
    """
    if isinstance(netlist, list):
        netlist = "".join(netlist)
    p = subprocess.Popen(["ngspice", "-s"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    capture = p.communicate(input=netlist.encode())
    p_status = p.wait()
    output = capture[0].decode().splitlines()
    return output


def run_file(filename):
    """ Run a spice simulation directly from file.

    Required inputs:
    ----------------
    filename (str):     name/path of the simulation netlist
                        file.

    Returns
    ----------------
    output(list):       list of string with the output
                        generated by ngspice.
    """
    with open(filename, "r") as infile:
        netlist = infile.read()
    output = run_simulation(netlist)
    return output
