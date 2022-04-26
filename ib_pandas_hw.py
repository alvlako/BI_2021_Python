#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[ ]:


import matplotlib.pyplot as plt


# In[2]:


print('Task 1. Nucleotide distribution')

print('type train.csv absolute path')
inp = input()
nucl = pd.read_csv(inp)


# In[3]:


print(nucl.head())


# In[4]:


count_nuc = pd.DataFrame()
count_nuc['A'] = nucl['A']


# In[5]:


count_nuc['C'] = nucl['C']
count_nuc['G'] = nucl['G']
count_nuc['T'] = nucl['T']
count_nuc['position'] = nucl['pos']
count_nuc = count_nuc.set_index('position')


# In[6]:


count_nuc.plot.bar(rot=0)

# In[19]:


print('Task 2. Extract specific columns')
part_nuc = pd.DataFrame()
part_nuc = nucl.loc[nucl['matches'] > np.mean(nucl['matches'])]
part_nuc = part_nuc.drop(['A', 'T', 'G', 'C'], axis=1)
part_nuc = part_nuc.drop(['A_fraction', 'T_fraction', 'G_fraction', 'C_fraction'],axis=1)
print(part_nuc.head())


# In[20]:


print(' Task 3, EDA')
print(nucl.info())


# In[21]:


print(nucl.describe())


# In[22]:


fig, axs = plt.subplots(ncols=3, nrows=5, figsize=(20, 10))
index = 0
axs = axs.flatten()
for i, j in nucl.items():
    sns.boxplot(y=i, data=nucl, ax=axs[index])
    index += 1
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
plt.show()


# In[23]:


print(nucl.isnull().sum().sort_values(ascending=False))


# In[25]:


print(nucl.isna().sum().sort_values(ascending=False))


# In[26]:


print(nucl.corr())


# In[27]:


h_labels = [x.replace('_', ' ').title() for x in list(nucl)]
fig, ax = plt.subplots(figsize=(10, 6))
_ = sns.heatmap(nucl.corr(), annot=True, xticklabels=h_labels, yticklabels=h_labels, cmap=sns.cubehelix_palette(as_cmap=True), ax=ax)


# In[37]:


print('Additional task')
# Make functions


def read_gff(path):
    gff = pd.read_csv(path, sep='\t', comment='#', skiprows=1)
    gff.columns = ['chromosome', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes']
    return(gff)


# In[106]:

print('type gff absolute path')
path = input()
gff = read_gff(path)
print(gff.head())


# In[43]:


def read_bed6(path):
    bed = pd.read_csv(path, sep='\t', comment='#', skiprows=1)
    bed.columns = ['chromosome', 'start', 'end', 'name', 'score', 'strand']
    return bed

# In[107]:

print('type bed absolute path')
path1 = input()
bed = read_bed6(path1)
print(bed.head())

# In[58]:


print('Extract simple names of rRNA')
rna_info = read_gff(path)
rna_info_convenient = rna_info
rna_info_convenient['attributes']=rna_info['attributes'].str.extract('(Name.*rRNA)')
rna_info_convenient['attributes'] = rna_info_convenient['attributes'].str.replace('Name=', '')
rna_info_convenient['attributes'] = rna_info_convenient['attributes'].str.replace('_rRNA', '')
print(rna_info_convenient.head())


# In[102]:


print('Count distinct rRNA types per chromosome')
rna_dist = rna_info_convenient.filter(items=['chromosome', 'attributes'])
rna_dist['count'] = 1
rna_dist.head()
print(rna_dist.groupby(['chromosome', 'attributes']).sum())


# In[117]:


print('Intersect')
merged = gff.append(bed)
merged = merged.sort_values(by='start')
merged.head()
annot_ind_list = merged.index[merged['type'] != 'NaN'].tolist()
annot_read_start = [x+1 for x in annot_ind_list]
annot_read_end = [x-1 for x in annot_ind_list]
save = annot_read_start + annot_read_end + annot_ind_list
merged1 = merged.iloc[save]
print(merged1.sort_values(by='start').head())
