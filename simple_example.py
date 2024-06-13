import pickle
#This example serializes the object into byte stream and store 
data = {
    'a': [1, 2.0, 3+4j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

pickled_object = pickle.dumps(obj=data,protocol=pickle.HIGHEST_PROTOCOL)
print(pickled_object)

#output -> b'\x80\x05\x95w\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x01a\x94]\x94(K\x01G@\x00\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x07complex\x94\x93\x94G@\x08\x00\x00\x00\x00\x00\x00G@\x10\x00\x00\x00\x00\x00\x00\x86\x94R\x94e\x8c\x01b\x94\x8c\x10character string\x94C\x0bbyte string\x94\x86\x94\x8c\x01c\x94\x8f\x94(\x89\x88N\x90u.'

deserialized_object = pickle.loads(pickled_object)
print(deserialized_object)

#output -> {'a': [1, 2.0, (3+4j)], 'b': ('character string', b'byte string'), 'c': {False, True, None}}
