import os
import pandas as pd

files = os.listdir('link')
sample_id_dict = {}
for f in files:
    if f.startswith('.'):
        continue
    sample_id = f.split('_')[0]
    if sample_id in sample_id_dict:
        sample_id_dict[sample_id].append(f)
    else:
        sample_id_dict[sample_id] = [f]

for key in sample_id_dict:
    sample_id_dict[sample_id] = sorted(sample_id_dict[sample_id])

records = []
for key in sorted(sample_id_dict.keys()):
    records.append((key, 'AGAGTTTGATCMTGGCTCAG', 'ATTACCGCGGCTGCTGG', sample_id_dict[key][0], sample_id_dict[key][1], 'NA'))

df = pd.DataFrame(records, columns=['#SampleID', 'ForwardPrimer', 'ReversePrimer', 'ForwardFastqGZ', 'ReverseFastqGZ', 'Description'])
df.to_csv('meta_data.txt', sep='\t', index=False)

