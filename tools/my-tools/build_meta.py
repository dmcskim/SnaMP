import os
import re
import argparse
import textwrap
import pandas as pd


class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, 
                      argparse.RawTextHelpFormatter):
   pass

parser = argparse.ArgumentParser(description='Generate simple meta-data file from input file names.',
                                 formatter_class=CustomFormatter)
parser.add_argument('-r', '--region', help='select HV region', choices=['V13', 'V34'], required=True)
parser.add_argument('-m', '--matching_regex',
                    help=textwrap.dedent('''\
                        matching regular expression for determing sample_id in meta_data file,
                        use () to indicate group.
                        e.g.
                        '^(.+)_S\d+_L001_R[12]_001.fastq.gz$'
                        '^(.+)_L001_R[12]_001.fastq.gz$'
                        '^(.+)_.+_L001_R[12]_001.fastq.gz$'
                        '''),
                    default='^(.+)_S\d+_L001_R[12]_001.fastq.gz$')
parser.add_argument('-o', '--output_fp', help='output file path', default='meta_data.txt')
args = parser.parse_args()

if args.region == 'V13':
    f_primer = 'AGAGTTTGATCMTGGCTCAG'
    r_primer = 'ATTACCGCGGCTGCTGG'
elif args.region == 'V34':
    f_primer = 'CCTACGGGNGGCWGCAG'
    r_primer = 'GACTACHVGGGTATCTAATCC'

files = os.listdir('input')
sample_id_dict = {}
for f in files:
    if f.startswith('.'):
        continue
    # sample_id construction
    m = re.match(args.matching_regex, f)
    if not m:
        raise RuntimeError('"%s" does not match "%s"' % (f, args.matching_regex))
    sample_id = m.group(1)
    if sample_id in sample_id_dict:
        sample_id_dict[sample_id].append(f)
    else:
        sample_id_dict[sample_id] = [f]

for sample_id in sample_id_dict:
    sample_id_dict[sample_id] = sorted(sample_id_dict[sample_id])

records = []
for key in sorted(sample_id_dict.keys()):
    records.append((key, f_primer, r_primer, sample_id_dict[key][0], sample_id_dict[key][1], 'NA'))

df = pd.DataFrame(records, columns=['#SampleID', 'ForwardPrimer', 'ReversePrimer', 'ForwardFastqGZ', 'ReverseFastqGZ', 'Description'])
df.to_csv(args.output_fp, sep='\t', index=False)

