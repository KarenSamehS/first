import random
import time
import matplotlib.pyplot as plt

def multiply_block(A, B, C, n, bsize):
    # Initialize matrix C with zeros
    for i in range(n):
        for j in range(n):
            C[i][j] = 0.0
    
    # Amount that fits evenly into blocks
    en = bsize * (n // bsize)
    
    # Main loop with blocking
    for kk in range(0, en, bsize):
        for jj in range(0, en, bsize):
            for i in range(n):
                for j in range(jj, jj + bsize):
                    sum_val = C[i][j]
                    for k in range(kk, kk + bsize):
                        sum_val += A[i][k] * B[k][j]
                    C[i][j] = sum_val

def matrix_multiplication(n, bsize):
    # Generate random matrices
    A = [[random.randint(0, 25) for m in range(n)] for m in range(n)]
    B = [[random.randint(0, 25) for l in range(n)] for l in range(n)]
    C = [[0 for b in range(n)] for b in range(n)]

    # Perform matrix multiplication using blocking
    start_time = time.time()
    multiply_block(A, B, C, n, bsize)
    end_time = time.time()
    
    return C, (end_time - start_time)


# Input matrix size and blocking size
# Examples to observe significant changes in the diagram
matrix_sizes = [50, 97, 100, 150, 300 ,500] 
block_sizes =  [1, 2, 3, 8, 16, 25, 50, 80 ,97, 99, 100, 125, 150, 175, 300, 325, 500, 550] # Example block sizes
#for a smooth result use block_sizes = [1,2,3,8,16,25,50,97] 

plt.figure(figsize=(12,8))

for n in matrix_sizes:
    print("Matrix Size : " , n)
    execution_times = []
    for bsize in block_sizes:
        result, execution_time = matrix_multiplication(n, bsize)
        print(f"Execution TIme : {execution_time:.6f} seconds" ) 

        execution_times.append(execution_time)
    plt.plot(block_sizes, execution_times, marker='o', label=f"Matrix Size: {n}")

plt.title("Relationship between Blocking Size and Execution Time for Matrix Multiplication")
plt.xlabel("Blocking Size")
plt.ylabel(" Execution Time (seconds)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


"""
No blocking (blocking size equal to 1) may lead to the most straightforward implementation of matrix multiplication, 
but it may not exploit potential performance improvements from blocking.
Large Matrix Size with Small Blocking Size:
Matrix Size: 500x500
Blocking Size: 2
This will likely result in a longer execution time due to the large matrix size and small blocking size. 
The small blocking size may not effectively utilize cache and may lead to frequent cache misses.
Small Matrix Size with Large Blocking Size:
Matrix Size: 100x100
Blocking Size: 50
This combination might show faster execution times compared to smaller blocking sizes.
 Larger blocking sizes can exploit spatial locality better for smaller matrices, leading to faster execution times.
Prime Matrix Size with Prime Blocking Size:
Matrix Size: 97x97 (prime number)
Blocking Size: 97 (prime number)
Prime numbers for both matrix size and blocking size can result in inefficient cache utilization, 
leading to longer execution times due to potentially increased cache conflicts.
Equal Matrix Size and Blocking Size:
Matrix Size: 50x50
Blocking Size: 50
When the blocking size is equal to the matrix size, there might be minimal benefit from blocking, 
and the execution time may not significantly improve compared to unblocked matrix multiplication.
Matrix Size Not a Multiple of Blocking Size:
Matrix Size: 100x100
Blocking Size: 3
Choosing a blocking size that does not evenly divide the matrix size can lead to extra computations for the partial blocks at the end of each dimension, 
potentially impacting performance.
Matrix Size: 50x50
Blocking Size: 97
having a block size significantly larger than the matrix size could lead to efficient utilization of cache space and improved cache performance, 
especially if there is good spatial locality in the memory access pattern. However, it's important to consider the trade-offs,
such as potential wasted space and the impact on cache management algorithm
"It's important to note that an appropriate blocking size can indeed improve performance, and as the blocking size increases,
 it can further enhance performance by minimizing cache conflicts and improving cache utilization. However,
 using prime numbers for both matrix size and blocking size can introduce additional challenges in cache management, 
potentially leading to longer execution times."""