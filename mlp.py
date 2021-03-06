import numpy as np

def nonlin(x,deriv=False):
	if(deriv==True):
	    return x*(1-x)

	return 1/(1+np.exp(-x))

X = np.array([[0,0,1,1],
            [0,1,1,1],
            [1,0,1,1],
            [1,1,1,1]])

y = np.array([[0],
			[1],
			[1],
			[0]])

np.random.seed(1)

# randomly initialize our weights with mean 0
syn0 = 2*np.random.random((4,10)) - 1
syn1 = 2*np.random.random((10,4)) - 1
syn2 = 2*np.random.random((4,2)) - 1
syn3 = 2*np.random.random((2,1)) - 1




def fwd(l0,l1,l2,l3,l4,syn0,syn1,syn2,syn3):

    l1 = nonlin(np.dot(l0,syn0))

    l2 = nonlin(np.dot(l1,syn1))

    l3 = nonlin(np.dot(l2,syn2))

    l4 = nonlin(np.dot(l3,syn3))
    print(l4)

for j in range(10000):

	# Feed forward through layers 0, 1, and 2
    l0 = X

    l1 = nonlin(np.dot(l0,syn0))

    l2 = nonlin(np.dot(l1,syn1))

    l3 = nonlin(np.dot(l2,syn2))

    l4 = nonlin(np.dot(l3,syn3))

    l4_error = y - l4
    l4_delta = l4_error*nonlin(l4,deriv=True)

    l3_error = l4_delta.dot(syn3.T)
    l3_delta = l3_error * nonlin(l3,deriv=True)

    l2_error = l3_delta.dot(syn2.T) #y - l2
    l2_delta = l2_error*nonlin(l2,deriv=True)

    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * nonlin(l1,deriv=True)

    if (j% 1000) == 0:
	    print ("Error:" + str(np.mean(np.abs(l4_error))))
    syn3 += l3.T.dot(l4_delta)
    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)
    #print(syn1)
    #print(syn0)
fwd(np.array([[0,0,1,1]]),l1,l2,l3,l4,syn0,syn1,syn2,syn3)
