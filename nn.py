import numpy as np
#from numpy.random import Generator, PCG64

class simpel():

    def __init__(self):
        #rg = Generator(PCG64())
        #rg.standard_normal()
        self.weights = (np.array([[0.01122252],[0.06420096],[0.40555929]]))
        input=np.array([[0,0,1],
                        [1,1,1],
                        [1,0,1],
                        [0,1,1]])
        #print(v)
        #print(v.T)
        print("start weights")
        print(self.weights)
        #print("adjustment for .2 error and np.array([[1,1,1]]) output with derivative fn")
        #print(np.array([[.1,1,.1,1]]).T * (1 - np.array([[.1,1,.1,1]]).T) )
        for k in range(1000):
            output = self.think(input)
            expected_outputs = (np.array([[1,1,0,1]]).T)
            derivatedoutputoversigmoid = self.d_activationfunc(output)
            error = expected_outputs - output

            print( " == error is == "+str(error.T))
            adjus = np.dot(input.T , ( error * derivatedoutputoversigmoid ))
            self.weights += adjus
        print("last weights")
        print(self.weights)
        print("cevap np.dot(([[1,0,1]]) için " + str(self.think(input)))


    def activationfunc(self, x):
        return (1 / (1 + np.exp(-x)))

    def d_activationfunc(self,x):
        return x * (1- x)

    def train(self,input,output,repeat):
        return 1

    def think(self,x):
        return self.activationfunc(np.dot(x, self.weights))

    def get_result_for(self,query):
        query=query.astype(float)
        output = activationfunc(np.dot(query,self.weights))
        return output


if __name__ == "__main__":
    simple = simpel()
    ##simple.activationfunc(simple.weights)
