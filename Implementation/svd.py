import numpy as np
import seaborn as sns

def find_eig(data):
    eigenValues, eigenVectors = np.linalg.eig(np.dot(data, data.T))
    idx = eigenValues.argsort()[::-1]
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:, idx]

    sns.set_theme()
    plot = sns.relplot(x=range(1, len(eigenValues) + 1), y=eigenValues, kind="line", height=8, aspect=1.25)

    plot.set(xlabel="Cardinal Number of Eigen value", ylabel="Eigen values")
    # plot.savefig('aisehi')
    return eigenValues, eigenVectors