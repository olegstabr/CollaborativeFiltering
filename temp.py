# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных из файла
def load_data(path='./data/ml-100k/u.data'):
    prefs = {}
    for line in open(path):
        (user, movieId, rating, timestamp) = line.split("\t")
        prefs.setdefault(user, {})
        prefs[user][movieId] = float(rating)
    return prefs


# Визуализация матрицы R
def visualize_R(prefs):
    fig, ax = plt.subplots()
    min_val, max_val = 0, 15

    intersection_matrix = np.random.randint(0, 10, size=(max_val, max_val))

    ax.matshow(intersection_matrix, cmap=plt.cm.Blues)

    for i in xrange(15):
        for j in xrange(15):
            c = intersection_matrix[j, i]
            ax.text(i, j, str(c), va='center', ha='center')
    # plt.show()
    # ax.matshow(prefs, cmap=plt.cm.Blues)


def main():
    prefs = load_data()
    visualize_R(prefs)
    plt.show()

main()
