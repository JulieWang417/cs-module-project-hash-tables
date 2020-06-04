class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None 

    def __repr__(self):
        return (f"(key = {self.key}, value = {self.value})")

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity, minimum_size=128):
        self.capacity = capacity # number of buckets in the hash table
        self.storage = [None] * int(self.capacity)
        self.size = 0 # size is the total numbers of KV(key & value)
        


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return float(self.size)/self.capacity
        # number of things stored in the hash table / number of slots in the array

        """
        In Python, every integer is associated with its two's complement 
        and its sign. However, doing bit operation "& mask" loses the track of sign.
        For example, -1 & 0xffffffff becomes a huge positive number 4294967295.
        Therefore, after the while loop, a is the two's complement of the final 
        result as a 32-bit unsigned integer.

        """


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        total = 0
        for b in key.encode():
            total += b
            total &= 0xffffffffffffffff
        
        return total



    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        total = 0
        for b in key.encode():
            total += b
            total &= 0xffffffff  # 0xffffffff表示的是一个十六进制数, single f = 1111
            # 0xFFFFFFFF is a hexadecimal integer constant. Its decimal value is
            # simply 4294967295. 
        
        return total


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # Find the slot for the key
        # Search the linked list for the key
        # If found, update it
        # If not found, make a new HashTableEntry and add it to the list

        index = self.hash_index(key)  
        head = self.storage[index]  # set head as the head node
        # if the head is not empty, traverse the whole linked list
        while head is not None:
            if head.key == key: # compare if the two keys are equal
                # if they are equal, overwrite the value
                head.value = value
                return # job done! 
            else:
                # if we didn't find the key, traverse to the next node
                head = head.next 
        # append the new kv to the end
        head = HashTableEntry(key=key, value=value)
        # since we added a kv, sized up
        self.size += 1
        
        # Check load factor if greater than 0.7 (70% full)
        if (self.size / self.capacity) <= 0.2:
            # If load factor less than 0.2, half the table size
            self.resize(self.capacity/2)
        elif (self.size / self.capacity) >= 0.7:
            # If load factor greater than 0.7, double size
            self.resize(2*self.capacity)
        


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Find the slot for the key
        # Search the linked list for the key
        # If found, delete it from the linked list, then return the deleted value
        # If not found, return None

        index = self.hash_index(key)
        head = self.storage[index]
        keyFound = False
        prev = None
        current = head
        while current is not None:
            if current.key == key:
                keyFound = True
                self.size -= 1
                if prev is not None:
                    prev.next = current.next
                else:
                    head = current.next
                return
            else:
                prev = current
                current = current.next
            
        if not keyFound:
            print('Key {} not found'.format(key))
        else:
            print('Key {} deleted'.format(key))



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Find the slot for the key
        # Search the linked list for the key
        # If found, return the value
        # If not found, return None
        index = self.hash_index(key)
        head = self.storage[index]
        while head is not None:
            if head.key == key:
                return head.value
            else:
                head = head.next
        return None
        
    # When is the hash table overloaded?
        # It's overloaded when load factor > 0.7
        #It's underloaded when load factor < 0.2 (Stretch)
    """
    Resize:
    In a nutshell, take everything out of the old hash table array, and put it in a
    new, resized array.
    1. Allocate a new array of bigger size, typically double the previous size
    (or half the size if resizing down, down to some minimum)
    2. Traverse the old hash table -- O(n) over the number of elements in the hash
    table 
    For each of the elements:
        Figure it's slot in the bigger (or smaller), new array
        Put it there
    Automatically do this when the hash table is overloaded, or underloaded
    (stretch).
    """

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        
        new_ht = HashTable(new_capacity)
        
        for item in self.storage:
            while item is not None:
                new_ht.put(key,value)
                item = item.next
        
        self.capacity = new_ht.capacity
        self.storage = new_ht.storage



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
    

    """
    An instance of HashMap has two parameters that affect its performance: initial 
    capacity and load factor. The capacity is the number of buckets in the hash table, 
    and the initial capacity is simply the capacity at the time the hash table is created.
    The load factor is a measure of how full the hash table is allowed to get before its 
    apacity is automatically increased. When the number of entries in the hash table 
    exceeds the product of the load factor and the current capacity, the hash table is 
    rehashed (that is, internal data structures are rebuilt) so that the hash table has 
    approximately twice the number of buckets.

    As a general rule, the default load factor (.75) offers a good tradeoff between time
    and space costs. Higher values decrease the space overhead but increase the lookup 
    cost (reflected in most of the operations of the HashMap class, including
    get and put). The expected number of entries in the map and its load factor
    should be taken into account when setting its initial capacity, so as 
    to minimize the number of rehash operations. If the initial capacity is 
    greater than the maximum number of entries divided by the load factor, 
    no rehash operations will ever occur.

    """