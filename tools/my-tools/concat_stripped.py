import os
import argparse
import re
from itertools import islice

parser = argparse.ArgumentParser(description='Merge all fasta files in strip dir into one single fasta file as the input for UPARSE')
parser.add_argument('-i', '--input_dir', help='Input dir', required=True)
parser.add_argument('-o', '--output_fp', help='Ouput file path', default='reads.fa')
args = parser.parse_args()

def atoi(in_str):
    if re.match(r'^\d+$', in_str):
        return int(in_str)
    else:
        return -1

cnt = 1
with open(args.output_fp, 'w') as fo:
    for fp in sorted(os.listdir(args.input_dir), key=lambda x: atoi(x.split('.')[0])):
        m = re.match(r'^(.+)[.]fa$', fp)
        if m:
            print(m.group(1))
            with open(args.input_dir + '/' + fp) as f:
                while True:
                    next_n = list(islice(f, 2))
                    if not next_n:
                        break
                    fo.write('>%d;barcodelabel=%s;\n%s\n' % (cnt, m.group(1), next_n[1].strip()))
                    cnt += 1
            
