import os
import sys
import subprocess

f1 = sys.argv[1]

protein_list = []
with open(f1,'r') as handle:
    for line in handle:
        line = line.replace('\n','')
        protein_list.append(line)
print(protein_list)

#os.mkdir(os.getcwd() +'/prt_db')

os.chdir(os.getcwd() + '/prt_db')
'''
print(os.getcwd())
for i in protein_list:
    os.system('wget http://www.uniprot.org/uniprot/{}.txt'.format(i))
'''

output = str(subprocess.check_output(['ls']))
print(output)

flie_list = output.split('\n')
flie_list = file_list[:len(flie_list)-1]

prt_db = dict()
for i in range(len(flie_list)):
    with open(file_list[i],'r') as handle:
        for line in handle:
            if line.find('GO') >= 0:
                prt_db[protein_list[i]] += line
print(prt_db)
              


