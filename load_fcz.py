import foldcomp
import cmd from pymol
def load_fcz(filename, object=None, state=0, *, _self=cmd):
    with open(filename, "rb") as fcz:
        fcz_binary = fcz.read()
        (name, pdb) = foldcomp.decompress(fcz_binary)
        if (object == None):
            object = name
        cmd.read_pdbstr(pdb, object)

