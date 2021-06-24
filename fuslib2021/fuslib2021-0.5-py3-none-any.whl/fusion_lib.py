from aux import read_raster, writeimage
import math
import numpy as np
import gdal
import os
from tkinter import filedialog
import tkinter as tk
import idlwrap
import statsmodels.api as sm

from params import (w, num_class, num_similar_pixel, DN_min, DN_max, background, patch_long,
                        windowSize,logWeight,mid_idx, numberClass,spatImp,specUncertainty,tempUncertainty,tempst,sizeSlices)

import zarr
import dask.array as da
import rasterio
import matplotlib.pyplot as plt


pathst='' #global variable to set path for starfm results

def processingImages(algorit):
    if algorit=='EST':
        root = tk.Tk()
        root.withdraw()
            
        # set path of a folder to store temporary files
        temp_file = filedialog.askdirectory(title=u"Set the temporary folder where to store the results")
        
        # open the fine image of the first pair
        path1 = filedialog.askopenfilename(title=u"Open the fine image of the first pair:")
        suffix = os.path.splitext(path1)[-1]
        nl, ns, FileName1 = read_raster(path1)
        orig_ns = ns
        orig_nl = nl
        fp = gdal.Open(path1)
        nb = fp.RasterCount
        
        n_nl = math.ceil(orig_nl / patch_long)
        n_ns = math.ceil(orig_ns / patch_long)
        
        ind_patch = np.zeros((n_nl * n_ns, 4), dtype=np.int)
        
        for i_ns in range(0, n_ns):
            for i_nl in range(0, n_nl):
                ind_patch[n_ns * i_nl + i_ns, 0] = i_ns * patch_long
                ind_patch[n_ns * i_nl + i_ns, 1] = np.min([ns - 1, (i_ns + 1) * patch_long - 1])
                ind_patch[n_ns * i_nl + i_ns, 2] = i_nl * patch_long
                ind_patch[n_ns * i_nl + i_ns, 3] = np.min([nl - 1, (i_nl + 1) * patch_long - 1])
        
        def forImagenesLeidas(tempOut, file, n_nl, n_ns,ind_patch, suffix, fp, path1):
            for isub in range(0, n_nl * n_ns):
                col1 = ind_patch[isub, 0]
                col2 = ind_patch[isub, 1]
                row1 = ind_patch[isub, 2]
                row2 = ind_patch[isub, 3]
                data = file[:, row1:row2 + 1, col1:col2 + 1]
                out_name = tempOut + str(isub + 1) + suffix
                fp = path1
                writeimage(data, out_name, fp)
                
            
        tempoutname = temp_file + '//temp_F1'
        forImagenesLeidas(tempoutname,FileName1, n_nl, n_ns,ind_patch, suffix, fp, path1)
        
        
        # open the coarse image of the first pair
        path2 = filedialog.askopenfilename(title=u"Open the coarse image of the first pair:")
        _, _, FileName2 = read_raster(path2)
        
        tempoutname = temp_file + '//temp_C1'
        forImagenesLeidas(tempoutname,FileName2, n_nl, n_ns,ind_patch, suffix, fp, path1)
        
        
        # open the fine image of the second pair
        path3 = filedialog.askopenfilename(title=u"Open the fine image of the second pair:")
        _, _, FileName3 = read_raster(path3)
        
        tempoutname = temp_file + '//temp_F2'
        forImagenesLeidas(tempoutname,FileName3, n_nl, n_ns,ind_patch, suffix, fp, path1)
        
        
        # open the coarse image of the second pair
        path4 = filedialog.askopenfilename(title=u"Open the coarse image of the second pair:")
        _, _, FileName4 = read_raster(path4)
        
        tempoutname = temp_file + '//temp_C2'
        forImagenesLeidas(tempoutname,FileName4, n_nl, n_ns,ind_patch, suffix, fp, path1)
        
        
        # open the coarse image of the prediction time
        path5 = filedialog.askopenfilename(title=u"Open the coarse image of the prediction time:")
        _, _, FileName5 = read_raster(path5)
        
        tempoutname = temp_file + '//temp_C0'
        forImagenesLeidas(tempoutname,FileName5, n_nl, n_ns,ind_patch, suffix, fp, path1)
        
        executeEST(nb,n_nl,n_ns,ind_patch, suffix, fp, path1, path2, path3, path4, path5,temp_file,orig_ns, orig_nl)
        

        # -tif final result
        #plot the results
        
        try:
            filename= temp_file + '//predictionEST1.tif'
            productoES=rasterio.open(filename)
        except:
            filename= temp_file + '//predictionEST1'
            productoES=rasterio.open(filename)
            
        
        plt.imshow(productoES.read(1))
        plt.gray()
        plt.show()
        return productoES
        
    elif algorit=='ST':
        #start = time.time()
        root = tk.Tk()
        root.withdraw()
        
        
        temp_file = filedialog.askdirectory(title=u"Set the temporary folder where to store the results") 
        print(temp_file)
        
        global pathst
        pathst=temp_file 
        print(pathst)


        p1=filedialog.askopenfilename(title=u"Open the fine image of the first pair:")
        p2=filedialog.askopenfilename(title=u"Open the coarse image of the first pair:")
        p3=filedialog.askopenfilename(title=u"Open the coarse image of the prediction time:")
        
        #Set the path where the images are stored
        product = rasterio.open(p1)
        profile = product.profile
        LandsatT0 = rasterio.open(p1).read(1)
        MODISt0 = rasterio.open(p2).read(1)
        MODISt1 = rasterio.open(p3).read(1)
        
        # Set the path where to store the temporary results
        path_fineRes_t0 = temp_file+'Tiles_fineRes_t0/'
        path_coarseRes_t0 = temp_file+'Tiles_fineRes_t0/Tiles_coarseRes_t0/'
        path_coarseRes_t1 = temp_file+'Tiles_fcoarseRes_t1/'
        
        # Flatten and store the moving window patches
        partition(LandsatT0, path_fineRes_t0)
        partition(MODISt0, path_coarseRes_t0)
        partition(MODISt1, path_coarseRes_t1)
        
        
        #print ("Done partitioning!")
        # Stack the the moving window patches as dask arrays
        S2_t0 = da_stack(path_fineRes_t0, LandsatT0.shape)
        S3_t0 = da_stack(path_coarseRes_t0, MODISt0.shape)
        S3_t1 = da_stack(path_coarseRes_t1, MODISt1.shape)
        
        shape = (sizeSlices, LandsatT0.shape[1])
        #print ("Done stacking!")
        
        return executeST(LandsatT0,MODISt0,MODISt1,S2_t0,S3_t0,S3_t1,shape,profile,product,temp_file)
      
    



