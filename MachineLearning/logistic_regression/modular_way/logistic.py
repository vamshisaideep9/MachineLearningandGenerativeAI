import numpy as np



class LogisticRegression:
    
    def __init__(self, lr=0.0001, n_iters = 1000):
        
        self.lr = lr
        self.n_iters = n_iters
        self.theta = None
        self.loss_history = []
        
        
    def _add_bias(self, x):
        
        ones = np.ones((x.shape[0],1))
        return np.hstack((ones, x))
    
    
    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    
    def _compute_loss(self, y, y_hat):
        epsilon = 1e-5 # prevent log(theta)
        y_hat = np.clip(y_hat, epsilon, 1-epsilon)
        loss = np.mean(y*np.log(y_hat) + (1-y)*np.log(1-y_hat))
        return loss
    
    
    def fit(self, x, y):
        x = self._add_bias(x)
        n_samples, n_features = x.shape
        
        self.theta = np.zeros(n_features)
        
        for _ in range(self.n_iters):
            z = x @ self.theta 
            y_hat = self._sigmoid(z)
            
            gradient = (1/n_samples)*(x.T @ (y_hat - y))
            self.theta -= self.lr * gradient
            
            loss = self._compute_loss(y, y_hat)
            self.loss_history.append(loss)
            
    
    def predict_proba(self, X):
        X = self._add_bias(X)
        z = X @ self.theta
        return self._sigmoid(z)
    
    
    
    def predict(self, X):
        probs = self.predict_proba(X)
        return (probs >= 0.5).astype(int)
        
        
    
    
    
    
    
    