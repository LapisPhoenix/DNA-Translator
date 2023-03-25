# see LICENSE

import random


def translateDNA(dna: list):
    if not isinstance(dna, list):
        raise ValueError("DNA must be a list!")

    for group in dna:
        if len(group) > 3:
            raise Exception("DNA must be in groups of 3 or less!")

        for letter in group:
            if letter.lower() not in ["a", "u", "t", "c", "g"]:
                raise Exception(
                    f"Invalid DNA! DNA should be one of these letters: A, U, T, G, C but got '{letter}'!"
                )

    # Make sure all DNA is lowercase for translation
    dna = [x.lower() for x in dna]

    rnaTranslationTable = str.maketrans(
        {"a": "u", "u": "a", "t": "a", "g": "c", "c": "g"}
    )

    rna = [
        str(y).translate(rnaTranslationTable) for y in dna
    ]  # Creates a list of letters that has been translated already, actually translate live and is immediattly added to the list.

    rna = [x.upper() for x in rna]  # Get ready for AA translation

    aaTranslationTable = {  # Dont use str.maketrans(), it doesnt work for this: ValueError: string keys in translate table must be of length 1
        "AAA": "Phe",
        "AAC": "Leu",
        "AAG": "Phe",
        "AAU": "Leu",
        "ACA": "Cys",
        "ACC": "Trp",
        "ACG": "Cys",
        "ACU": "Thr",
        "AGA": "Ser",
        "AGC": "Ser",
        "AGG": "Ser",
        "AGU": "Ser",
        "AUA": "Tyr",
        "AUC": "Spc",
        "AUG": "Tyr",
        "AUU": "Spc",
        "CAA": "Val",
        "CAC": "Val",
        "CAG": "Val",
        "CAU": "Val",
        "CCA": "Gly",
        "CCC": "Gly",
        "CCG": "Gly",
        "CCU": "Gly",
        "CGA": "Ala",
        "CGC": "Ala",
        "CGG": "Ala",
        "CGU": "Ala",
        "CUA": "Asp",
        "CUC": "Glu",
        "CUG": "Asp",
        "CUU": "Glu",
        "GAA": "Leu",
        "GAC": "Leu",
        "GAG": "Leu",
        "GAU": "Leu",
        "GCA": "Arg",
        "GCC": "Arg",
        "GCG": "Arg",
        "GCU": "Arg",
        "GGA": "Pro",
        "GGC": "Pro",
        "GGG": "Pro",
        "GGU": "Pro",
        "GUA": "His",
        "GUC": "Glu",
        "GUG": "His",
        "GUU": "Glu",
        "UAA": "Iso",
        "UAC": "Met",
        "UAG": "Iso",
        "UAU": "Iso",
        "UCA": "Ser",
        "UCC": "Arg",
        "UCG": "Ser",
        "UCU": "Arg",
        "UGA": "Thr",
        "UGC": "Thr",
        "UGG": "Thr",
        "UGU": "Thr",
        "UUA": "Asn",
        "UUC": "Lys",
        "UUG": "Asn",
        "UUU": "Lys",
    }

    # Why did that take so long 😭

    aa = [aaTranslationTable.get(codon, "X") for codon in rna]

    # Change back to uppercase for consistency sake
    dna = [j.upper() for j in dna]

    sep = "-" * 50  # Python is stupid

    print(
        f"Translaton\n{sep}\nDNA: {', '.join(dna)}\nRNA: {', '.join(rna)}\n AA: {', '.join(aa)}\r{sep}\n\n"
    )


translateDNA(["TTA", "TCT", "TTG", "AA"])

# Output:
# Translaton
# --------------------------------------------------
# DNA: TTA, TCT, TTG, AA
# RNA: AAU, AGA, AAC, UU
# AA: Leu, Ser, Leu, X
# --------------------------------------------------


