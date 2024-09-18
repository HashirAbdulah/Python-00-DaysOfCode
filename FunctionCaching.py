# Function caching allows us to cache the return values of a function depending on the arguments. Its helps in reducing again computation for the same values or arguments... But there are disadvantages in caching like overhead memory(memory usage) and mutable objects like lists and dictionaries are not cached...
from functools import lru_cache
import time
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*3

print(fx(5))
print("Done for 5")
print(fx(4))
print("Done for 4")
print(fx(6))
print("Done for 6")
fx.cache_clear

print(fx(5))
print("Done for 5")
print(fx(4))
print("Done for 4")
print(fx(6))
print("Done for 6")
print(fx(61))
print("Done for 61")
