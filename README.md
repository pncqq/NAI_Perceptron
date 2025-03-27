# 🤖 NAI_Perceptron

Projekt przedstawia implementację klasycznego **algorytmu perceptronu** do klasyfikacji binarnej danych z ograniczonego zbioru **Iris**. Celem jest rozróżnienie gatunków *Iris-versicolor* i *Iris-virginica*.

## 📂 Zawartość repozytorium

- `main.py` – główny plik z implementacją algorytmu perceptronu
- `functions.py` – funkcje pomocnicze do obsługi danych, klasyfikacji i uczenia
- `Data/perceptron.data` – zbór treningowy (CSV)
- `Data/perceptron.test.data` – zbór testowy (CSV)

## 🧠 Funkcjonalności

- Wczytanie danych treningowych i testowych z plików CSV
- Dynamiczne dostosowanie liczby wag do liczby cech
- Wybór współczynnika uczenia (learning rate)
- Trening perceptronu przez zadaną liczbę epok
- Testowanie dokładności modelu na danych testowych
- Klasyfikacja ręcznych wektorów wejściowych

## ⚙️ Technologie

- Python 3.x
- NumPy

## ▶️ Jak uruchomić

1. Sklonuj repozytorium:
```bash
git clone https://github.com/pncqq/NAI_Perceptron.git
cd NAI_Perceptron
```

2. Uruchom program:
```bash
python main.py
```

> 🔎 W trakcie działania program poprosi o podanie współczynnika uczenia i liczby epok. Dane z plików zostaną automatycznie załadowane.

## 📈 Wskazówki

- Najlepsze rezultaty daje **mały learning rate** (np. `0.01`) i wiele epok treningu
- Klasy Iris-versicolor i Iris-virginica **nie są idealnie separowalne**, ale mimo to perceptron potrafi osiągnąć wysoką skuteczność

## 👨‍💻 Autor
**Filip Michalski**  
Projekt wykonany w ramach kursu NAI (Narzędzia AI) jako praktyczne wprowadzenie do algorytmów uczenia nadzorowanego.
