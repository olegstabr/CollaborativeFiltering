# -*- coding: utf-8 -*-


# Загрузка данных из файла
def load_data(path='./data/ml-100k/u1.base'):
    prefs = {}
    with open(path) as file:
        for line in file:
            (user, movieId, rating, timestamp) = line.split("\t")
            prefs.setdefault(movieId, {})
            prefs[movieId][user] = float(rating)
    return prefs

