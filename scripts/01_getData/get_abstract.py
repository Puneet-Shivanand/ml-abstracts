from Bio import Entrez
import time
Entrez.email = "vinay.rs@leucinerichbio.com"
handle = Entrez.esearch(db="pubmed",term="Amyotrophic Lateral Sclerosis",retmax="21000")

record = Entrez.read(handle)
with open("~/Documents/ML_Pubmed/id_list.txt","w") as file_write:
	for item in record['IdList']:
		file_write.write(item)
		file_write.write('\n')
