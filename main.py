#Editor for inserting genes using transposon
#Finds the positions of the inserted transposon and the gene

# Imports
from Bio import SeqIO
from Bio.Seq import Seq

#function to get input from the user
def user_input():
    print("Input limited to fasta or genbank file")
    #to give the user a outlook of input file format
    input_genome = input("please insert the genome to be edited :")
    # Gives access to the user to import their genome of interest
    for sequence in SeqIO.parse(input_genome, "fasta"):
        print("The length of the given input genome sequence is ")
        print(len(sequence))
    #Imports sequence using biopython limited to fasta format
    for sequence in SeqIO.parse(input_genome, "gb"):
        print("The length of the given input genome sequence is ")
        print(len(sequence))
    #Imports sequence using biopython limited to genbank sequence
    choose = input("choose one of the transposon : 1. Tn5 2. Tn7 ")
    #gets input from user about the transposon selection
    if choose == "1" or "tn5":
        flag = True
    #if it is true goes to tn5 function to produce a random insertion in the genome
    elif choose == "2" or "Tn7":
        flag = False

def desired_gene():
    #if it is false goes to tn7 function to produce a single site specific modification
    insert_Gene = input("Please insert the desired gene of interest :")
    #gets the desired gene from the user
    for fragment in SeqIO.parse(insert_Gene, "fasta"):
        print("The length of the desired gene of interest")
        print(len(fragment.seq))
        ak = fragment.seq
        print(ak)

#function that interpret transposon tn7
#It insert at specific sections

    #imports the essential transposon gene from the local directory
    for TnsA in SeqIO.parse("tnsA.txt", "fasta"):
        tnsA = TnsA.seq
    # transposes A which forms a complex with the transposes B and C to form a nick in the DNA
    for TnsB in SeqIO.parse("tnsB.txt", "fasta"):
        tnsB = TnsB.seq
    for TnsC in SeqIO.parse("tnsC.txt", "fasta"):
        tnsC = TnsC.seq
    for TnsD in SeqIO.parse("tnsD.txt", "fasta"):
        tnsD = TnsD.seq
    # transposes D which further helps in the choosing the desired position
    gene = tnsA + tnsB + tnsC + tnsD
    print(len(gene))
    final = concatinate(gene, ak)
    print(final)

# to concatinate the given desired gene with the tranposes to form final insert
def concatinate(gene, fragment):
    return gene + fragment

#function that imports the tn5 transpose
def tn5():
    for tns5 in SeqIO.parse("tn5.txt", "fasta"):
        tns5 = tns5.seq
        print(tns5)

user_input()
desired_gene()
tn5()






