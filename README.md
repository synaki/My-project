# my-project
Advanced programming coursework

Program to insert tn5 and tn7 transposes in a given genome

tn5 and tn7 are bacterial transposon which could able to insert the desired gene in a given genome and they do it in different method.

Tn7 transposon could able to insert the gene at specific sites while Tn5 insert at random sites.

using Biopython we developed a program which could able to insert tn7 and tn5 in genome, we can create as many variants as possible.

In future after the laboratory studies we can device a program that could give the arbituary expression rate of the inserted gene.


Example Run:

"Files that should be there before the run": Ecoli.fna or Ecoli.gff ( or any other genome file in fasta or genbank format)
					     Sensor.txt ( You insert DNA could be anything but limited to .txt)
					     tn5 transposes (directly imports itself and should be there in the directory)
					     tn7 transposes (directly imports itself and should be there in the directory)


Input limited to fasta or genbank file
please insert the genome to be edited: Ecoli.fna          ..........(input from user)
The length of the given input genome sequence is 
4641652
Please insert the desired gene of interest :Sensor.txt    ..........(input from user)
The length of the desired gene of interest
4155
The insert tn7 transposes length is : 6063
The final insert and tn7 transposes length is : 10220
The length of tn5 transposes is : 1353
The final insert and tn5 transposes length is : 5508
The insert tn7 transposes length is : 6063
The final insert and tn7 transposes length is : 10220
The length of tn5 transposes is : 1353
The final insert and tn5 transposes length is : 5508
Please provide the insert position using tn7: 85          ..........(input from user)
The Insertion position is : 3945404
The Length of the genome carrying the desired gene is :
4645807
How many variants of genome to be generated :4            ...........(input from user)
gives genome results
gives the length of final genome

Creates a new file called ak.txt which has the all variants of your desired genome
