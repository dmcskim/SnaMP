import re
import sys
import os
import argparse

parser = argparse.ArgumentParser(description='Parse genebank download file into greengene format')
parser.add_argument('-i', '--input_dir', help='input dir', required=True)
parser.add_argument('-o', '--output_dir', help='output dir', default='./')
args = parser.parse_args()

def parse_file(in_fp, tax, fa):
    global cnt
    m = re.match(r'.*/(.*) (.*)\.fasta', in_fp)
    taxa = 'k__xxx; p__xxx; c__xxx; o__xxx; f__xxx; g__{}; s__{}'.format(m.group(1), m.group(2))
    read = ''
    with open(in_fp) as fi:
        for line in fi:
            if line.startswith('>'):
                if len(read) != 0:
                    fa.write('%s\n' % read)
                fa.write('>%d\n' % cnt)
                tax.write('%d\t%s\n' % (cnt, taxa))
                read = ''
                cnt += 1
            else:
                read += line.strip()
        fa.write('%s\n' % read)

cnt = 1
with open(args.output_dir + '/mock.fa', 'w') as fa, open(args.output_dir + '/mock.tax', 'w') as tax:
    for in_fp in os.listdir(args.input_dir):
        if in_fp.startswith('.'):
            continue
        parse_file(args.input_dir + '/' + in_fp, tax, fa)