def dice(table: str, number: int):
    if not isinstance(number, int):
        exit("BAD")

    eyeTable = {
        1: ["TAC", "CTT", "CTG", "GCA", "CGA", "AGT", "CAC", "ATT"],
        2: ["TAC", "GTA", "TAA", "TGT", "CTT", "ACC", "CAC", "TAA", "ACT"],
        3: ["TAC", "AGT", "TGG", "GAA", "TAT", "GAT", "TAG", "ACT"],
        4: ["TAC", "CCT", "CGA", "CGA", "AAA", "TAG", "ACT"],
        5: ["TAC", "CGA", "GAT", "GAA", "TAC", "TAA", "ACT"],
        6: ["TAC", "CCA", "CGA", "AAG", "AAA", "ATT"]
    }

    legTable = {
        1: ['TAC', ' CTT', ' CCA', 'TGG', ' AGT', ' TAG', ' ACT'],
        2: ['TAC', ' TAA', ' AGT', 'TGG', ' CCT', ' ATT'],
        3: ['TAC', ' GTT ', ' AAG ', ' TAA', ' TGT', ' TCT', ' ATT'],
        4: ['TAC', ' TGG', ' CCA', ' GAT', ' CAG', 'TAG', ' ACT'],
        5: ['TAC', ' TGG ', ' TGG ', ' GAC', ' CCT CAA', ' ATT'],
        6: ['TAC ', 'GTT ', ' AAT ', 'AAA', ' TAA', ' CAC', ' AGT', 'TAG', 'ACT']
    }

    armTable = {
        1: ['TAC', 'TAT', ' CCA', ' AAT', ' TCT', ' AAA', 'TAT', ' CTG', ' AAT', ' GTA', 'CAA', 'ATT'],
        2: ['TAC ', 'CTA', ' ACC', ' TGG', ' CAC', ' CTT', 'CCA', 'ATT'],
        3: ['TAC', 'AGT', ' TAG', 'CCA', ' AAT', 'ATT'],
        4: ['TAC', ' TAG', ' CCA', ' TCT', ' CCC', 'GCA', 'TAG', 'ACT'],
        5: ['TAC', ' AAT ', ' CTT', ' TCT', 'TAT', ' ATT'],
        6: ['TAC', ' TAG', ' TCC', ' CTA', ' AGT', ' CTT', ' AGT', 'CCC', 'ATT']
    }

    hairCTable = {
        1: ['TAC', 'AGT', 'AAA', 'CTT', 'GAT', 'CAG', 'CAT', 'TAG', 'ACT'],
        2: ['TAC', 'GTT', 'TGG', 'TAT', 'GAT', 'ATT'],
        3: ['TAC', 'GTA', 'TGG', 'CAT', 'CTT', 'CCT', 'ATT'],
        4: ['TAC', 'AGT', 'GCA', 'CGA', 'CTA', 'GAT', 'ATT'],
        5: ['TAC', 'GTT', 'GTA', 'TAT', 'TAT', 'TAG', 'ACT'],
        6: ['TAC', 'GTT', 'TAT', 'GTT', 'TAT', 'CTA', 'CTT', 'ATT']
    }

    hairTTable = {
        1: ['TAC', 'AGT', 'GCA', 'CAT', 'CTT', 'CCT', 'CGA', 'GTA', 'TAG', 'ACT'],
        2: ['TAC', 'TGG', 'TGT', 'TAA', 'TAG', 'ACT'],
        3: ['TAC', 'CTT', 'GAT', 'TGG', 'AAT', 'GTT', 'TAG', 'ACT'],
        4: ['TAC', 'GTA', 'TGG', 'GAA', 'TAT', 'CCA', 'ATT'],
        5: ['TAC', 'TAT', 'CTT', 'CCA', 'ATT'],
        6: ['TAC', 'CTA', 'AGT', 'TAA', 'TGT', 'TAG', 'ACT']
    }

    skinTable = {
        1: ['TAC', 'GTA', 'GCA', 'CAC', 'CTT', 'CCC', 'CGA', 'ATT'],
        2: ['TAC', 'CTT', 'GAT', 'TAA', 'TGT', 'CTT', 'ACC', 'TAG', 'ACT'],
        3: ['TAC', 'CCA', 'GCA', 'CGA', 'AGT', 'ATT'],
        4: ['TAC', 'CCC', 'CGA', 'GCA', 'AAT', 'TAG', 'ACT'],
        5: ['TAC', 'CCG', 'CGA', 'ACC', 'GTT', 'ATT'],
        6: ['TAC', 'CCT', 'CTT', 'TAA', 'GAA', 'TAG', 'ACT']
    }

    sfgTable = {
        1: ['CAT', 'GAT', 'TGG', 'CAC', 'CTT', 'CCA', 'TAG', 'ACT'],
        2: ['CAT', 'AAG', 'TAA', 'TGT', 'CTT', 'ACC', 'ATT'],
        3: ['CAT', 'AAA', 'AGT', 'CAA', 'CAC', 'CTT', 'CTT', 'ATT'],
        4: ['CAT', 'TAA', 'TGT', 'CTT', 'ACC', 'TAG', 'ACT'],
        5: ['CAT', 'BTT', 'CCT', 'CGA', 'CCA', 'ATT'],
        6: ['CAT', 'TAT', 'GCA', 'AAA', 'GAA', 'ATT']
    }

    options = {"eye": eyeTable, "leg": legTable, "arm": armTable, "haircolor": hairCTable,
               "hairtype": hairTTable, "skin": skinTable, "special": sfgTable}

    if table not in options:
        exit("BAD")

    dna = options[table][number]

    # Im losing my mind

    # Now we call translateDNA()

    print( f"""Using {table} as the DNA, we get the following:""" )
    translateDNA(dna)


while True:
    if input("Again? (y/n) ").casefold() == "y":
        if input("Dice? (y/n) ").casefold() == "y":
            number = input("Enter a number between 1 and 6, or leave blank for random: ")
            table = input("Enter table (eye, leg, arm, haircolor, hairtype, skin, special): ").replace(" ", "").casefold()

            if table not in ["eye", "leg", "arm", "haircolor", "hairtype", "skin", "special"]:
                print("Enter a valid table.")
                table = input("Enter table (eye, leg, arm, haircolor, hairtype, skin, special): ").replace(" ", "").casefold()
            
            if number == "":
                number = random.randint(1, 6)

            if type(number) == str and not number.isdigit():
                print("Enter a number.")
                number = input("Enter a number between 1 and 6: ")
            elif int(number) < 1 or int(number) > 6:
                print("Enter a number between 1 and 6.")
                number = input("Enter a number between 1 and 6: ")

            dice(table, int(number))
            

        else:
            print("Enter DNA in lengths of 3, and seperated by a space.")
            dna = input().split(" ")  # Creates a list
            # print(dna) # Testing purposes
            translateDNA(dna)
    else:
        break
