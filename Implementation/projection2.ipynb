{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1fc8ca99-781f-4381-98c1-66beebd43393",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "def project_onto_signal_subspace_part2(data, eigenVectors, r):\n",
    "    U, sigma, V = np.linalg.svd(data)\n",
    "    V = V.T\n",
    "\n",
    "    X_elem = np.array([sigma[i] * np.outer(U[:, i], V[:, i]) for i in range(0, r)])\n",
    "    X_train_extracted = X_elem.sum(axis=0)\n",
    "    X_train_extracted_data = np.asarray(list(X_train_extracted[:, 0]) + list(X_train_extracted[:, -1]))\n",
    "\n",
    "    U = eigenVectors[:, :r]\n",
    "    UT = U.T\n",
    "    pX = np.matmul(UT, X_train_extracted)\n",
    "    centroid = (np.min(pX, axis=1) + np.max(pX, axis=1))/2\n",
    "    centroid = centroid[:, np.newaxis]\n",
    "\n",
    "    return centroid, pX, U, X_train_extracted_data"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
