import allel
import sys
import zarr
#data = allel.read_vcf('gene1.vcf.gz')
zarr_path = "gene1.zarr"
#allel.vcf_to_zarr("gene1.vcf.gz",zarr_path,fields="*",log=sys.stdout,overwrite=True)
data1 = zarr.open(zarr_path)
data1.tree(expand=True)
"""
print(sorted(data.keys()))
inp=""
while inp!="quit":
	inp = input()
	try:
		eval(inp)
	except:
		pass
"""	