def executeEST(nb,n_nl,n_ns,ind_patch, suffix, fp, path1, path2, path3, path4, path5,temp_file,orig_ns, orig_nl):

    print('there are total', n_nl*n_ns, 'blocks')
    
    for isub in range(0, n_nl * n_ns):
    
        # open each block image
    
        FileName = temp_file + '//temp_F1' + str(isub + 1) + suffix
        nl, ns, fine1 = read_raster(FileName)
    
        FileName = temp_file + '//temp_C1' + str(isub + 1) + suffix
        _, _, coarse1 = read_raster(FileName)
    
        FileName = temp_file + '//temp_F2' + str(isub + 1) + suffix
        _, _, fine2 = read_raster(FileName)
    
        FileName = temp_file + '//temp_C2' + str(isub + 1) + suffix
        _, _, coarse2 = read_raster(FileName)
    
        FileName = temp_file + '//temp_C0' + str(isub + 1) + suffix
        _, _, coarse0 = read_raster(FileName)
    
        fine0 = np.zeros((nb, nl, ns)).astype(float)    # place the blended result
    
        # row index of images
        row_index = np.zeros((nl, ns)).astype(int)
        for i in range(0, nl):
            row_index[i, :] = i
    
        # column index of images
        col_index = np.zeros((nl, ns)).astype(int)
        for i in range(0, ns):
            col_index[:, i] = i
    
        # compute the threshold of similar pixel seeking
        similar_th = np.zeros((2, nb)).astype(float)
        for iband in range(0, nb):
            similar_th[0, iband] = np.std(fine1[iband, :, :] * 2.0 / num_class)
            similar_th[1, iband] = np.std(fine2[iband, :, :] * 2.0 / num_class)
    
        # compute the distance of each pixel in the window with the target pixel (integrate window)
        D_temp1 = w - np.tile((idlwrap.indgen(w*2+1)), (int(w*2+1), 1))
        d1 = np.power(D_temp1, 2)
        D_temp2 = w - np.tile(idlwrap.indgen(1, w*2+1), (1, int(w*2+1)))
        d2 = np.power(D_temp2, 2)
        D_D_all = 1.0 + np.sqrt(d1 + d2) / float(w)
        D_D_all = D_D_all.flatten()
    
        # find interaction of valid pixels of all input images: exclude missing pixels and background
        valid_index = np.zeros((nl, ns)).astype(int)
        ind_valid = np.where((fine1[0, :, :] != background) & (fine2[0, :, :] != background) & (coarse1[0, :, :] != background) \
            & (coarse2[0, :, :] != background) & (coarse0[0, :, :] != background))
        num_valid = int(int(np.size(ind_valid)) / len(ind_valid))
        if num_valid > 0:
            valid_index[ind_valid] = 1  # mark good pixels in all images
    
        for j in range(0, nl):    # retrieve each target pixel
            for i in range(0, ns):
    
                if valid_index[j, i] == 1:     # do not process the background
    
                    ai = int(np.max([0, i - w]))
                    bi = int(np.min([ns - 1, i + w]))
                    aj = int(np.max([0, j - w]))
                    bj = int(np.min([nl - 1, j + w]))
    
                    ind_wind_valid = np.where((valid_index[aj:bj+1, ai:bi+1]).ravel() == 1)
                    position_cand = np.zeros((bi-ai+1)*(bj-aj+1)).astype(int) + 1    # place the location of each similar pixel
                    similar_cand = np.zeros((bi-ai+1)*(bj-aj+1)).astype(int)    # place the similarity measure between each pixel and the target pixel
                    row_wind = row_index[aj:bj+1, ai:bi+1]
                    col_wind = col_index[aj:bj+1, ai:bi+1]
    
                    # searching for similar pixels
                    for ipair in [0, 1]:
                        for iband in range(0, nb):
                            cand_band = np.zeros((bi-ai+1)*(bj-aj+1)).astype(int)
                            if ipair == 0:
                                S_S = np.abs(fine1[iband, aj:bj+1, ai:bi+1] - fine1[iband, j, i])
                            elif ipair == 1:
                                S_S = np.abs(fine2[iband, aj:bj + 1, ai:bi + 1] - fine2[iband, j, i])
                            similar_cand = similar_cand + S_S.ravel() / ((similar_th[ipair, iband]).ravel() + 0.00000001)
                            ind_cand = np.where(S_S.ravel() < similar_th[ipair, iband])
                            cand_band[ind_cand] = 1
                            position_cand = position_cand * cand_band
    
                    cand_band = 0
                    indcand0 = np.where((position_cand != 0) & ((valid_index[aj:bj+1, ai:bi+1]).ravel() == 1))   # select similar pixel initially
                    number_cand0 = int(int(np.size(indcand0)) / len(indcand0))
                    order_dis = np.argsort(similar_cand[indcand0]).astype(int)
                    number_cand = int(np.min([number_cand0, num_similar_pixel]))
                    indcand = indcand0[0][order_dis[0:number_cand]]
    
                    if number_cand > 5:    # compute the correlation
                        S_D_cand = np.zeros(number_cand).astype(float)
                        x_cand = (col_wind.ravel())[indcand]
                        y_cand = (row_wind.ravel())[indcand]
                        finecand = np.zeros((nb*2, number_cand)).astype(float)
                        coarsecand = np.zeros((nb*2, number_cand)).astype(float)
    
                        for ib in range(0, nb):
                            finecand[ib, :] = (fine1[ib, aj:bj+1, ai:bi+1]).ravel()[indcand]
                            finecand[ib+nb, :] = (fine2[ib, aj:bj+1, ai:bi+1]).ravel()[indcand]
                            coarsecand[ib, :] = (coarse1[ib, aj:bj+1, ai:bi+1]).ravel()[indcand]
                            coarsecand[ib+nb, :] = (coarse2[ib, aj:bj+1, ai:bi+1]).ravel()[indcand]
    
                        if nb == 1:   # for images with one band, like NDVI
                            S_D_cand = 1.0 - 0.5*(nb.abs((finecand[0, :]-coarsecand[0, :]) / (finecand[0, :]+coarsecand[0, :])) +
                                                  np.abs((finecand[1, :]-coarsecand[1, :]) / (finecand[1, :]+coarsecand[1, :])))
                        else:
                            # for images with multiple bands
                            sdx = np.std(finecand, axis=0, ddof=1)
                            sdy = np.std(coarsecand, axis=0, ddof=1)
                            meanx = np.mean(finecand, axis=0)
                            meany = np.mean(coarsecand, axis=0)
    
                            x_meanx = np.zeros((nb*2, number_cand)).astype(float)
                            y_meany = np.zeros((nb*2, number_cand)).astype(float)
                            for ib in range(0, nb*2):
                                x_meanx[ib, :] = finecand[ib, :] - meanx
                                y_meany[ib, :] = coarsecand[ib, :] - meany
    
                            S_D_cand = nb*2.0*np.mean(x_meanx*y_meany, axis=0) / (sdx*sdy) / (nb*2.0-1)
    
                        ind_nan = np.where(S_D_cand != S_D_cand)
                        num_nan = int(int(np.size(ind_nan)) / len(ind_nan))
                        if num_nan > 0:
                            S_D_cand[ind_nan] = 0.5    # correct the NaN value of correlation
    
                        D_D_cand = np.zeros(number_cand).astype(float)   # spatial distance
                        if (bi-ai+1)*(bj-aj+1) < (w*2.0+1)*(w*2.0+1):   # not an integrate window
                            D_D_cand = 1.0 + np.sqrt((i-x_cand)**2+(j-y_cand)**2) / w
                        else:
                            D_D_cand[0:number_cand] = D_D_all[indcand]      # integrate window
    
                        C_D = (1.0-S_D_cand) * D_D_cand + 0.0000001           # combined distance
                        weight = (1.0/C_D)/np.sum(1.0/C_D)
    
                        for ib in range(0, nb):   # compute V
                            fine_cand = np.hstack(((fine1[ib, aj:bj+1, ai:bi+1]).ravel()[indcand], (fine2[ib, aj:bj+1, ai:bi+1]).ravel()[indcand]))
                            coarse_cand = np.hstack(((coarse1[ib, aj:bj+1, ai:bi+1]).ravel()[indcand], (coarse2[ib, aj:bj+1, ai:bi+1]).ravel()[indcand]))
                            coarse_change = np.abs(np.mean((coarse1[ib, aj:bj+1, ai:bi+1]).ravel()[indcand]) - np.mean((coarse2[ib, aj:bj+1, ai:bi+1]).ravel()[indcand]))
                            if coarse_change >= DN_max*0.02:  # to ensure changes in coarse image large enough to obtain the conversion coefficient
    
                                X = coarse_cand.reshape(-1, 1)
                                Y = fine_cand.reshape(-1, 1)
                                XX = sm.add_constant(X)
                                model = sm.OLS(Y, XX).fit()
                                regress_result = model.params
                                sig = model.f_pvalue
    
                                # correct the result with no significancy or inconsistent change or too large value
                                if sig <= 0.05 and 0 < regress_result[1] <= 5:
                                    V_cand = regress_result[1]
                                else:
                                    V_cand = 1.0
    
                            else:
                                V_cand = 1.0
    
                            # compute the temporal weight
                            difc_pair1 = np.abs(np.mean((coarse0[ib, aj:bj+1, ai:bi+1]).ravel()[ind_wind_valid])-np.mean((coarse1[ib, aj:bj+1, ai:bi+1]).ravel()[ind_wind_valid]))+0.01**5
                            difc_pair2 = np.abs(np.mean((coarse0[ib, aj:bj+1, ai:bi+1]).ravel()[ind_wind_valid])-np.mean((coarse2[ib, aj:bj+1, ai:bi+1]).ravel()[ind_wind_valid]))+0.01**5
                            T_weight1 = (1.0/difc_pair1) / (1.0/difc_pair1+1.0/difc_pair2)
                            T_weight2 = (1.0/difc_pair2) / (1.0/difc_pair1+1.0/difc_pair2)
    
                            # predict from pair1
                            coarse0_cand = (coarse0[ib, aj:bj+1, ai:bi+1]).ravel()[indcand]
                            coarse1_cand = (coarse1[ib, aj:bj+1, ai:bi+1]).ravel()[indcand]
                            fine01 = fine1[ib, j, i] + np.sum(weight * V_cand * (coarse0_cand-coarse1_cand))
                            # predict from pair2
                            coarse2_cand = (coarse2[ib, aj:bj+1, ai:bi+1]).ravel()[indcand]
                            fine02 = fine2[ib, j, i] + np.sum(weight * V_cand * (coarse0_cand-coarse2_cand))
                            # the final prediction
                            fine0[ib, j, i] = T_weight1 * fine01 + T_weight2 * fine02
                            # revise the abnormal prediction
                            if fine0[ib, j, i] <= DN_min or fine0[ib, j, i] >= DN_max:
                                fine01 = np.sum(weight*(fine1[ib, aj:bj+1, ai:bi+1]).ravel()[indcand])
                                fine02 = np.sum(weight*(fine2[ib, aj:bj+1, ai:bi+1]).ravel()[indcand])
                                fine0[ib, j, i] = T_weight1 * fine01 + T_weight2 * fine02
    
                    else:  # for the case of no enough similar pixel selected
    
                        for ib in range(0, nb):
                            # compute the temporal weight
                            difc_pair1 = np.mean((coarse0[ib, aj:bj+1, ai:bi+1]).ravel()[ind_wind_valid])-np.mean((coarse1[ib, aj:bj+1, ai:bi+1]).ravel()[ind_wind_valid])+0.01**5
                            difc_pair1_a = np.abs(difc_pair1)
                            difc_pair2 = np.mean((coarse0[ib, aj:bj+1, ai:bi+1]).ravel()[ind_wind_valid])-np.mean((coarse2[ib, aj:bj+1, ai:bi+1]).ravel()[ind_wind_valid])+0.01**5
                            difc_pair2_a = np.abs(difc_pair2)
                            T_weight1 = (1.0/difc_pair1_a) / (1.0/difc_pair1_a+1.0/difc_pair2_a)
                            T_weight2 = (1.0/difc_pair2_a) / (1.0/difc_pair1_a+1.0/difc_pair2_a)
                            fine0[ib, j, i] = T_weight1 * (fine1[ib, j, i] + difc_pair1) + T_weight2 * (fine2[ib, j, i] + difc_pair2)
    
        print('finish ', str(isub + 1), 'block')
        tempoutname1 = temp_file + '//predictionEST'
        Out_Name = tempoutname1 + str(isub + 1) + suffix 
        fp = path1
        writeimage(fine0, Out_Name, fp)
    
    # # ***************************************************************
    # # mosaic all the blended patch
    
    datalist = []
    minx_list = []
    maxX_list = []
    minY_list = []
    maxY_list = []
    
    for isub in range(0, n_ns * n_nl):
        out_name = temp_file + '//predictionEST' + str(isub+1) + suffix 
        datalist.append(out_name)
    
        col1 = ind_patch[isub, 0]
        col2 = ind_patch[isub, 1]
        row1 = ind_patch[isub, 2]
        row2 = ind_patch[isub, 3]
    
        minx_list.append(col1)
        maxX_list.append(col2)
        minY_list.append(row1)
        maxY_list.append(row2)
    
    minX = min(minx_list)
    minY = min(minY_list)
    
    xOffset_list = []
    yOffset_list = []
    i = 0
    for data in datalist:
        xOffset = int(minx_list[i] - minX)
        yOffset = int(minY_list[i] - minY)
        xOffset_list.append(xOffset)
        yOffset_list.append(yOffset)
        i += 1
    
    in_ds = gdal.Open(path1)
    path = os.path.splitext(path5)[0] + "_ESTARFM_FAST" + suffix
    if suffix == '.tif':
        driver = gdal.GetDriverByName("GTiff")
    elif suffix == "":
        driver = gdal.GetDriverByName("ENVI")
    dataset = driver.Create(path, orig_ns, orig_nl, nb, gdal.GDT_Float32)
    
    i = 0
    for data in datalist:
        nl, ns, datavalue = read_raster(data)
        for j in range(0, nb):
            dd = datavalue[j, :, :]
            dataset.GetRasterBand(j + 1).WriteArray(dd, xOffset_list[i], yOffset_list[i])
        i += 1
    
    geoTransform = in_ds.GetGeoTransform()
    dataset.SetGeoTransform(geoTransform)
    proj = in_ds.GetProjection()
    dataset.SetProjection(proj)


