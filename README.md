# load_fcz
load Foldcomp fcz binary into PyMOL

Foldcomp
https://github.com/steineggerlab/foldcomp

PyMOL
https://github.com/schrodinger/pymol-open-source

# Usage
Before using this, install foldcomp via pip bundled with your PyMOL.
And then, 

```
run load_fcz.py
load_fcz yourfcz.fcz
```

# Advanced usage
If defining this function in the importing.py of (core of) PyMOL, it allows loading fcz files when launching PyMOL.
Example importing.py is available from this repo, but **be very careful** to replace your original importing.py by this because there may be version differences. Please take backups of your original importing.py before you edit it.

## How to modify your importing py

### 0. Install foldcomp

Install foldcomp by pip bundled with PyMOL. 

### 1. Add function (snippet below) to importing.py
```
import foldcomp
def load_fcz(filename, object=None, state=0, *, _self=cmd):
  with open(filename, "rb") as fcz:
  fcz_binary = fcz.read()
  (name, pdb) = foldcomp.decompress(fcz_binary)
  if (object == None):
    object = name
  cmd.read_pdbstr(pdb, object)
```  
### 2. Add load_fcz to the loader list

At the bottom of importing.py, you will find the loader list. Add there your load_fcz.
Example is below.

```
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
```
### 3. Check if it works

From the commandline, launch pymol specifying some fcz files

```
pymol test.fcz test2.fcz 
```

# License

Follows PyMOL's and foldcomp license. 

I'm not aware how to contribute to PyMOL software. Your advice will help. 
