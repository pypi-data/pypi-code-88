import os


if __name__ == '__main__':
    name = "test"
    nbr = 100
    # en python on utilise la notaion underscore (en Java par exemple en utilse CamelCase)
    nbr_float = 100.52
    print(name)
    print(nbr)
    print(nbr_float)

    # afficher le type d'une variable
    print(type(name))

    # Collection
    my_list = [1, 3, 3, 4]
    # dans les autres langages on peut pas avoir ca pcq ils sont typés
    my_list_2 = [1, "chain de char", 4]

    my_dict = {
        "key_2": 1,
        "toto": "titi"
    }
    print(my_dict["key_2"])
    print(my_dict.keys())
    print(my_dict.values())
