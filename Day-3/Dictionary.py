#dictionary = a collection of {key : value} pairs
#             ordered and changeable. No duplicates
#             eg (ID-NAME) (COUNTRY-CAPITALS)

capitals = {"USA":"Washington",
            "France":"Paris",
            "India": "New Delhi",
            "Russia":"Moscow"}

print(capitals.get("Russia"))
print(capitals.get("Japan")) #if key is not present then python return NONE. Comes handy in if else.

capitals.update({"Germany":"Berlin"}) ##update can add new key values.
print(capitals)

capitals.update({"Germany":"Tokyo"}) ###Update can also modify existing key-value pairs.
print(capitals)

capitals.popitem() ###Used to pop the last add key-value pair
print(capitals)

keys = list(capitals.keys()) ###keys() method return all of the keys. Returns an object
print(keys)

values = list(capitals.values()) ###values() method return all the values. Returns an object
print(values)

items = list(capitals.items()) ###Returns a dictionary object which resembles like a 2d list of tuples.
print(items)

for key,value in capitals.items():
    print(f"{key}: {value}")