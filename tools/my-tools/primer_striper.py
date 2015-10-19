import sys
from itertools import islice

def strip_primer(in_fp, out_fp, head_len, tail_len):
    #print in_fp, out_fp, head_len, tail_len
    with open(in_fp) as f, open(out_fp, 'w') as fo:
        while True:
            next_n = list(islice(f, 2))
            if not next_n:
                break
            fo.write(next_n[0])
            fo.write(next_n[1].strip()[int(head_len):-int(tail_len)] + '\n')

if __name__ == '__main__':
    strip_primer(*sys.argv[1:])
