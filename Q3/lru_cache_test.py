from lru_cache import LRUCache
import time

'''
    create an instance of LRUCache object, insert some values, retrieve some values
    and display the cached items.
'''

# An instance of LRUCache object with size = 5 and expiration time of 10 s.
cache = LRUCache(5, 10)


cache.set_item('A',5)
cache.set_item('B',3)
cache.set_item('C',4)
cache.set_item('D',1)
cache.get_item('A')
print(cache.display())
cache.set_item('A',2)
cache.set_item('B',0)
cache.set_item('E',2)
cache.set_item('F',3)
cache.get_item('A')
print(cache.display())
cache.set_item('B',3)
cache.set_item('C',4)
cache.set_item('D',1)
print(cache.display())

# To see the time expiration
time.sleep(10)
cache.set_item('D',10)
print(cache.display())
