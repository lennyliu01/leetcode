import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequencies(text):
    frequencies = defaultdict(int)
    for char in text:
        frequencies[char] += 1
    return frequencies

def build_huffman_tree(text):
    frequencies = calculate_frequencies(text)
    priority_queue = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        combined_node = Node(None, left.freq + right.freq)
        combined_node.left = left
        combined_node.right = right
        heapq.heappush(priority_queue, combined_node)

    return priority_queue[0]

def generate_codes(node, current_code='', codes={}):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code

    generate_codes(node.left, current_code + '0', codes)
    generate_codes(node.right, current_code + '1', codes)

    return codes

text = 'this is an example for huffman encoding'
huffman_tree = build_huffman_tree(text)
huffman_codes = generate_codes(huffman_tree)
print('Huffman codes:', huffman_codes)
