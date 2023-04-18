import csv
from pathlib import Path

from tqdm.auto import tqdm

if __name__ == "__main__":
    data = []

    n = 0
    with Path(__file__).parent.joinpath("adresses-france.csv").open("r") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in tqdm(reader):
            n += 1
            if n > 5_000_000:
                break
    print(f"The file has {n} addresses.")