from typing import Union, Dict

GenericSchema = Dict[str, Union[str, float, int]]

#Aqui é importante ter isso, pois caso tenha uma mudança no tipo do dado ao fazer a requisição, o retorno vai ser None, então fica fácil identificar onde quebrou
CompraSchema: GenericSchema = {
    "ean" : int,
    "price" : str,
    "store" : int,
    "dateTime" : str
}