import numpy as np
import pandas as pd
import sys
from collections import OrderedDict

def count_fq(fp):
    cnt = 0
    with open(fp) as f:
        for line in f:
            cnt += 1
    if cnt % 4 != 0:
        print("error line number")
        sys.exit(1)
    return cnt/4

def build_count_table(origin_files, joined_files, filtered_files, otu_table_file):
    origin_counts = [count_fq(x) for x in origin_files]
    joined_counts = [count_fq(x) for x in joined_files]
    joined_rate = np.array(joined_counts).astype(float)/np.array(origin_counts) * 100
    filtered_counts = [count_fq(x) for x in filtered_files]
    filtered_rate = np.array(filtered_counts).astype(float)/np.array(joined_counts) * 100
    blast_counts = pd.read_csv(otu_table_file, index_col=0, sep='\t').sum(axis=0)
    blast_rate = np.array(blast_counts).astype(float)/np.array(filtered_counts) * 100
    df_index = blast_counts.index
    
    ordered_dict = OrderedDict([("Origin_count", origin_counts), \
                                ("Joined_count", joined_counts), \
                                ("Good_quality_count", filtered_counts), \
                                ("Blast_hit_count", list(blast_counts)), \
                                ("Merge_rate(%)", joined_rate), \
                                ("Good_quality_rate(%)", filtered_rate), \
                                ("Blast_hit_rate(%)", blast_rate)])

    df = pd.DataFrame(dict(ordered_dict), index = df_index)
    df = df.reindex_axis(ordered_dict.keys(), axis=1)
    return df

if __name__ == "__main__":
    files = sys.argv[1:-2]
    file_bundles = np.split(np.array(files).astype(str), 3)
    otu_table_file = sys.argv[-2]
    output_file = sys.argv[-1]
    
    df = build_count_table(file_bundles[0], file_bundles[1], file_bundles[2], otu_table_file)
    df.to_csv(output_file, sep='\t')
