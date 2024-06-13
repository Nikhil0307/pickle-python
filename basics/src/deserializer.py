import pickle
from typing import Any


def Deserialize_from_file(filename) -> Any:
    with open(f"../files/{filename}.pkl", "wb") as f:
        return pickle.load(file=f)


if __name__ == '__main__':
    Deserialize_from_file(filename="test1")
