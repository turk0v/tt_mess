def ordered(obj):
     if (type(obj) == type(dict)):
         return sorted((k, ordered(v)) for k, v in obj.items())
     if (type(obj) == type(list)):
         return sorted(ordered(x) for x in obj)
     else:
         return obj

def equals_json(json1, json2):
    return ordered(json1) == ordered(json2)