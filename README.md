# Reliable_IoT-Agro
Here, we introduced an IoT-based SF application with particular attention to data cleansing 
by providing Fog-based data reliability using data analysis to recognize and correct failures 
in real and raw collected farming data. 

We evaluate our Failure Detection Mechanism (FDM) and Failure Recovery Mechanism (FRM) in a virtual machine running 
a Ubuntu 64-bit operative system and using Python version 2.7.17 and R version 3.6.3 for the ML and Interpolation algorithms, respectively.
In Python, we deploy aML library by using scikit-learn; in particular, DBSCAN from sklearn.cluster, IsolationForest from sklearn.ensemble, 
and OneClassSVM from sklearn.svm. In R, we deploy the following functions to interpolate: spline for Cubic Spline interpolation, 
approx for Linear interpolation, and loess.smooth for Nearest Neighbor interpolation.
