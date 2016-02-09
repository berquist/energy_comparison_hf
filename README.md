# energy_comparison_hf

## Versions

* CFOUR 2.00beta (binary)
* DALTON 2016.0 (compiled)
* GAMESS 2014-05-1 (compiled)
* MOLPRO 2012.1.23 (compiled)
* NWChem 6.0 (binary)
* ORCA 3.0.3 (binary)
* Psi 4.0.0-beta5 (compiled)
* Q-Chem 4.3.2 (compiled)

## Requirements

To run `compare.py`, [cclib](https://github.com/cclib/cclib) is used.

To run the various packages,

``` bash
xcfour > cfour.out # rename cfour.in to ZMAT and place the GENBAS file in the same directory
dalton dalton.dal
rungms gamess.inp
molpro
nwchem
orca orca.in > orca.out
psi4
qchem qchem.in qchem.out
```
