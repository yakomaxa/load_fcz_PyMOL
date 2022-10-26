import foldcomp
from pymol import cmd
import glob

def load_fcz(filename):
    with open(filename, "rb") as fcz:
        fcz_binary = fcz.read()
        (name, pdb) = foldcomp.decompress(fcz_binary)
        print(name)
        cmd.read_pdbstr(pdb,name)

pymol.cmd.extend("load_fcz", load_fcz)
names_filenames_sc = lambda: cmd.Shortcut(cmd.get_names() + glob.glob('*'))
cmd.auto_arg[0]['load_fcz'] = [names_filenames_sc, 'filename or object name', '']
