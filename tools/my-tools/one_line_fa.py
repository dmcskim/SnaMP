import re
import argparse

parser = argparse.ArgumentParser(description='Conver multiple line fasta file into one line fasta file')
parser.add_argument('-i', '--input_fp', help='input file path', required=True)
parser.add_argument('-o', '--output_fp', help='output file path', required=True)
args = parser.parse_args()


read = ''
with open(args.input_fp) as fi, open(args.output_fp, 'w') as fo:
    for line in fi:
        if line.startswith('>'):
            if read != '':
                fo.write('%s\n' % read)
            fo.write('%s\n' % line.strip())
            read = ''
        else:
            read += line.strip()
    fo.write('%s\n' % read)