def executeST(LandsatT0,MODISt0,MODISt1,S2_t0,S3_t0,S3_t1,shape,profile,product,temp_file):
    # Perform the prediction with STARFM
    for i in range(0, LandsatT0.size-(sizeSlices)*shape[1]+1, (sizeSlices)*shape[1]):
       
        fine_image_t0 = S2_t0[i:i+sizeSlices*shape[1],]
        coarse_image_t0 = S3_t0[i:i+sizeSlices*shape[1],]
        coarse_image_t1 = S3_t1[i:i+sizeSlices*shape[1],]
        prediction = algstarfm(fine_image_t0, coarse_image_t0, coarse_image_t1, profile, shape)
       
        if i == 0:
            predictions = prediction
           
        else:
            predictions = np.append(predictions, prediction, axis=0)
      
    
    # -tif final result
    profile = product.profile
    profile.update(dtype='float64', count=7) # number of bands

    file_name =  pathst +  '//predictionST.tif'
    
    result = rasterio.open(file_name, 'w', **profile)
    result.write(predictions, 1)
    result.close()
    

    plt.imshow(predictions)
    plt.gray()
    plt.show()
    return result
    
    
    
# Flatten blocks inside a dask array            
def block2row(array, row, folder, block_id=None):
    if array.shape[0] == windowSize:
        # Parameters	
        name_string = str(block_id[0] + 1)
        m,n = array.shape
        u = m + 1 - windowSize
        v = n + 1 - windowSize

    	# Get Starting block indicesque ha pasado al perro de susana bicho
        start_idx = np.arange(u)[:,None]*n + np.arange(v)

    	# Get offsetted indices across the height and width of input array
        offset_idx = np.arange(windowSize)[:,None]*n + np.arange(windowSize)

    	# Get all actual indices & index into input array for final output
        flat_array = np.take(array,start_idx.ravel()[:,None] + offset_idx.ravel())

        # Save to (dask) array in .zarr format
        file_name = pathst + folder + name_string + 'r' + row + '.zarr'
        zarr.save(file_name, flat_array)
    
    return array

