import json
import os


def json_comparing(json1: "Json1 filename",
                   json2: "Json2 filename") -> "Boolean":
    """The function returns True if the corresponding
    fields of type float are equal to the fifth digit."""

    # Считываем Json_1 и Json_2

    json_file_rel_path_1 = os.path.join(os.path.dirname(__file__), json1)
    with open(json_file_rel_path_1) as json_1:
        data_1 = json.load(json_1)

    json_file_rel_path_2 = os.path.join(os.path.dirname(__file__), json2)
    with open(json_file_rel_path_2) as json_2:
        data_2 = json.load(json_2)

    # Значение по ключам

    id_values_list_1 = [f'{val["id"]:0.5f}' for val in data_1["ids"]]
    id_values_list_2 = [f'{val["id"]:0.5f}' for val in data_2["ids"]]

    # Комбинации значений

    id_values_combinations = [(x,y) for x in id_values_list_1
                              for y in id_values_list_2]

    return all(map(lambda x: x[0] == x[1], id_values_combinations))


print(json_comparing("json_1.json", "json_2.json"))