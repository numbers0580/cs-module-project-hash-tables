class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.hTable = [None] * capacity

        # Counter
        self.items = 0

    # def insert_at_head(self, node):
    #     node.next = self.head
    #     self.head = node


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.items / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        # print(f"Initial hash value: {hash}")
        for i in key:
            # hash = ((hash << 5) + hash) + ord(i)
            hash = (hash * 33) + ord(i) # both this and the line above works the same
            # print(f"Loop: ord(i) = {ord(i)}, hash value = {hash}")
        return hash & 0xffffffff


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # Day 1
        # hIndex = self.hash_index(key)
        # self.hTable[hIndex] = HashTableEntry(key, value)

        # Day 2
        hIndex = self.hash_index(key)
        if self.hTable[hIndex] == None:
            # There are no entries here, so we could place one here
            self.hTable[hIndex] = HashTableEntry(key, value)
            self.items += 1 # Increment count to show we added an item where there was previously None
        else:
            prev = None
            cur = self.hTable[hIndex]

            while cur != None:
                if cur.key == key:
                    # Found given key, store value
                    cur.value = value
                    return
                # Didn't find key at current position, move prev & cur by one
                prev = cur
                cur = cur.next
            # Out of while-loop, so we must've found the right key. Have prev point to the new value as the next one in Linked List
            prev.next = HashTableEntry(key, value)
            self.items += 1

        # Outside of if-else. Now check if added value requires a resize
        if self.get_load_factor() >= 0.7:
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # Day 1
        # hIndex = self.hash_index(key)
        # self.hTable[hIndex] = HashTableEntry(key, None)

        # Day 2
        hIndex = self.hash_index(key)
        # print(f"DEL -- index = {hIndex}, key = {key}, value = {self.hTable[hIndex].value}")

        if self.hTable[hIndex] == None:
            # Empty table
            return "Entered key was not found"
        elif self.hTable[hIndex].key == key:
            # I created this because there was some issue with initializing prev = None in the else-statement below
            # It created an error inside the if cur.key == key statement below. As you can see, I tried multiple ways to fix it to no avail
            # This elif I created is a workaround
            self.hTable[hIndex] = self.hTable[hIndex].next
            self.items -= 1
        else:
            prev = None
            cur = self.hTable[hIndex]
            # print(f"DEL outisde While: cur.key = {cur.key}")

            while cur != None:
                # print(f"DEL inside While: cur.key = {cur.key}, key = {key}")
                if cur.key == key:
                    # print(f"DEL If-statement: cur.key = {cur.key}, key = {key}")
                    if prev != None:
                        prev.next == cur.next
                    # Still getting issues after addressing prev = None, trying to manually set cur to None (delete)
                    cur = HashTableEntry(key, None)
                    # Okay, still getting errors. Try removing cur.next
                    cur.next = None
                    self.items -= 1
                    return
                prev = cur
                cur = cur.next
                # print(f"DEL skipped if: new cur.key = {cur.key}")
                if cur == None:
                    return "Key wasn't found in table."

        if self.get_load_factor() < 0.2 and self.capacity > MIN_CAPACITY:
            # I should never have to worry about creating conditionals to check capacity > MIN and capacity/2 < MIN
            # since the root capacity value is 2^x. In this case, 2^3 = 8
            self.resize(self.capacity // 2)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # Day 1
        # hIndex = self.hash_index(key)
        # val = self.hTable[hIndex].value
        # return val

        # Day 2
        hIndex = self.hash_index(key)
        cur = self.hTable[hIndex]
        val = None # Initialization. Will return None if val doesn't get replaced in loop below
        while cur != None:
            if cur.key == key:
                # Found It!
                val = cur.value
                break
            cur = cur.next
        return val


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        # M-2
        # Create temporary table of hTable
        currTable = self.hTable.copy()
        # Change capacity amount
        self.capacity = new_capacity
        # Now that hTable is stored in a temp, re-map hTable with the new capacity
        self.hTable = [None] * new_capacity
        self.items = 0 # resetting the counter

        for obj in currTable:
            if obj != None:
                # Stored obj into a temp to use in the while-loop below without affecting obj
                currObj = obj
                while currObj != None:
                    self.put(currObj.key, currObj.value)
                    currObj = currObj.next



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
