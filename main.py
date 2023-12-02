#!/usr/bin/python3
import sys
import pandas as pd
from enum import Enum
class CsvField(Enum):
    ID = "LinkId"
    START = "Start"
    END = "End"
    CAP = "Capacity"
    WEI = "Weight"

class Link:
    def __init__(self, capacity: int, weight: int):
        self.capacity = capacity
        self.weight = weight
    def __str__(self) -> str:
        return f"Lk(cp:{self.capacity},wt:{self.weight})"

def parse_csv_network(csv: dict):
    matrice = []
    links_number = len(csv)
    for _ in range(links_number):
        matrice.append([None for _ in range(links_number)])
    for row in csv:
        start = ord(row[CsvField.START.value]) - ord("A")
        end = ord(row[CsvField.END.value]) - ord("A")
        cap = row[CsvField.CAP.value]
        wei = row[CsvField.WEI.value]
        link = Link(cap, wei)
        matrice[start][end] = link
    return matrice

def print_network(network_matrice: list):
    print("|||", end="")
    for i in range(len(network_matrice)):
        print(f"---({i})---|", end="")
    print()
    for j, row in enumerate(network_matrice):
        print(f"({j})", end="")
        for maybe_link in row:
            if maybe_link is None:
                print("    x     ", end="")
            else:
                print(f"{maybe_link} ", end="")
        print()

if __name__ == "__main__":
    csv_filepath = sys.argv[1]
    csv_dict = pd.read_csv(csv_filepath).to_dict("records")
    network = parse_csv_network(csv_dict)
    print_network(network)
