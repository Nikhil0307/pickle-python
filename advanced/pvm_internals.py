import pickletools
import pickle

a = []
b = [a]
a.append(b)

pickled_data = pickle.dumps(a)

# Deserializing the byte stream to see opcodes
pickletools.dis(pickled_data)

"""
OUTPUT:: 
    0: \x80 PROTO      4                # protocol version
    2: \x95 FRAME      9              # Marks a Frame 
   11: ]    EMPTY_LIST                # Create empty list
   12: \x94 MEMOIZE    (as 0)         # Save Object as memo 0
   13: ]    EMPTY_LIST                # Create empty list
   14: \x94 MEMOIZE    (as 1)         # Save Object as memo 1
   15: h    BINGET     0              # Retrieve Object memo 0
   17: a    APPEND                    # Append Object
   18: a    APPEND                    # Append Object
   19: .    STOP                      # End of Serialization Stream
"""
