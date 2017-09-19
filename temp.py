# -*- coding: utf-8 -*-
from scipy.stats.stats import pearsonr


# Загрузка данных из файла
def load_data(path='./data/ml-100k/u1.base'):
    prefs = {}
    with open(path) as file:
        for line in file:
            (user, movieId, rating, timestamp) = line.split("\t")
            prefs.setdefault(user, {})
            prefs[user][movieId] = float(rating)
    return prefs


# Вычисление коэффициента Пирсона
def pearson(x, y, common):
    n = len(common)
    # Простые суммы
    sumX = sum([float(x[i]) for i in common])
    sumY = sum([float(y[i]) for i in common])

    # Суммы квадратов
    sumXSq = sum([x[i] ** 2 for i in common])
    sumYSq = sum([y[i] ** 2 for i in common])
    # Сумма проивзедений
    pSum = sum([x[i] * y[i] for i in common])

    # Коэффициент корреляции Пирсона
    num = pSum - sumX * sumY / n
    den = ((sumXSq - pow(sumX, 2) / n) * (sumYSq - pow(sumY, 2) / n)) ** .5

    if den == 0:
        return 0
    k = num / den
    return k


def pearson2(x, y, common):
    n = len(common)
    # Простые суммы
    sumX = sum([float(x[i]) for i in common])
    sumY = sum([float(y[i]) for i in common])
    # Среднее по x и y
    averageX = float(sumX / n)
    averageY = float(sumY / n)
    # Сумма числителя
    num = sum([(float(x[i]) - averageX) * (float(y[i]) - averageY) for i in common])
    den = (sum([pow((float(x[i]) - averageX), 2) for i in common]) * sum(
        [pow(float(y[i]) - averageY, 2) for i in common])) ** .5
    if den == 0:
        return 0
    k = num / den
    return k


def pearson_sys(x, y):
    dict1 = {}
    dict2 = {}
    for item in x:
        if item in y:
            dict1[item] = x[item]
            dict2[item] = y[item]
    return pearsonr(dict1.values(), dict2.values())[0]


# Реализация функции близости 1 (Коэффициент корреляции Пирсона)
def sim_distance_1(prefs, person1, person2):
    # Получить список предметов, оцененных обоими
    common = {}
    for item in prefs[str(person1)]:
        if item in prefs[str(person2)]:
            common[item] = 1

    # Если нет ни одной общей оценки, вернуть 0
    if len(common) == 0:
        return 0
    return pearson2(prefs[str(person1)], prefs[str(person2)], common)


# Реализация функции близости 1 (Коэффициент корреляции Пирсона)
def sim_distance_pearson_sys(prefs, person1, person2):
    # Получить список предметов, оцененных обоими
    common = {}
    for item in prefs[str(person1)]:
        if item in prefs[str(person2)]:
            common[item] = 1

    # Если нет ни одной общей оценки, вернуть 0
    if len(common) == 0:
        return 0

    return pearson_sys(prefs[str(person1)], prefs[str(person2)])


# Реализация функции близости 2 (Коэффициент Жаккара)
def sim_distance_2(prefs, person1, person2):
    # Получить список предметов, оцененных обоими
    common = {}
    dict1 = prefs[str(person1)]
    dict2 = prefs[str(person2)]
    for item in dict1:
        if item in dict2:
            common[item] = 1

    # Если нет ни одной общей оценки, вернуть 0
    n = len(common)
    if n == 0:
        return 0
    return n / float(len(dict1) + len(dict2) - n)


# Возвращает отранжированных k пользователей
def top_matches(prefs, person, k=5, similarity=sim_distance_1):
    scores = [(similarity(prefs, person, int(other)), other)
              for other in prefs if int(other) != person]
    scores.sort()
    scores.reverse()
    return scores[0:k]


# Получить неизвестную оценку объекта для пользователя
def get_rating(prefs, person, object_id, similarity=sim_distance_1):
    # Посчитать меру близости пользователя со всеми остальными (кроме себя самого)
    # С помощью topMatches найти k самых похожих пользователя
    # Вычислить оценку для объекта object_id
    matches = top_matches(prefs, person, similarity=similarity)
    sim = {}
    for item in matches:
        values = prefs[item[1]]
        sim[item[1]] = values

    num = sum([float(sim[item[1]][str(object_id)]) * item[0]
               for item in matches if str(object_id) in sim[item[1]].keys()])
    den = sum([item[0] for item in matches])
    if den == 0:
        return 0
    rating = num / den
    return rating


def get_rating_for_user():
    pass


def main():
    prefs = load_data()
    print('Пирсон мой      user1=1 user2=120  = %s' % sim_distance_1(prefs, 1, 120))
    print('Пирсон из библ. user1=1 user2=120  = %s' % sim_distance_pearson_sys(prefs, 1, 120))
    print('Жаккар          user1=1 user2=120  = %s' % sim_distance_2(prefs, 1, 120))
    print('Топ-5 Пирсон     = %s' % top_matches(prefs, 1))
    print('Топ-5 Жаккар     = %s' % top_matches(prefs, 1, similarity=sim_distance_2))
    # print
    # dict1 = {}
    # dict2 = {}
    # for item in prefs[str(1)]:
    #     if item in prefs[str(120)]:
    #         dict1[item] = prefs[str(1)][item]
    #         dict2[item] = prefs[str(120)][item]
    # print('1 оценки = %s' % dict1)
    # print('120 оценки = %s' % dict2)
    print
    print('Пирсон: Фильм id = %s | Спрогнозированная оценка = %f' % (742, get_rating(prefs, 1, 742)))
    print('Жаккар: Фильм id = %s | Спрогнозированная оценка = %f' % (
        742, get_rating(prefs, 1, 742, similarity=sim_distance_2)))


main()
