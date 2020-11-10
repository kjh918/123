
# library import
from imctools.scripts import ometiff2analysis
from imctools.scripts import imc2tiff
from imctools.scripts import ome2micat
from imctools.scripts import probablity2uncertainty
from imctools.scripts import convertfolder2imcfolder
from imctools.scripts import exportacquisitioncsv

import os
import logging
import re
import zipfile
import sys

f = sys.argv[1]
home = os.path.expanduser('~')

#naming
csv_pannel = home+f+'config/pannel.csv'
csv_pannel_metal = 'metal'
csv_pannel_ilastik = 'ilastik' 
csv_pannel_full = 'full'

# making tree
if not os.path.exists(home+'/'+f):
    os.makedirs(home+'/'+f)
os.chdir(home + '/' + f)

folders = [home+'/'+f+'/example']
file_regexp = '.*.zip'
folder_base = home+ '/'+f+'/output'

folder_analysis = os.path.join(folder_base, 'tiffs')
folder_ilastik = os.path.join(folder_base, 'ilastik')
folder_ome = os.path.join(folder_base, 'ometiff')
folder_cp = os.path.join(folder_base, 'cpout')
folder_histocat = os.path.join(folder_base, 'histocat')
folder_uncertainty = os.path.join(folder_base, 'uncertainty')

suffix_full = '_full'
suffix_ilastik = '_ilastik'
suffix_ilastik_scale = '_s2'
suffix_mask = '_mask.tiff'
suffix_probablities = '_Probabilities'
failed_images = list()

list_analysis_stacks =[
    (csv_pannel_ilastik, suffix_ilastik, 1),
    (csv_pannel_full, suffix_full, 0)
]

for fol in [folder_base, folder_analysis, folder_ilastik,
            folder_ome, folder_cp, folder_histocat, folder_uncertainty]:
    if not os.path.exists(fol):
        os.makedirs(fol)


for i in folders:
    os.makedirs(os.path.abspath(i), exist_ok=True)

print(' ')
print('# Put the zipped inuput files in example folder. ex. zip(.mcd + .txt) ')
print(os.system('tree -d'))
print(' ')
###################################3

# check sample list
# make ometiff data
falied_images = list()
re_fn = re.compile(file_regexp)
for fol in folders:
    print(fol)
    for fn in os.listdir(fol):
        if re_fn.match(fn):
            fn_full = os.path.join(fol, fn)
            print(fn_full)
            try:
                convertfolder2imcfolder.convert_folder2imcfolder(fn_full,out_folder=folder_ome, dozip=False)
            except:
                logging.exception('Error in {}'.format(fn_full))


# write metadata
exportacquisitioncsv.export_acquisition_csv(folder_ome, fol_out=folder_cp)

# hisocat result
if not(os.path.exists(folder_histocat)):
    os.makedirs(folder_histocat)

for fol in os.listdir(folder_ome):
    ome2micat.omefolder2micatfolder(os.path.join(folder_ome,fol), folder_histocat, dtype='uint16')

for i in folders:
    for fol in os.listdir(folder_ome):
        sub_fol = os.path.join(folder_ome, i)
        for img in os.listdir(sub_fol):
            print(img)
            if not img.endswith('.ome.tiff'):
                continue
            basename = img.rstrip('.ome.tiff')
            print(img)
            for (col, suffix, addsum) in list_analysis_stacks:
                try:
                    ometiff2analysis.ometiff_2_analysis(os.path.join(sub_fol, img),folder_analysis, basename + suffix, pannelcsv=csv_pannel,metalcolumn=csv_pannel_metal,usedcolumn=col, addsum=addsum, bigtiff=False,pixeltype='uint16')
                except:
                    logging.exception('Error in {}'.format(img))

for fol in os.listdir(folder_ome):
    ome2micat.omefolder2micatfolder(os.path.join(folder_ome,fol), folder_histocat,\
    fol_masks=folder_analysis, mask_suffix=suffix_mask, dtype='uint16')

'''
os.chdir(folder_histocat)
print('result dict')
print(os.system('tree -d'))
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'#usage: python {sys.argv[0]} [group names]')
        sys.exit()
'''






















