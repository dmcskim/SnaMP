# HOMD 14.5

## Download
Download page: http://www.homd.org/?name=seqDownload&type=R

* HOMD 16S rRNA RefSeq Version 14.5 (Starts from position 9): `HOMD_16S_rRNA_RefSeq_V14.5.p9.fasta`
* HOMD 16S rRNA RefSeq Version 14.5 Taxonomy File for QIIME: `HOMD_16S_rRNA_RefSeq_V14.5.qiime.taxonomy`
* HOMD 16S rRNA RefSeq Version 14.5 Aligned FASTA File: `HOMD_16S_rRNA_RefSeq_V14.5.aligned.fasta`

## Basic info

* __889__ reference sequences
* For download files, the order is not matched
* Parsed file would be order matched and use index(start from 1) as sequence header
* Taxonomy file:
	* HOMD label separator: only `;`  
	* Parsed(GG) label separator: `;` followed by a __space__
	* The parsed format is compatible with GG, but taxonomy label may not be identical.
	

## Parse
```
python parse.py -a download/HOMD_16S_rRNA_RefSeq_V14.5.aligned.fasta -u download/HOMD_16S_rRNA_RefSeq_V14.5.p9.fasta -t download/HOMD_16S_rRNA_RefSeq_V14.5.qiime.taxonomy -d .
```

> Written with [StackEdit](https://stackedit.io/).