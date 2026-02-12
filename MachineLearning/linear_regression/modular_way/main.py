import numpy as np
from linear_reg import LinearRegression


# Generate synthetic data
np.random.seed(42)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

# Initialize model
model = LinearRegression(learning_rate=0.1, epochs=200)

# Train
model.fit(x, y)

print("Learned theta0:", model.theta0)
print("Learned theta1:", model.theta1)


import matplotlib.pyplot as plt

plt.plot(model.loss_history)
plt.title("Loss vs Epochs")
plt.xlabel("Epoch")
plt.ylabel("MSE")
plt.show()


plt.scatter(x,y)
plt.plot(x, model.predict(x), color='red')
plt.title("Fitted Line")
plt.show()
