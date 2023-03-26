import csv
import random as rnd

# Zmienne globalne
label_to_numeric = {}
alfa = 0
dimension_count = 0


# Wczytywanie danych z pliku CSV
def load_data(file_name):
    # Wczytywanie pliku do listy
    data = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            label = row[-1]
            if label not in label_to_numeric:
                label_to_numeric[label] = len(label_to_numeric)
            numeric_label = label_to_numeric[label]

            data.append([float(i) if idx != len(row) - 1 else numeric_label for idx, i in enumerate(row)])

    # Ile kolumn występuje w danych (ile wymiarów)
    global dimension_count
    dimension_count = len(data[0]) - 1
    return data


def random_weight_vector():
    weights_vector = []
    # Wagi początkowe wektora wag
    for i in range(dimension_count):
        val = rnd.random()
        weights_vector.append(val)

    return weights_vector
