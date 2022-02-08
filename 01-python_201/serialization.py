import pickle

hackers = {"sandy": 1, "geohot": 100, "neo": 1000}

for key, value in hackers.items():
    print(key, value)

serialized_hackers = pickle.dumps(hackers)
print(serialized_hackers)

hackers_v2 = pickle.loads(serialized_hackers)

print(hackers_v2)

for key, value in hackers_v2.items():
    print(key, value)

with open("hackers.pickle", "wb") as handle:
    pickle.dump(hackers_v2, handle)

with open("hackers.pickle", "rb") as handle:
    hackers_v3 = pickle.load(handle)

print(hackers_v3)

for key, value in hackers_v3.items():
    print(key, value)
