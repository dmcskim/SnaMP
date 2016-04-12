import os
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='Generate simple meta-data file from input file names.')
parser.add_argument('-r', '--region', help='select HV region', choices=['V13', 'V34'], required=True)
parser.add_argument('-o', '--output_fp', help='output file path', default='meta_data.txt')
args = parser.parse_args()

if args.region == 'V13':
    f_primer = 'AGAGTTTGATCMTGGCTCAG'
    r_primer = 'ATTACCGCGGCTGCTGG'
elif args.region == 'V34':
    f_primer = 'CCTACGGGNGGCWGCAG'
    r_primer = 'GACTACHVGGGTATCTAATCC'

files = os.listdir('link')
sample_id_dict = {}
for f in files:
    if f.startswith('.'):
        continue
    # sample_id construction
    sample_id = f.split('_')[0]
    if sample_id in sample_id_dict:
        sample_id_dict[sample_id].append(f)
    else:
        sample_id_dict[sample_id] = [f]

for key in sample_id_dict:
    sample_id_dict[sample_id] = sorted(sample_id_dict[sample_id])

records = []
for key in sorted(sample_id_dict.keys()):
    records.append((key, f_primer, r_primer, sample_id_dict[key][0], sample_id_dict[key][1], 'NA'))

df = pd.DataFrame(records, columns=['#SampleID', 'ForwardPrimer', 'ReversePrimer', 'ForwardFastqGZ', 'ReverseFastqGZ', 'Description'])
df.to_csv(args.output_fp, sep='\t', index=False)

