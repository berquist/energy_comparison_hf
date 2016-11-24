#!/usr/bin/env python3

import cclib
from cclib.io import ccopen

outputfilenames_scf = (
    ('CFOUR', 'cfour.out'),
    ('DALTON', 'dalton.out'),
    # ('Gaussian', 'g09.out'),
    ('GAMESS', 'gamess.out'),
    ('MOLPRO', 'molpro.out'),
    ('NWChem', 'nwchem.out'),
    ('ORCA', 'orca.out'),
    ('Psi4', 'psi4.out'),
    ('Q-Chem', 'qchem.out'),
)

outputfilenames_ccsd_t = (
    ('CFOUR', 'ccsd_t/cfour.out'),
    ('DALTON', 'ccsd_t/dalton.out'),
    # ('Gaussian', 'ccsd_t/g09.out'),
    # Some complaint about fewer virtuals than occupieds.
    # ('GAMESS', 'ccsd_t/gamess.out'),
    # ???
    # ('MOLPRO', 'ccsd_t/molpro.out'),
    ('NWChem', 'ccsd_t/nwchem.out'),
    ('ORCA', 'ccsd_t/orca.out'),
    ('Psi4', 'ccsd_t/psi4.out'),
    ('Q-Chem', 'ccsd_t/qchem.out'),
)

energies_scf = [
    (cclib.parser.daltonparser.DALTON, 'Converged SCF energy, gradient:', 5),
    (cclib.parser.gaussianparser.Gaussian, 'SCF Done:  E(RHF)', 4),
    (cclib.parser.gamessparser.GAMESS, 'FINAL RHF ENERGY IS', 4),
    (cclib.parser.molproparser.Molpro, '!RHF STATE 1.1 Energy', -1),
    (cclib.parser.nwchemparser.NWChem, 'Total SCF energy', -1),
    (cclib.parser.orcaparser.ORCA, 'Total Energy       :', 3),
    (cclib.parser.psiparser.Psi, '@RHF Final Energy:', 3),
    (cclib.parser.qchemparser.QChem, 'Total energy in the final basis set', -1),
]

energies_ccsd_t = [
    (cclib.parser.daltonparser.DALTON, 'Total energy CCSD(T):', -1),
    (cclib.parser.gaussianparser.Gaussian, ' CCSD(T)= ', -1),
    # (cclib.parser.gamessparser.GAMESS, '', ),
    # (cclib.parser.molproparser.Molpro, '', ),
    (cclib.parser.nwchemparser.NWChem, ' Total CCSD(T) energy:', -1),
    (cclib.parser.orcaparser.ORCA, 'E(CCSD(T))', -1),
    (cclib.parser.psiparser.Psi, '* CCSD(T) total energy', -1),
    (cclib.parser.qchemparser.QChem, ' CCSD(T) total energy', -1),
]

energy_types = [
    ('scf', energies_scf),
    ('ccsd(t)', energies_ccsd_t),
]


def search_file(fh, string_to_search, fieldnum):
    for line in fh:
        if string_to_search in line:
            return line.split()[fieldnum]


def get_energy_type(energy_type_str):
    for energy_type in energy_types:
        if energy_type[0] == energy_type_str:
            return energy_type[1]


def get_energy(outputfilename, energy_type_str='scf'):
    job = ccopen(outputfilename)
    energies = get_energy_type(energy_type_str)
    for (jobtype, string_to_search, fieldnum) in energies:
        if isinstance(job, jobtype):
            with open(outputfilename) as fh:
                energy = search_file(fh, string_to_search, fieldnum).replace('D', 'E')
            return float(energy)


def get_energy_nocclib(outputfilename, string_to_search, fieldnum):
    with open(outputfilename) as fh:
        energy = search_file(fh, string_to_search, fieldnum)
    return float(energy)


if __name__ == '__main__':

    scfenergies = []
    ccsdtenergies = []

    for (program, outputfilename) in outputfilenames_scf:
        if program == 'CFOUR':
            scfenergy = get_energy_nocclib(outputfilename, 'E(SCF)=', 1)
        else:
            scfenergy = get_energy(outputfilename, 'scf')
        scfenergies.append((program, scfenergy))

    scfenergies = sorted(scfenergies, key=lambda x: x[1])

    print('HF')
    for (program, scfenergy) in scfenergies:
        print(scfenergy, program)

    for (program, outputfilename) in outputfilenames_ccsd_t:
        if program == 'CFOUR':
            ccsdtenergy = get_energy_nocclib(outputfilename, 'E(CCSD(T))', 2)
        else:
            ccsdtenergy = get_energy(outputfilename, 'ccsd(t)')
        ccsdtenergies.append((program, ccsdtenergy))

    ccsdtenergies = sorted(ccsdtenergies, key=lambda x: x[1])

    print('CCSD(T)')
    for (program, ccsdtenergy) in ccsdtenergies:
        print(ccsdtenergy, program)
