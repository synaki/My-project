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
    for sequence in SeqIO.parse(input_genome, "gb"):
        print("The length of the given input genome sequence is ")
        print(len(sequence))

    TnsA = input("please insert the TnsA gene :")
    for tnsA in SeqIO.parse(TnsA, "fasta"):
        
    TnsB = input("please inser the TnsB gene :")
    TnsC = input("please insert the TnsC gene :")
    TnsD = input("please insert the TnsD gene :")


user_input()
