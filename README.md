# DFT-Turbomole

## Description

With this Workflow, IR as well as UV/Vis spectra can be calculated for a large set of molecules using the [DFT-Turbomole WaNo](https://github.com/KIT-Workflows/DFT-Turbomole).

## Server setup

The code is based on python and the necessary virtual environment on the server is provided by Simstack. In addition, configuration files are necessary for the DFT-Turbomole and [Prepare-Screening](https://github.com/KIT-Workflows/Prepare-Screening) WaNos (cf. the respective README files).

## Required input

The required input consists of one or several molecules which can be provided in different formats

## Settings

- **Prepare-Screening**  
Chose your molecule(s) and the type of desired spectra.

- **DFT-Turbomole**  
Choose you DFT method (functional, basis set, dispersion correction, ...) in the second DFT-Turbomole WaNo ('DFT-Turbomole_1'). Note that UV/Vis emission spectra cannot be calculated when a COSMO model
is selected.

## Output

The output of this Workflow consists of (if chosen) one IR and one U/Vis spectrum (absorption and emission) per molecule.
