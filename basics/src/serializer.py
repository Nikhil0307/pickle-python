import pickle
from typing import Any


def Serialize_to_file(data_to_serialize, filename) -> Any:
    with open(f"../files/{filename}.pkl", "wb") as f:
        pickle.dump(obj=data_to_serialize, file=f, protocol=pickle.HIGHEST_PROTOCOL)
        return True


if __name__ == '__main__':
    data = {
        'a': [1, 2.0, 3 + 4j],
        'b': ("character string", b"this is bytes"),
        'c': {None, True, False}
    }
    Serialize_to_file(data_to_serialize=data, filename="test1")
