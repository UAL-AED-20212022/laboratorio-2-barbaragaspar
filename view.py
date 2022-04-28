import controller as c
from models.LinkedList import LinkedList

linkedList = LinkedList()

def main():
    while True:
        instruction = input().split()

        if instruction[0] == "RPI":
            pais_novo = instruction[1]
            c.RPI(linkedList, pais_novo)

        elif instruction[0] == "RPF":
            pais_novo = instruction[1]
            c.RPF(linkedList, pais_novo)

        elif instruction[0] == "RPDE":               
            pais_novo = instruction[1]
            pais_registado = instruction[2]
            c.RPDE(linkedList, pais_novo, pais_registado)

        elif instruction[0] == "RPAE":
            pais_novo = instruction[1]
            pais_registado = instruction[2]
            c.RPAE(linkedList, pais_novo, pais_registado)

        elif instruction[0] == "RPII":
            pais_novo = instruction[1]
            indice = int(instruction[2])
            c.RPII(linkedList, pais_novo, indice)

        elif instruction[0] == "VNE":
            c.VNE(linkedList)
 
        elif instruction[0] == "VP":
            nome_pais = instruction[1]
            c.VP(linkedList, nome_pais)

        elif instruction[0] == "EPE":
            c.EPE(linkedList)

        elif instruction[0] == "EUE":
            c.EUE(linkedList)

        elif instruction[0] == "EP":
            nome_pais = instruction[1]
            c.EP(linkedList, nome_pais)