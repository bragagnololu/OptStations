# OptStations

OptSations é um repositório que contém os códigos utilizados para desenvolvimento do estudo chamado: **A PRACTICAL APPROACH FOR THE OPTIMIZATION OF AIR MONITORING NETWORKS USING SATELLITE DATA**.

The work aimed to present an optimization methodology for the allocation of air pollution monitoring stations using information from the Sentinel-5P satellite and the open source language Python.

## Codes in this repository

The repository contains a *.py file* that converts the images obtained by the Sentinel-5P satellite database into files compatible with QGIS, where they can be processed to be used in the next optimization steps. Also, the repository has a *Jupyter Notebook* that presents step-by-step optimization using the PulP library and GLPK solver.

### build_command.py

Requirements: xarray, numpy, glob, os, harp libs (https://stcorp.github.io/harp/doc/html/index.html)
 
  
    input_path = '' # path where the Sentinel 5P files are (.NC files)
    output_path = '' # path to save the processed images
    txt_file = '/commands_list.txt' # path to save .txt files with harp command
    
    res = 0.025 # resolution to save the images (the smaller, the heavier the file size!)
    
More information regarding the methodology can be found in the paper. Data for code reproduction are located in the DATA.rar file.
