import pickle
from typing import Any


def Deserialize_from_file(filename) -> Any:
    with open(f"../files/{filename}.pkl", "rb") as f:
        return pickle.load(file=f)


def Deserialize(data):
    """
    This method should be passed with the pickle serialized data which returns the deserialized data
    :param data: pickle serialized data
    :return: pickle deserialized original data
    """
    return pickle.loads(data=data)


if __name__ == '__main__':
    data = Deserialize_from_file(filename="test1")
    print(data)
