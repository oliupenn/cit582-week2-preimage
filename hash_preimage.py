import hashlib
import os

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    matched = False
    while not matched:
        txt = os.urandom(2)
        hashed_txt = hashlib.sha256(txt).hexdigest()
        l = len(target_string)
        if l % 4 == 0:
            num_digits_hex = int(l/4)
        else:
            num_digits_hex = int(l/4)+1
        hashed_trimmed_txt = hashed_txt[-num_digits_hex:]
        x = hex_to_bin(hashed_trimmed_txt)
        x_same_length_target = x[-l:]
        if is_matched(x,target_string):
            matched = True
    return txt

def is_matched(x,y):
    res = True
    for i in range(len(y)):
        if y[i] != x[i]:
            res = False
    return res

def hex_to_bin(x):
    length = len(x)
    res = int(x,16)
    res = bin(res)
    res = res[2:]
    length_diff = length*4 - len(res)
    if length_diff != 0:
        for i in range(length_diff):
            res = '0'+res       
    return res
