import csv
import numpy as np


class LinearRegression:

    def __init__(self, learning_rate : float = 0.001, epochs : int = 100):
        self.theta0 = 0.0
        self.theta1 = 0.0

        self.learning_rate = learning_rate
        self.epochs = epochs

        self.loss_history = []

    
    def predict(self, x):
        return self.theta0 + self.theta1*x

    
    def compute_loss(self, x, y): 
        y_pred = self.predict(x)
        n = len(y)
        loss = (1/n)* np.sum((y-y_pred)**2)
        return loss

    def _compute_gradients(self, x, y):
        n = len(y)

        y_pred = self.predict(x)
        errors = y_pred - y

        grad_theta0 = (2/n)*np.sum(errors)
        grad_theta1 = (2/n)*np.sum(errors*x)

        return grad_theta0, grad_theta1


    def _update_parameters(self, grad_theta0, grad_theta1):
        self.theta0 -= self.learning_rate * grad_theta0
        self.theta1 -= self.learning_rate * grad_theta1



    def fit(self, x, y):
        x = np.array(x)
        y = np.array(y)

        y = y.reshape(-1,1)
        x = x.reshape(-1,1)

        for epoch in range(self.epochs):
            grad_theta0, grad_theta1 = self._compute_gradients(x,y)
            self._update_parameters(grad_theta0, grad_theta1)
            loss = self.compute_loss(x,y)
            self.loss_history.append(loss)



