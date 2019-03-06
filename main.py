#Editor for inserting genes using transposon
#Finds the positions of the inserted transposon and the gene

# Imports
from Bio import SeqIO
from Bio.Seq import Seq
import sys

#function to get input from the user
def usage(Sensor):
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
    product = gene
    final = product + Sensor
    print(final)
    return final


def user_input():
    print("Input limited to fasta or genbank file")
    # Gives access to the user to import their genome of interest
    #regulating the input file formats
    try:
        input_genome = input("please insert the genome to be edited: ")

    except FileNotFoundError:

        print("%s cannot be opened for reading" % (input_genome))

    else:

        for sequence in SeqIO.parse(input_genome, "fasta"):

            print("The length of the given input genome sequence is ")
            print(len(sequence))

    #Imports sequence using biopython limited to fasta format
    for sequence in SeqIO.parse(input_genome, "gb"):

        print("The length of the given input genome sequence is ")

        print(len(sequence))
    #Imports sequence using biopython limited to genbank sequence


    insert_Gene = input("Please insert the desired gene of interest :")
    #gets the desired gene from the user
    for fragment in SeqIO.parse(insert_Gene, "fasta"):
        print("The length of the desired gene of interest")
        print(len(fragment.seq))
        Sensor = fragment.seq


    return Sensor, input_genome

def location_predictor():
    try:
        location = float(input("Please provide the insert position using tn7: "))

    except:
        print("input is restricted to float")

    genome_map = int(46416.52 * location)
    print("The Insertion position is :", genome_map)
    return genome_map

#function helps to insert the transposon carring segment at desired location


Sensor, input_genome, = user_input()
usage(Sensor)
location_predictor()

