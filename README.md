# Reliable_IoT-Agro
Here, we introduced an IoT-based SF application with particular attention to data cleansing by providing Fog-based data reliability using data analysis to recognize and correct failures in real and raw collected farming data. 

We evaluate our Failure Detection Mechanism (FDM) and Failure Recovery Mechanism (FRM) in a virtual machine running a Ubuntu 64-bit operative system and using Python version 2.7.17 and R version 3.6.3 for the Machine Learning (ML) and Interpolation algorithms, respectively. In Python, we deploy a ML library by using scikit-learn; in particular, DBSCAN from sklearn.cluster, IsolationForest from sklearn.ensemble, and OneClassSVM from sklearn.svm. In R, we deploy the following functions to interpolate: spline for Cubic Spline interpolation, approx for Linear interpolation, and loess.smooth for Nearest Neighbor interpolation.

We conduct evaluation experiments with three temperature datasets. For testing purposes, we included randomly 1%, 5%, and 10% of outliers in each of the three datasets above mentioned using the InterQuartile Range (IQR), generating in total nine datasets. Three datasets "Per_Hour" with 24 instances collected by Omicron device with 1%, 5%, and 10% of outliers, respectively. Three datasets "Per_Day" with 288 instances collected by Intel device with 1%, 5%, and 10% of outliers, respectively. Three datasets "Per_Month" with 22532 instances collected by Libelium device with 1%, 5%, and 10% of outliers, respectively. For privacy issues, we can not share the temperature datasets. But we shared the codes and results of each test.

We conducted experiments with different datasets to evaluate, in terms of Accuracy, Recall, Precision, FAR, and F-Score, several candidate algorithms for realizing FDM; this mechanism tags the detected outliers and generates the tagged outliers dataset that is the FRM’s input. We define the best performance condition for outliers detection algorithm: high Accuracy, high Precision, and low FAR. In particular,  we vary the parameters from each algorithm described in Section 3.3 as follows. For DBSCAN, the eps (e) parameter from 0.1 to 0.8 (with min_samples set in 3). For IF, the contamination (c) parameter from 0 to 0.5. For SVM, the nu parameter from 0.01 to 0.1. We evaluated the algorithms using the datasets above described aggregating to each of the 1%, 5%, and 10% of outliers. 

In the Failure_Detection_Mechanism file, you can find the codes and results per each dataset described before (Per_Hour, Per_Day, and Per_Month). Each file contains:
- Codes to run the DBSCAN, Isolation Forest (IF), and Support Vector Machine (SVM) algorithms (e.g., test_DBSCAN.py) 
- Codes to generate graphs per algorithm and the comparison between them (e.g., plot_DBSCAN.py and plot_comparison.py)
- The algorithm to generate the outliers (i.e., outlier_source_outside.py)
- The algorithm to extract the confusion matrix results from each test and calculated the metrics evaluated per ML algorithm (i.e., writer2csv.py)
- The results of each test per ML algorithm varying the specific parameters above mentioned.

We conducted experiments with the datasets outputted by FDM for evaluating, regarding RMSE, several interpolation techniques that allow replacing the outliers with ’accurate’ data.

The Failure_Recovery_Mechanism file contains:
- The R codes to run the interpolation techniques (e.g., CubicSpline.R)
- The python code to compute the RMSE (i.e., RMSE.py)
- The results from each RMSE computing per outlier percentage (e.g., RMSE-O1.csv)
