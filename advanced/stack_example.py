import pickletools
import pickle

# Example dictionary
data = {'x': 12, 'y': [1, 2, 3]}

# Serialize the object
pickled_data = pickle.dumps(data)

# Deserializing the byte stream to see opcodes
pickletools.dis(pickled_data)

"""
OUTPUT ::
    0: \x80 PROTO      5                   # protocol version
    2: \x95 FRAME      0x000000000000004f  # Marks a Frame
   11: \x94 DICT                           # Start of a dict object
   12: \x94 MARK                           # Mark stack for dict key-value pairs
   13: \x8c     SHORT_BINUNICODE 'x'       # Push key 'x'
   18: K        BININT1    42              # Push value 42
   25: ]        EMPTY_LIST                 # Start a list object
   33: e        APPENDS                    # Append list to dict
   35: .        STOP                       # End of the stream
"""
