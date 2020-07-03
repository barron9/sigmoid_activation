# multivariate mlp example
from numpy import array
from numpy import hstack
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(100, activation='sigmoid', input_dim=3)) #dim 3x2
model.add(Dense(3))
model.compile(optimizer='adam', loss='mse')
# fit model,
X=array([[10,12,14],
                [11,14,15],
                [15,20,30]])
print(X)
y=array([[1,2,0],
[1,2,4],
[1,2,5]
])
print(y)
model.fit(X, y, epochs=1010, verbose=0)

yhat = model.predict(array([[12,13,15]]), verbose=0)
print(yhat)
