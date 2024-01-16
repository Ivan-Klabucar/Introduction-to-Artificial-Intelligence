import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--train", help="Putanja do datoteke skupa podataka za treniranj")
parser.add_argument("--test", help="Putanja do datoteke skupa podataka za testiranje")
parser.add_argument("--nn", help="Arhitektura neuronske mreˇze")
parser.add_argument("--popsize", type=int, help="Velicina populacije genetskog algoritma")
parser.add_argument("--elitism", type=int, help="Elitizam genetskog algoritma")
parser.add_argument("--p", type=float, help="Vjerojatnost mutacije svakog elementa kromosoma genetskog algoritma")
parser.add_argument("--K", type=float, help="Standardna devijacija Gaussovog suma mutacije")
parser.add_argument("--iter", type=int, help="Broj iteracija genetskog algoritma")
args = parser.parse_args()

