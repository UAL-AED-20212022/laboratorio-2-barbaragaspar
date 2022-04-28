from models.LinkedList import LinkedList

###### Registar pais no inicio da lista ######

def RPI(linkedList, pais_novo): #Criar uma função que registe o pais no inicio da lista
    linkedList.insert_at_start(pais_novo) #ir buscar a função à linkedlist
    linkedList.traverse_list() # mostrar a lista
    return #se for igual a 1 vai mostrar a traverse_list

###### Registar pais no final da lista #######

def RPF(linkedList, pais_novo):
    linkedList.insert_at_end(pais_novo)
    linkedList.traverse_list() #mostrar a lista
    return 

###### Registar pais depois do outro elemento jé registado ###

def RPDE(linkedList, pais_novo, pais_registado):
    linkedList.insert_after_item(pais_registado, pais_novo)
    linkedList.traverse_list()
    return

###### Registar pais antes de outro elemento ja registado ###

def RPAE(linkedList, pais_novo, pais_registado):
    linkedList.insert_before_item (pais_registado, pais_novo)
    linkedList.traverse_list()
    return

##### Registar pais num determinado indice ####

def RPII(linkedList, pais_novo, indice: int):
    linkedList.insert_at_index(indice, pais_novo)
    linkedList.traverse_list()
    return

###### Verificar número de elementos da lista ####

def VNE(linkedList):
    print(f"O número de elementos são {linkedList.get_count()}")
    return

##### Verificar se um pais se encontra na lista ####
def VP(linkedList, nome_pais):
    if (linkedList.search_item(nome_pais) == True):
        print(f"O pais {nome_pais} encontra-se na lista")
        return

    elif (linkedList.search_item(nome_pais) == False):
        print(f"O país {nome_pais} não se encontra na lista")
        return

###### Eliminar o primeiro elemento da lista ###
def EPE(linkedList):
    pais = linkedList.start_node.item
    linkedList.delete_at_start()
    print(f"O país {pais} foi eliminado da lista")
    return

###### Eliminar o ultimo elelmento da lista ####
def EUE(linkedList):
    pais = linkedList.get_last_node()
    linkedList.delete_at_end()
    print(f"O país {pais} foi eliminado da lista")
    return

##### Eliminar um determinado pais da lista ###
def EP(linkedList, nome_pais):
    if (linkedList.search_item(nome_pais) == True):
        linkedList.delete_element_by_value(nome_pais)
        print(f"O pais {nome_pais} foi eliminado da lista")
        return

    elif (linkedList.search_item(nome_pais) == False):
        print(f"O país {nome_pais} não se encontra na lista")
        return
    