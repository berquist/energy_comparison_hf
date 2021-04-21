# energy_comparison_hf

How close can we get programs to agree on the Hartree-Fock energy? What about the CCSD(T) energy?

## Versions

* CFOUR 2.00beta (binary)
* DALTON 2020.0 (compiled)
* GAMESS 2014-05-1 (compiled)
* Molpro 2012.1.23 (compiled)
* NWChem 6.8 (binary)
* ORCA 4.2.1 (binary)
* Psi4 1.3.2 (binary)
* Q-Chem 5.3.2 (compiled)

## Requirements

To run `compare.py`, [cclib](https://github.com/cclib/cclib) is used.

To run the various packages,

``` bash
xcfour > cfour.out # rename cfour.in to ZMAT and place the GENBAS file in the same directory
dalton -noarch -nobackup dalton.dal
rungms gamess.inp
molpro
nwchem nwchem.in > nwchem.out
orca orca.in > orca.out
psi4 psi4.in
qchem qchem.in qchem.out
```

## TODO

- CCSD(T) for Molpro and GAMESS
