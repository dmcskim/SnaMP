import sys
import pandas as pd
import numpy as np

def absolute_2_relative(in_fp, out_fp):
    df = pd.read_csv(in_fp, index_col=0, sep='\t')
    for col in df.columns:
        df[col] = df[col]/np.sum(df[col]) * 100
    df.to_csv(out_fp, sep='\t')

if __name__ == "__main__":
    absolute_2_relative(sys.argv[1], sys.argv[2])
