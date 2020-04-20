#!/usr/bin/env python3
"""Stacked bar chart"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

width = 0.5

plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')

ind = np.arange(fruit.shape[1])
color_list = ['red', 'yellow', '#ff8000', '#ffe5b4']
fruit_list = ['apples', 'bananas', 'oranges', 'peaches']

for i in range(fruit.shape[0]):
  plt.bar(ind, fruit[i],
    bottom = np.sum(fruit[:i], axis = 0),
    color = color_list[i % len(color_list)],
    width=width, label=fruit_list[i])

plt.xticks(ind, ('Farrah', 'Fred', 'Felicia'))
plt.yticks(np.arange(0, 81, 10))
plt.legend()

plt.show()
