import requests
import json


def num_of_pages_and_amount(url,search_parameters):

    """
    Calcula el número de páginas y la cantidad de elementos
    totales resultantes de una búsqueda por parámetros en
    la API a consultar.

    """

    response = requests.get(url, params= 
    search_parameters)
    data = json.loads(response.content)

    amount = int(data["total"])
    pages = (amount//20)+1


    return pages,amount


def url_generator_list(url,search_parameters,pages):

    """
    Retorna una lista que contiene tantas URL's como páginas
    se ingresen en el parámetro "pages".

    """

    list_urls = []
    for num in range(pages):
        list_urls.append(url+"?"+search_parameters+"&page="+str(num+1))
        
    for u in list_urls:
        print(u) 


    return list_urls

