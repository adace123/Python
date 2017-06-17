def genomeSearch(gene):
    if gene.find("ATG")<0:
        print("No gene is found.")
    else:
        for i in range(len(gene)):
            if gene[i:i + 3] == "ATG":
                if gene[i + 3:].find("TAA") >= 0:
                    if len(gene[i + 3:gene.find("TAA")]) % 3 == 0:
                        print(gene[i + 3:gene.find("TAA")])
                elif gene[i+3:].find("TGA") >= 0:
                    if len(gene[i + 3:gene.find("TGA")]) % 3 == 0:
                        print(gene[i + 3:gene.find("TGA")])
                elif gene[i+3:].find("TAG") >= 0:
                    if len(gene[i + 3:gene.find("TAG")]) % 3 == 0:
                        print(gene[i + 3:gene.find("TAG")])


genome = input("Enter genome: ")

genomeSearch(genome)