# Divide an image in overlapping blocks   
def partition(image, folder):
    image_da = da.from_array(image, chunks = (windowSize,image.shape[1]))
    image_pad = da.pad(image_da, windowSize//2, mode='constant')
    
    for i in range(0,windowSize):
        row = str(i)
        block_i = image_pad[i:,:]
        block_i_da = da.rechunk(block_i, chunks=(windowSize,image_pad.shape[1]))
        block_i_da.map_blocks(block2row, dtype=int, row=row, folder=folder).compute()


# Create a list of all files in the folder and stack them into one dask array
def da_stack(folder, shape):
    da_list = [] 
    full_path = pathst + folder
    max_blocks = shape[0]//windowSize + 1 
    
    for block in range(1,max_blocks + 1):
        for row in range(0,windowSize):
            name = str(block) + 'r' + str(row)
            full_name = full_path + name + '.zarr'
            try:
                da_array = da.from_zarr(full_name)
                da_list.append(da_array) 
            except Exception:
                continue
      
    return da.rechunk(da.concatenate(da_list, axis=0), chunks = (shape[1],windowSize**2))


# Calculate the spectral distance
def spectral_distance(fine_image_t0, coarse_image_t0):
    spec_diff = fine_image_t0 - coarse_image_t0
    spec_dist = 1/(abs(spec_diff) + 1.0)
    #print ("Done spectral distance!", spec_dist)
    
    return spec_diff, spec_dist


# Calculate the temporal distance    
def temporal_distance(coarse_image_t0, coarse_image_t1):
    temp_diff = coarse_image_t1 - coarse_image_t0
    temp_dist = 1/(abs(temp_diff) + 1.0)
    #print ("Done temporal distance!", temp_dist)
    
    return temp_diff, temp_dist
   

# Calculate the spatial distance    
def spatial_distance(array):
    coord = np.sqrt((np.mgrid[0:windowSize,0:windowSize]-windowSize//2)**2)
    spat_dist = np.sqrt(((0-coord[0])**2+(0-coord[1])**2))
    rel_spat_dist = spat_dist/spatImp + 1.0 # relative spatial distance
    rev_spat_dist = 1/rel_spat_dist # relative spatial distance reversed
    flat_spat_dist = np.ravel(rev_spat_dist)
    spat_dist_da = da.from_array(flat_spat_dist, chunks=flat_spat_dist.shape)
    #print ("Done spatial distance!", spat_dist_da)
    
    return spat_dist_da


# Define the threshold used in the dynamic classification process
def similarity_threshold(fine_image_t0):#, st_dev):
    fine_image_t0 = da.where(fine_image_t0==0, np.nan, fine_image_t0)
    st_dev = da.nanstd(fine_image_t0, axis=1)# new
    sim_threshold = st_dev*2/numberClass 
    #print ("Done similarity threshold!", sim_threshold)

    return sim_threshold


# Define the spectrally similar pixels within a moving window    
def similarity_pixels(fine_image_t0):
    sim_threshold = similarity_threshold(fine_image_t0)
    # possible to implement as sparse matrix
    similar_pixels = da.where(abs(fine_image_t0 - 
                                  fine_image_t0[:,mid_idx][:,None])
        <= sim_threshold[:,None], 1, 0) #sim_threshold[:,mid_idx][:,None], 1, 0) # new
    #print ("Done similarity pixels!", similar_pixels)
   
    return similar_pixels
        

# Apply filtering on similar pixels 
def filtering(fine_image_t0, spec_dist, temp_dist, spec_diff, temp_diff):
    similar_pixels = similarity_pixels(fine_image_t0) 
    max_spec_dist = abs(spec_diff)[:,mid_idx][:,None] + specUncertainty + 1
    max_temp_dist = abs(temp_diff)[:,mid_idx][:,None] + tempUncertainty + 1  
    spec_filter = da.where(spec_dist>1.0/max_spec_dist, 1, 0)
    st_filter = spec_filter
    
    if tempst == True:
        temp_filter = da.where(temp_dist>1.0/max_temp_dist, 1, 0)
        st_filter = spec_filter*temp_filter  
        
    similar_pixels_filtered = similar_pixels*st_filter
    #print ("Done filtering!", similar_pixels_filtered)

    return similar_pixels_filtered # sim_pixels_sparse
    

# Calculate the combined distance
def comb_distance(spec_dist, temp_dist, spat_dist):
    if logWeight == True:
        spec_dist = da.log(spec_dist + 1)
        temp_dist = da.log(temp_dist + 1)
    
    comb_dist = da.rechunk(spec_dist*temp_dist*spat_dist, 
                           chunks=spec_dist.chunksize)
    #print ("Done comb distance!", comb_dist)
    
    return comb_dist
    
        
# Calculate weights
def weighting(spec_dist, temp_dist, comb_dist, similar_pixels_filtered):
    # Assign max weight (1) when the temporal or spectral distance is zero
    zero_spec_dist = da.where(spec_dist[:,mid_idx][:,None] == 1, 1, 0)
    zero_temp_dist = da.where(temp_dist[:,mid_idx][:,None] == 1, 1, 0)
    zero_dist_mid = da.where((zero_spec_dist == 1), 
                             zero_spec_dist, zero_temp_dist)
    shape = da.subtract(spec_dist.shape,(0,1))
    zero_dist = da.zeros(shape, chunks=(spec_dist.shape[0],shape[1]))
    zero_dist = da.insert(zero_dist, [mid_idx], zero_dist_mid, axis=1)
    weights = da.where((da.sum(zero_dist,1)[:,None] == 1), zero_dist, comb_dist)
    
    # Calculate weights only for the filtered spectrally similar pixels
    weights_filt = weights*similar_pixels_filtered
    
    # Normalize weights
    norm_weights = da.rechunk(weights_filt/(da.sum(weights_filt,1)[:,None]), 
                              chunks = spec_dist.chunksize)
    
    #print ("Done weighting!", norm_weights)
    
    return norm_weights


# Derive fine resolution reflectance for the day of prediction 
def predict(fine_image_t0, coarse_image_t0, coarse_image_t1, shape):
    spec = spectral_distance(fine_image_t0, coarse_image_t0)
    spec_diff = spec[0]
    spec_dist = spec[1]
    tempst = temporal_distance(coarse_image_t0, coarse_image_t1)
    temp_diff = tempst[0] 
    temp_dist = tempst[1]
    spat_dist = spatial_distance(fine_image_t0)
    comb_dist = comb_distance(spec_dist, temp_dist, spat_dist)
    similar_pixels = filtering(fine_image_t0, spec_dist, temp_dist, spec_diff, 
                               temp_diff)
    weights = weighting(spec_dist, temp_dist, comb_dist, similar_pixels)    
    pred_refl = fine_image_t0 + temp_diff
    weighted_pred_refl = da.sum(pred_refl*weights, axis=1)   
    prediction = da.reshape(weighted_pred_refl, shape)
    #print ("Done prediction!")
    
    return prediction
    
 
# Compute the results (converts the dask array to a numpy array)   
def algstarfm(fine_image_t0, coarse_image_t0, coarse_image_t1, profile, shape):
    #print ('Processing...')
    prediction_da = predict(fine_image_t0, coarse_image_t0, coarse_image_t1, shape)
    #with ProgressBar():
    prediction = prediction_da.compute()
    
    return prediction



def estarfm():
    return processingImages('EST')
def starfm():
    return processingImages('ST')
