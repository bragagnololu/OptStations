# -*- coding: utf-8 -*-
"""
Created on Tue May 25 14:38:13 2021

@author: Luci
"""

import xarray as xr # import xarray
import numpy as np
import glob
import os

input_path = r'D:\Dados\Desktop\Sentinel5P\O3'
output_path = r'D:\Dados\Desktop\Sentinel5P\O3'
txt_file = r'D:\Dados\Desktop\Sentinel5P\O3\commands_list.txt'

searchcriteria = "S5*"
search = os.path.join(input_path, searchcriteria)

dirpaths = glob.glob(search)
res = 0.025

cmd_list = []

for file in dirpaths:
    data5p = xr.open_dataset(file, group='PRODUCT')
    
    lat_start = np.asarray((data5p['latitude'][0][0][0])) #first value of latitude
    lat_final = np.asarray((data5p['latitude'][-1][-1][-1]))  #last value of latitude
    
    long_start = np.asarray((data5p['longitude'][0][0][0])) #first value of latitude
    long_final = np.asarray((data5p['longitude'][-1][-1][-1]))  #last value of latitude
    
    lat_dif = abs(lat_final-lat_start)
    long_dif = abs(long_final-long_start)
    
    rows = round(lat_dif * (1/res)) 
    cols = round(long_dif * (1/res)) # 0.025 > 1/res > 40
    
    bin_spat = str((rows,float(lat_start),res,cols,float(long_start),res))
    
    filename = os.path.split(file)[1]
    output_file = output_path + '/C_' + filename 
    
    command = 'harpconvert -a "keep(latitude_bounds,longitude_bounds,O3_column_number_density);'+'bin_spatial'+bin_spat+';squash(time, (latitude_bounds,longitude_bounds));derive(latitude {latitude});derive(longitude {longitude});exclude(latitude_bounds,longitude_bounds,count,weight)"'  + ' ' + file + ' ' + output_file
    # CO: CO_column_number_density
    # NO2: tropospheric_NO2_column_number_density
    # O3: O3_column_number_density
    # SO2: SO2_column_number_density
    # CH4: CH4_column_volume_mixing_ratio_dry_air
    
    
    cmd_list.append(command)
    

with open(txt_file, 'w') as f:
    for item in cmd_list:
        f.write("%s\n" % item)    
        f.write("\n")

for cmd in cmd_list:
    os.system(cmd)


