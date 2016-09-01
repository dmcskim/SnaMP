import sys
import argparse
import re
from itertools import islice

parser = argparse.ArgumentParser(description='Parse HOMD database to greengene format')
parser.add_argument('-a', '--aligned_fp', help='aligned fasta file', required=True)
parser.add_argument('-u', '--unaligned_fp', help='unaligned fasta file', required=True)
parser.add_argument('-t', '--taxa_fp', help='taxaonomy file', required=True)
parser.add_argument('-d', '--target_dir', default='.')
args = parser.parse_args()

header2align = {}
with open(args.aligned_fp) as f:
    while True:
        next_n = list(islice(f, 2))
        if not next_n:
            break
        m = re.match(r'^.* File_(.*?) .*$', next_n[0].strip())
        if m:
            header = m.group(1)
        else:
            raise RuntimeError('This should never happen')
        read = next_n[1].strip()
        header2align[header] = read
        
header2taxa = {}
with open(args.taxa_fp) as f:
    for line in f:
        content = line.strip().split('\t')
        header = content[0].strip()
        taxa = content[1].strip().replace(';', '; ')
        header2taxa[header] = taxa

with open(args.unaligned_fp) as f, \
        open(args.target_dir + '/homd_aligned.fa', 'w') as al, \
        open(args.target_dir + '/homd.fa', 'w') as fa, \
        open(args.target_dir + '/homd.tax', 'w') as tax:
    cnt = 1
    for i, line in enumerate(f):
        if i % 2 == 0:
            content = line.strip().split('|')
            header = content[0].strip()[1:]
            
            al.write('>%d\n' % cnt)
            al.write('%s\n' % header2align[header])
            fa.write('>%d\n' % cnt)
            tax.write('%d\t%s\n' % (cnt, header2taxa[header]))
            cnt += 1
        else:
            fa.write(line)