d1 = {"prop1a": "prop1a",
    "prop1b": "prop1b"}
d2 = {"prop2a": "prop2a",
    "prop2b": "prop2b"}

d3 = d1 | d2
# d3 = {**d1, **d2}
print(d3)