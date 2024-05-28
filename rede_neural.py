import numpy as np

# X = (horas de estudio, horas de descanso),
X = np.array(([2, 7], [1, 5], [3, 8]), dtype=float)
y = np.array(([90], [80], [99]), dtype=float)
#datos que se quieren predecir
xPredicted = np.array(([4,8]), dtype=float)

X = X/np.amax(X, axis=0)
xPredicted = xPredicted/np.amax(xPredicted, axis=0)
y = y/100

class Neural_Network(object):
  def __init__(self):
  #parameters
    self.inputSize = 2
    self.outputSize = 1
    self.hiddenSize = 3

  #weights
    self.W1 = np.random.randn(self.inputSize, self.hiddenSize) # (3x2) weight matrix from input to hidden layer
    self.W2 = np.random.randn(self.hiddenSize, self.outputSize) # (3x1) weight matrix from hidden to output layer

  def forward(self, X):
    #forward propagation through our network
    self.z = np.dot(X, self.W1) # dot product of X (input) and first set of 3x2 weights
    self.z2 = self.sigmoid(self.z) # activation function
    self.z3 = np.dot(self.z2, self.W2) # dot product of hidden layer (z2) and second set of 3x1 weights
    o = self.sigmoid(self.z3) # final activation function
    return o

  def sigmoid(self, s):
    # activation function
    return 1/(1+np.exp(-s))

  def sigmoidPrime(self, s):
    #derivative of sigmoid
    return s * (1 - s)

  def backward(self, X, y, o):
    # backward propagate through the network
    self.o_error = y - o # error in output
    self.o_delta = self.o_error*self.sigmoidPrime(o) # applying derivative of sigmoid to error

    self.z2_error = self.o_delta.dot(self.W2.T) # z2 error: how much our hidden layer weights contributed to output error
    self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) # applying derivative of sigmoid to z2 error

    self.W1 += X.T.dot(self.z2_delta) # adjusting first set (input --> hidden) weights
    self.W2 += self.z2.T.dot(self.o_delta) # adjusting second set (hidden --> output) weights

  def train(self, X, y):
    o = self.forward(X)
    self.backward(X, y, o)

  def saveWeights(self):
    np.savetxt("w1.txt", self.W1, fmt="%s")
    np.savetxt("w2.txt", self.W2, fmt="%s")

  def predict(self):
    print ("Prediccion: ")
    print ("Input (scaled): \n" + str(xPredicted))
    print ("Dato de salida: \n" + str(self.forward(xPredicted)))

NN = Neural_Network()
for i in range(1000): # trains the NN 1,000 times
  print ("# " + str(i) + "\n")
  print ("Datos de entrada: \n" + str(X))
  print ("Datos de salida: \n" + str(y))
  print ("Predicciones: \n" + str(NN.forward(X)))
  print ("Error: \n" + str(np.mean(np.square(y - NN.forward(X)))))
  print ("\n")
  NN.train(X, y)

NN.saveWeights()
NN.predict()