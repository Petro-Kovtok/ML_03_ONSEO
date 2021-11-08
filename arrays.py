import numpy as np

if __name__=="__main__":
    A = np.array([[1,3,4],[2,0,7]])
    B = np.array([[1,9,0],[6,5,2]])

    print(A @ B.T)