import pandas as pd
from collections import OrderedDict
import re
import sys

def get_location_dict(tax_file):
    taxa_set = set()
    id_2_label = {}
    with open(tax_file) as f:
        for line in f:
            content = line.strip().split('\t')
            taxa_id = content[0]
            taxa_label = content[1]
            taxa_set.add(taxa_label)
            id_2_label[taxa_id] = taxa_label
    ordered_set = sorted(list(taxa_set))
    location_dict = OrderedDict(zip(ordered_set, range(len(ordered_set))))
    return location_dict, id_2_label

def build_column(location_dict, id_2_label, res_file):
    marker = 0
    m = re.match(r'^.+/(.+).txt', res_file)
    coloumn_name = m.group(1)
    count_list = [0] * len(location_dict)
    with open(res_file) as f:
        for line in f:
            if line.startswith('# BLAST'):
                marker = 0
            else:
                marker += 1
            
            if marker == 5:
                content = line.strip().split('\t')
                count = int(content[0].split('-')[1])
                taxa_id = content[1]
                identity = float(content[7])
                coverage = float(content[8])
                
                location = location_dict[id_2_label[taxa_id]]
                count_list[location] += count
    return coloumn_name, count_list

if __name__ == '__main__':
    location_dict, id_2_label = get_location_dict(sys.argv[-2])
    c_list = [build_column(location_dict, id_2_label, x) for x in sys.argv[1:-2]]
    name_list = [x[0] for x in c_list]
    df = pd.DataFrame({x[0]:x[1] for x in c_list}, index=location_dict.keys())
    df.reindex_axis(name_list, axis=1)
    df = df[(df != 0).any(axis=1)]
    df.insert(loc=len(df.columns), column="taxonomy", value=df.index)
    #df.insert(loc=0, column="#OTU ID", value=["OTU_" + str(x) for x in range(len(df.index))])
    df.insert(loc=0, column="#OTU ID", value=["OTU_" + str(x) for x in df.index])
    df.to_csv(sys.argv[-1], sep = '\t', index=False)
