import pandas as pd
from collections import OrderedDict
import re
import sys

def parse_taxonomy(tax_file):
    id_2_label = {}
    with open(tax_file) as f:
        for line in f:
            content = line.strip().split('\t')
            taxa_id = content[0]
            taxa_label = content[1]
            id_2_label[taxa_id] = taxa_label
    return id_2_label

def parse_blast_res(id_2_label, res_file):
    marker = 0
    otu_id_2_taxa_label = {}
    with open(res_file) as f:
        for line in f:
            if line.startswith('# BLAST'):
                marker = 0
            else:
                marker += 1
            
            if marker == 5:
                content = line.strip().split('\t')
                otu_id = content[0] + ";"
                taxa_id = content[1]
                otu_id_2_taxa_label[otu_id] = id_2_label[taxa_id] 
    return otu_id_2_taxa_label

if __name__ == '__main__':
    id_2_label = parse_taxonomy(sys.argv[1])
    otu_id_2_taxa_label = parse_blast_res(id_2_label, sys.argv[2])
    df = pd.read_csv(sys.argv[3], sep='\t') 
    df.insert(loc=len(df.columns), column="taxonomy", value=[otu_id_2_taxa_label[x] if x in otu_id_2_taxa_label else "unknown" for x in df["OTUId"]])
    df["OTUId"] = ["OTU_" + str(x) for x in range(len(df.index))]
    df = df.rename(columns = {'OTUId': "#OTU ID"})
    df.to_csv(sys.argv[4], sep = '\t', index=False)
