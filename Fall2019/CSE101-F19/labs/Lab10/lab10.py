from PythonLabs.BitLab import  *

def buildtree(filename):
    """Build a Huffman tree using letters and frequencies in a file."""
    pq = init_queue(read_frequencies(filename))
    while len(pq) > 1:
        n1 = pq.pop()
        n2 = pq.pop()
        pq.insert(Node(n1,n2))
    return pq[0]

# Write your code below, following the steps from T71 to T91 in Chapter 8 of the Conery Textbook
#  After each step, be sure to print the results and try to understand what is happening






# You will implement this function for Problem 2

def print_hex(string):
    decimal_to_hex_string_dict = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6',
                           7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C',
                           13:'D', 14:'E', 15:'F' }




# Uncomment the line below when working on Problem 2 to test your program
# print_hex("Hello")  # This should print "48 65 6C 6C 6F"
