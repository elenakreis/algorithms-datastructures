from garbage_bins import Garbage
import numpy as np

def gather_input(list):
    n, m, k = int(list[0]), int(list[1]), int(list[2])
    edges = np.zeros((m,m))
    for i in range(3, len(list), 2):
        a, b = int(list[i])-1, int(list[i+1])-1
        edges[a][b] = 1
        edges[b][a] = 1
    return edges, k


files = ['small_1','small_2','small_3','small_4','small_5','small_6','big_1','big_2','big_3','big_4','big_5','big_6','extra_1','extra_2','extra_3','extra_4','extra_5','extra_6','extra_7','extra_8']
yes, no = 0, 0

for file in files:
    file_in = open("./samples/"+file+".IN","r")
    input = file_in.read().split()
    edges, k = gather_input(input)
    garbage = Garbage(edges, k)
    max_set = garbage.approximate()

    if(len(max_set)>=k):
        result = "possible"
    else:
        result = "impossible"

    file_out = open("./samples/"+file+".OUT","r")
    output = file_out.read().split()[0]
    print(file, " ", result, " ", result==output)
    if result == output:
        yes +=1
    else:
        no+=1

    file_in.close()
    file_out.close()

print("CORRECT ", yes, "        INCORRECT ",no)
