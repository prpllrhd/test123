DATA_SOURCE = (('key1', 'value1'),
               ('key1', 'value2'),
               ('key2', 'value3'),
               ('key2', 'value4'),
               ('key2', 'value5'),)
newdata = {}
for k, v in DATA_SOURCE:
    newdata.setdefault(k, []).append(v)
print newdata
