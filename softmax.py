import numpy as np


class Softmax (object):
    """" Softmax classifier """

    def __init__ (self, inputDim, outputDim):
        self.W = None
        #########################################################################
        # TODO: 5 points                                                        #
        # - Generate a random softmax weight matrix to use to compute loss.     #
        #   with standard normal distribution and Standard deviation = 0.01.    #
        #########################################################################
        sigma =0.01
        self.W = sigma * np.random.randn(inputDim,outputDim)
        pass
        #########################################################################
        #                       END OF YOUR CODE                                #
        #########################################################################

    def calLoss (self, x, y, reg):
        """
        Softmax loss function
        D: Input dimension.
        C: Number of Classes.
        N: Number of example.

        Inputs:
        - x: A numpy array of shape (batchSize, D).
        - y: A numpy array of shape (N,) where value < C.
        - reg: (float) regularization strength.

        Returns a tuple of:
        - loss as single float.
        - gradient with respect to weights self.W (dW) with the same shape of self.W.
        """
        loss = 0.0
        dW = np.zeros_like(self.W)
        #############################################################################
        # TODO: 20 points                                                           #
        # - Compute the softmax loss and store to loss variable.                    #
        # - Compute gradient and store to dW variable.                              #
        # - Use L2 regularization                                                  #
        # Bonus:                                                                    #
        # - +2 points if done without loop                                          #
        #############################################################################
        #Calculating loss for softmax
        #calculate the score matrix
        N = x.shape[0]
        s =x.dot(self.W)
        # calculating s-max(s)
        s_ = s-np.max(s, axis=1, keepdims= True)
        exp_s_ = np.exp(s_)
        # calculating base
        sum_f = np.sum(exp_s_, axis=1, keepdims=True)
        # calculating probability of incorrect label by dividing by base
        p_yi = exp_s_[np.arange(N),y]/sum_f
        # Calculating loss by applying log over the probability
        loss_i = - np.log(p_yi)
        #keep as column vector
        loss = np.sum(loss_i)/N
        ds = (exp_s_ >0).astype(int)
        ds[np.arange(x.shape[0]),y] += -1
        dW = (1/x.shape[0]) * (x.T).dot(ds)
        dW = dW + (2* reg* self.W)
        pass
        #############################################################################
        #                          END OF YOUR CODE                                 #
        #############################################################################

        return loss, dW

    def train (self, x, y, lr=1e-3, reg=1e-5, iter=100, batchSize=200, verbose=False):
        """
        Train this Softmax classifier using stochastic gradient descent.
        D: Input dimension.
        C: Number of Classes.
        N: Number of example.

        Inputs:
        - x: training data of shape (N, D)
        - y: output data of shape (N, ) where value < C
        - lr: (float) learning rate for optimization.
        - reg: (float) regularization strength.
        - iter: (integer) total number of iterations.
        - batchSize: (integer) number of example in each batch running.
        - verbose: (boolean) Print log of loss and training accuracy.

        Outputs:
        A list containing the value of the loss function at each training iteration.
        """

        # Run stochastic gradient descent to optimize W.
        lossHistory = []
        for i in range(iter):
            xBatch = None
            yBatch = None
            #########################################################################
            # TODO: 10 points                                                       #
            # - Sample batchSize from training data and save to xBatch and yBatch   #
            # - After sampling xBatch should have shape (D, batchSize)              #
            #                  yBatch (batchSize, )                                 #
            # - Use that sample for gradient decent optimization.                   #
            # - Update the weights using the gradient and the learning rate.        #
            #                                                                       #
            # Hint:                                                                 #
            # - Use np.random.choice                                                #
            #########################################################################
            xBatch = x[np.random.choice(x.shape[0], batchSize)]
            yBatch = y[np.random.choice(y.shape[0], batchSize)]
            loss, dW = self.calLoss(xBatch,yBatch,reg)
            self.W= self.W - lr * dW
            lossHistory.append(loss)



            pass
            #########################################################################
            #                       END OF YOUR CODE                                #
            #########################################################################
            # Print loss for every 100 iterations
            if verbose and i % 100 == 0 and len(lossHistory) is not 0:
                print ('Loop {0} loss {1}'.format(i, lossHistory[i]))

        return lossHistory

    def predict (self, x,):
        """
        Predict the y output.

        Inputs:
        - x: training data of shape (N, D)

        Returns:
        - yPred: output data of shape (N, ) where value < C
        """
        yPred = np.zeros(x.shape[0])
        ###########################################################################
        # TODO: 5 points                                                          #
        # -  Store the predict output in yPred                                    #
        ###########################################################################
        s =x.dot(self.W)
        yPred = np.argmax(s, axis=1)
        pass
        ###########################################################################
        #                           END OF YOUR CODE                              #
        ###########################################################################
        return yPred


    def calAccuracy (self, x, y):
        acc = 0
        ###########################################################################
        # TODO: 5 points                                                          #
        # -  Calculate accuracy of the predict value and store to acc variable    #
        ###########################################################################
        yPred = self.predict(x)
        acc = np.mean(y == yPred)*100
        print(yPred[:40])
        print(y[:40])
        pass
        ###########################################################################
        #                           END OF YOUR CODE                              #
        ###########################################################################
        return acc
