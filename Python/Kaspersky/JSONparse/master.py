import json

input = '{"a": {"a1": null,"a2": 2},"b": {"b1": "12","b2": 1.2}, "c": [10, 20], "d": 50}'

parsed = json.loads(input)

print({ k: v for d in [ { f'{k}.{i}': v for i, v in enumerate(parsed[k])} if type(parsed[k]) is list else { f'{k}.{kk}': v for kk, v in parsed[k].items() } if type(parsed[k]) is dict else { k: parsed[k] } for k in parsed.keys() ] for k, v in d.items()})
