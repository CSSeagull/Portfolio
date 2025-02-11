import numpy as np

N = int(input("Enter an integer N: ")) # Recieve the value of N

if N < 3: #N should be greater than 3
    print("N must be 3 or greater to extract an inner array.")
else:
    array = np.random.randint(0, 100, (N, N)) # N x N 2D array generation
    print("random array:")
    print(array)

    inner_array = array[1:-1, 1:-1] #N-1 x N-1 slicing 
    print("\ninner array:")
    print(inner_array)