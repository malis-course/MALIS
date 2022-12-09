# Lab 3: Support Vector Machines

 The aim of this lab is to practice with Support Vector Machines (SVM), and in particular with the PEGASOS (Primal Estimated sub-GrAdient SOlver for SVM) algorithm. PEGASOS is a fast stochastic sub-gradient descent algorithm for solving the primal optimization problem cast by an SVM. In the first part of this lab, you will be to implement PEGASOS. As it is based on a primal problem, it is only adapted to linear kernels; the authors of PEGASOS proposed a way to use other non-linear kernels, at the price of time efficiency. Therefore in the second part of the lab, instead of implementing that less efficient version of PEGASOS, you will work on a features mapping method that will allow you to separate non-linearly separable datasets using PEGASOS. You will test your implementations on four datasets.

### Learning goals

After this lab, you should be able to:

1. Have a clear understanding of support vector machines
2. Master the concept of feature transformations
3. Have a deep understanding of the Gaussian Kernel (RBF)
4. Be familiar with the PEGASOS implementations

Go to [notebook](./svm.ipynb).