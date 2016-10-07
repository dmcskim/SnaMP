# MIX

```
python mix.py --hg_fa_fp ../../HOMD/14.5/homd.fa --hg_tax_fp ../../HOMD/14.5/homd.tax --mock_fa_fp ../../BEI_MOCK/HM-783D/mock.fa --mock_tax_fp ../../BEI_MOCK/HM-783D/mock.tax
```

1.  Match taxonomy by fuzzy seach.
	* https://github.com/seatgeek/fuzzywuzzy
2.  Color print
	* https://pypi.python.org/pypi/termcolor
3.  Since we only have taxonomy label at genus and species level for mock database, we will convert HOMD/GG taxonomy to match mock taxonomy if matched or selected to be matched.


> Written with [StackEdit](https://stackedit.io/).