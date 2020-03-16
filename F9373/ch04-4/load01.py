import load_mnist as lm

dataset = lm.load_mnist()

print(dataset['x_train'][0], dataset['y_train'][0])
