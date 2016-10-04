# Mock DNA

1.  Manually extract target taxa from source BEI document.
2.  Search Genbank(http://www.ncbi.nlm.nih.gov/nuccore) for each target item with suffix __16s__
	* Set __Molecule types__ to __rRNA__
	* Set __Species__ to __Bacteria__
	* Set __Sequence length__: 1000 ~ 2000
	* Click __Top Organism__ to filter if possible
	* Click __send to__
		* __Choose Destination__: file
		* __Format__: FASTA
		* __Sort by__: default order
		* click __create file__
		* save under __download__
3.  Convert to GG format `python parse.py -i download`




> Written with [StackEdit](https://stackedit.io/).