# load_fcz
load foldcomp fcz binary into PyMOL

# usage
run load_fcz.py

# Advanced usage
If defining this function in the importing.py of (core of) PyMOL, it allows loading fcz files when launching PyMOL.
Example importing.py is avaiable from this repo, but be vary careful to replace your original importing.py by this beucase there may be version differences.

## How to modify your importing py

### 0. Install foldcomp
Install foldcomp by pip bundled with PyMOL. 

### 1. add function (snippet below) to importing.py

import foldcomp
def load_fcz(filename, object=None, state=0, *, _self=cmd):
  with open(filename, "rb") as fcz:
  fcz_binary = fcz.read()
  (name, pdb) = foldcomp.decompress(fcz_binary)
  if (object == None):
    object = name
  cmd.read_pdbstr(pdb, object)
  
### 2. add load_fcz to the loader list
At the bottom of importing.py, you will find the loader list. Add there your load_fcz.

loadfunctions = {
        'mae': incentive_format_not_available_func,
        'pdbml': 'pymol.lazyio:load_pdbml',
        'cml': 'pymol.lazyio:load_cml',
        'mtz': load_mtz,
        'py': lambda filename, _self: _self.do("_ run %s" % filename),
        'pml': lambda filename, _self: _self.do("_ @%s" % filename),
        'pwg': _processPWG,
        'aln': 'pymol.seqalign:load_aln_multi',
        'fasta': _processFASTA,
        'png': 'pymol.viewing:load_png',
        'idx': load_idx,
        'pse': load_pse,
        'psw': load_pse,
        'ply': load_ply,
        'r3d': load_r3d,
        'cc1': load_cc1,
        'pdb': read_pdbstr,
        'stl': 'pymol.lazyio:read_stlstr',
        'dae': 'pymol.lazyio:read_collada',
        'fcz': load_fcz,

        # Incentive
        'vis': incentive_format_not_available_func,
        'moe': incentive_format_not_available_func,
        'phypo': incentive_format_not_available_func,
    }




I'm not aware how to contribute to PyMOL software. Your advice will help. 
