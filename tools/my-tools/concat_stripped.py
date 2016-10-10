import os
import re
import sys
from itertools import islice

cnt = 1
with open(sys.argv[-1], 'w') as fo:
    for fp in sys.argv[:-1]:
        m = re.match(r'^.+/(.+)[.]fa$', fp)
        if m:
            print(m.group(1))
            with open(fp) as f:
                while True:
                    next_n = list(islice(f, 2))
                    if not next_n:
                        break
                    fo.write('>%d;barcodelabel=%s;\n%s\n' % (cnt, m.group(1), next_n[1].strip()))
                    cnt += 1
            
