# Reliable_IoT-Agro
We introduces an IoT-based SF application with particular attention to data cleansing by providing Fog-based data reliability using data analysis to recognize and correct failures in real and raw collected farming data.

Our proposal includes a conceptual Things-Fog-Cloud based architecture that incorporates mechanisms for detecting and treating outliers. 
The Failure Detection Mechanism (FDM) finds outliers in datasets by Machine Learning (ML) algorithms. 
The Failure Recovery Mechanism (FRM) replaces the identified outliers with data inferred by using interpolation techniques. 

Our approach is novel because there is no approach based on Machine Learning and Interpolation techniques, to the best of our knowledge, aimed to provide data reliability to Things-Fog-Cloud-based SF applications that support decision-making to farming stakeholders. We evaluate our approach by deploying the three Tiers-based architecture in a Colombian coffee smart farm. We run the FDM and FRM mechanisms at the Fog Tier over this real implementation to perform the data reliability testing. The datasets used in the case study contain real information about the coffee crop temperature in different time scales (hour, day, and month) and, further, information about the data collection sensor technologies (Intel, Omicron, and Libelium). Results show our mechanisms achieve high Accuracy, Precision, and Recall as well as low False Alarm Rate (FAR) and Root Mean Squared Error (RMSE) when detecting and replacing outliers with inferred data. Considering the obtained results, we conclude that our approach provides reliable data collection in Smart Farming to support correct decision-making. 

The main contributions of this work are: 
- An approach that introduces a Things-Fog-Cloud architecture that combines ML and Interpolation techniques to intelligently and automatically provide data reliability on SF applications. 
- An ML-based mechanism for outlier detection in IoT-based Smart Farming data collection. 
- An interpolation-based mechanism for replacing the outliers detected with inferred data.
- An extensive evaluation of the proposed approach by a case study involving real data collected in a network based on a Things-Fog-Cloud and deployed in a Colombian Smart Coffee Farm.


Check our web site: www.iot-agro.com

