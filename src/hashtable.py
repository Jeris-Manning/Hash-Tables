# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key) % (self.capacity)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.



        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)
        '''
        bucket = self._hash_mod(key)
        newPair = LinkedPair(key, value)
        if self.storage[bucket] == None:
            self.storage[bucket] = newPair
        else:
            newPair.next = self.storage[bucket]
            self.storage[bucket] = newPair



        '''
        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # pass



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # pass
        key_hash = self._hash_mod(key)
        if self.storage[key_hash] == None:
            print(Warning("NICE TRY BUCKAROO"))

        # honk = self.storage[key_hash]
        # if type(honk) == LinkedPair:
        #     while type(honk) == LinkedPair:
        #         if honk.key == key:
        #             del(honk)
        #         else:
        #             honk = honk.next
        # if type(honk) == tuple:
        #     if honk[0] == key:
        #         del(honk)
        # print(Warning("BAD KEY"))
        hashed_key = self.storage[key_hash]
        # print(hashed_key.key, "HASHED KEY IN DELET FUNK")
        keyholder = None
        while hashed_key.next != None:
            if hashed_key.key == key:

                if keyholder != None:
                    keyholder.next = hashed_key.next
                hashed_key.value = None

                return
            else:
                keyholder = hashed_key
                hashed_key = hashed_key.next
        if hashed_key.key == key:

            hashed_key.value = None

            return
        print(Warning("bad key"))




    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # pass
        key_hash = self._hash_mod(key)

        hash_key = self.storage[key_hash]
        while hash_key.next != None:
            if hash_key.key == key:
                return hash_key.value
            else:
                hash_key = hash_key.next
        if hash_key.key == key:
                return hash_key.value
        return None





    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.storage = self.storage + [None] * self.capacity
        self.capacity = self.capacity * 2

        # print(self.storage)




# if __name__ == "__main__":
#     ht = HashTable(2)

    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    # print(ht.storage, "checkpoint")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print(ht.storage[0].key, ht.storage[0].value, ht.storage[0].next)
    # print(ht.storage[0].next)
    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(ht.storage, "NOW EVEN BIGGER")

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # print(ht.storage[0].key, ht.storage[0].value, ht.storage[0].next)
    # print(ht.storage[1].key, ht.storage[1].value, ht.storage[1].next)


    # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")
