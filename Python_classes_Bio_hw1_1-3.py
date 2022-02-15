#!/usr/bin/env python
# coding: utf-8

# In[97]:


# Task 1. Here is the class defining bacteriophage using its sequence (a little toy genome)


# In[192]:


class PhageError(Exception):
    """Are you sure it is a living creature?"""
    pass

class Phage:
    """The phage can define its type, invades bacteria if no spacers matches and go lytic"""
    def __init__(self,genome):
        self.genome = genome.lower()
        print('Hi, I am a cute little phage')
        self.spacers_db = ['att', 'ccca','gtta']
    
    
    def phage_type(self):
        if self.genome.find('t') > -1:
            print('This is DNA phage')
        elif self.genome.find('u') > -1:
            print('This is RNA phage')
        elif self.genome.find('a') < 0 and self.genome.find('c') < 0 and self.genome.find('g') < 0:
            raise PhageError
            
    
    def invade_bacteria(self):
        invasion = 1
        for spacer in self.spacers_db:
            if self.genome.find(spacer) > -1:
                print ('Sorry, your phage was eliminated with CRISPR-Cas system')
                self.spacers_db.append(self.genome[0:3])
                invasion = 0
                break
        if invasion == 1:
            print ('Succefully invaded bacteria')
    
    def go_lytic(self):
        print('Bacteria was lysed')
        self.spacers_db = []
        print('The CRISPR-Cas spacers were destroyed')
        
        


# In[193]:


la = Phage('GUUG')


# In[194]:


Phage.phage_type(la)


# In[195]:


Phage.invade_bacteria(la)


# In[196]:


Phage.go_lytic(la)


# In[125]:


# Task 2. Here is the class describing RNA.


# In[213]:


class RNA:
    def __init__(self,seq_rna,check_start = False):
        self.rna = seq_rna.lower()
        self.check = check_start
        
        
    def translate(self):
        import Bio
        from Bio.Seq import Seq
        if self.check is False:
            prot = str(Seq(self.rna).translate())
        else:
            index_of_start = self.rna.find('aug')
            if index_of_start < 0:
                prot = 'No ORF available'
            else:
                prot = str(Seq(self.rna[index_of_start:]).translate())
        return prot
    
    
    def reverse_transcribe(self):
        import Bio
        from Bio.Seq import Seq
        return str(Seq(self.rna).back_transcribe())
        


# In[214]:


a = RNA('AUGUUCGGG')
RNA.translate(a)


# In[215]:


RNA.reverse_transcribe(a)


# In[216]:


a = RNA('AUGUUCGGG', True)
RNA.translate(a)


# In[217]:


a = RNA('AGGAUGCGG', True)
RNA.translate(a)


# In[218]:


a = RNA('AGGAGGCGG', True)
RNA.translate(a)


# In[ ]:


# Task 3. The class defining set without negative values.


# In[175]:


class NonNegativeSetError(Exception):
    """Negative value added"""
    pass

class NonNegativeSet(set):
    def __init__(self, x):
        super(NonNegativeSet,self).__init__({i for i in set(x) if i >= 0})
        
        
    def add(self, n):
        if n >= 0:
            super().add(n)
        else:
            raise NonNegativeSetError


# In[176]:


st = NonNegativeSet({1,2,3,-5,-4})
print(st)
st.add(-6)
print(st)


# In[177]:


st.add(8)
print(st)


# In[178]:





# In[ ]:





# In[ ]:




