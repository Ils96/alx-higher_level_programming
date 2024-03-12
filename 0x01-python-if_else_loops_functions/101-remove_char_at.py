#!/usr/bin/python3
def remove_char_at(str, q):
    if q < 0:
        return (str)
    return (str[:q] + str[q+1:])
