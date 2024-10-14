# Implement your Hash Function here

def get_hashcode(value):
    '''
    Arguments:
    value: String
    
    Returns:
    Hash Code: Integer
    '''
    bitwise_hash = 0
    for s in value:
        bitwise_hash ^= (bitwise_hash << 5) + (bitwise_hash >> 2) + ord(s)

    return bitwise_hash


def div_compression(hash_code, table_size):
    '''
    Arguments:
    hash_code: Integer
    table_size: Integer
    
    Returns: 
    Compressed hash code: Integer
    '''
    compressed = hash_code % table_size
    return compressed
