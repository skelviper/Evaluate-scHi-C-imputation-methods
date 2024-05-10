import sys
sys.path.append("/shareb/zliu/analysis/")
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd



import glob
import re



import cooler
from scipy import stats

from CHARMtools import Cell3D
import imp
imp.reload(Cell3D)
from CHARMtools import imputation
imp.reload(imputation)

# target = "Science2018"


imputed_matrix_dir = f"/shareb/mliu/evaluate_impute/data/imputed_data/ctg"

#cell
# target = "Cell2020"
# print(target)
# downsample_matrix_dir = f"/shareb/mliu/evaluate_impute/data/simulation_hic/{target}/hic/matrix"
# for group in range(1,5):
#     print(group)
#     downsample_matrix = np.load(f"{downsample_matrix_dir}/{target}_sample_matrix{group}.npy")
#     downsample_matrix = downsample_matrix[0:100,:]
#     imputed_matrices = np.array([imputation.ctg_impute_v2(mat) for mat in downsample_matrix])
#     #对imputed_matrices中的每一项取-np.log2
    
#     for mat in imputed_matrices:
#         np.fill_diagonal(mat, np.nan)

#     imputed_matrices = -1*np.log2(imputed_matrices)
#     print(imputed_matrices.shape)
#     #保存
#     save_path = f"{imputed_matrix_dir}/ctg_imputed_{target}_group{group}.npy"
#     print(save_path)
#     np.save(save_path, imputed_matrices)
# sc_matrix_dir = f"/shareb/mliu/evaluate_impute/data/real_sc_hic/Ramani/cooler"
chr_list = ["chr1","chr2","chr3","chr4","chr5","chr6","chr7","chr8","chr9","chr10","chr11","chr12","chr13","chr14","chr15","chr16","chr17","chr18","chr19","chr20","chr21","chr22"]
sc_matrix_dir = f"/shareb/mliu/evaluate_impute/data/real_sc_hic/Ramani/cooler"
for chr in chr_list:
    print(chr)
    imputed_matrices_list = []
    for cell in range(0,620):
        print(f"cell{cell}")
        clr = cooler.Cooler(f"{sc_matrix_dir}/cell{cell}.cool")
        matrix_chr = clr.matrix(balance=False).fetch(chr)
        matrix_chr_imputed = imputation.ctg_impute_v2(matrix_chr) 
        imputed_matrices_list.append(matrix_chr_imputed)
    imputed_matrices_array = np.array(imputed_matrices_list)
    print(imputed_matrices_array.shape)
    save_path = f"{imputed_matrix_dir}/schicluster_imputed_Ramani_{chr}.npy"
    np.save(save_path, imputed_matrices_array)
