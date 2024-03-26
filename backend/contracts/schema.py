from typing import Union, Dict

GenericSchema = Dict[str, Union[str, float, int]]

CompraSchema: GenericSchema = {
    "ean" : int,
    "price" : str,
    "store" : int,
    "dateTime" : str
}