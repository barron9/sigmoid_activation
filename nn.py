import numpy as np
from numpy.random import Generator, PCG64

class simpel():

    def __init__(self):
        rg = Generator(PCG64())
        rg.standard_normal()
        #print(rg.standard_normal((3,1)))
        v=np.array([[0,0,1],
                    [1,1,1],
                    [1,0,1],
                    [0,1,1]])
        print(v)
        print(v.T)
        print("adjustment for .2 error and np.array([[1,1,1]]) output with derivative fn")

        print(np.dot(v.T , ( .02 * np.array([[.1,1,.1,1]]).T * (1 - np.array([[.1,1,.1,1]]).T) ) ))
        print("start weights")
        self.weights=rg.standard_normal((3,1))
        print(self.weights)

    def activationfunc(self,x):
        print("activation func")
        print(1 / (1 + np.exp(-x)))
        return 1 / (1 + np.exp(-x))

    def d_activationfunc(self,x):
        return 1

    def train(self,input,output,repeat):

        return 1

    def get_result_for(self,query):
        query=query.astype(float)
        output = activationfunc(np.dot(query,self.weights))
        return output


if __name__ == "__main__":
    simple = simpel()
    simple.activationfunc(simple.weights)
