# -*- coding: utf-8 -*-
import json
import os

with open('json/item.json') as json_data:
    data_dict = json.load(json_data)
def get_item(n):
    if n==0:
        return "N/A"
    return (data_dict['data'][str(n)]["name"])

print(get_item(6630))