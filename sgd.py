# -*- coding: utf-8 -*-
"""
Created on Fri May 23 15:07:19 2025

@author: Abhi
"""
import numpy as np

def sgd(X, y, learning_rate=0.1, epochs=1000, batch_size=1):
    m = len(X)  
    theta = np.random.randn(2, 1) 
    
    # Add a bias term to X (X_0 = 1)
    X_bias = np.c_[np.ones((m, 1)), X]

    cost_history = []  

    for epoch in range(epochs):
        # Shuffle the data at the beginning of each epoch
        indices = np.random.permutation(m)
        X_shuffled = X_bias[indices]
        y_shuffled = y[indices]

        for i in range(0, m, batch_size):
            # Select a mini-batch or a single sample
            X_batch = X_shuffled[i:i+batch_size]
            y_batch = y_shuffled[i:i+batch_size]

            # Compute the gradient
            gradients = 2 / batch_size * X_batch.T.dot(X_batch.dot(theta) - y_batch)

            # Update the parameters (theta)
            theta -= learning_rate * gradients

        # Calculate and record the cost (Mean Squared Error)
        predictions = X_bias.dot(theta)
        cost = np.mean((predictions - y) ** 2)
        cost_history.append(cost)

        # Print progress every 100 epochs
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Cost: {cost}")

    return theta, cost_history

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)  
y = 4 + 3 * X + np.random.randn(100, 1)

# Train the model using SGD
theta_final, cost_history = sgd(X, y, learning_rate=0.1, epochs=1000, batch_size=1)