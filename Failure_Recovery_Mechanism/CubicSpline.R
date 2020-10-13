#Interpolation - CUBIC SPLINE
#Per Hour - Outlier 1% DBSCAN (e=0.3-0.8) IF (c=0-0.04)
hour_data_O1 <- read.table("/media/Moon/Thesis/DataCollection/Failure_Recovery/Per_Hour/O1-Test_2.csv", header = TRUE, sep=',' , dec='.')
plot(hour_data_O1$timestamp,hour_data_O1$Test_2)
result_hour_O1 <-spline(hour_data_O1$Test_2, n = length(hour_data_O1$timestamp))
plot(hour_data_O1$timestamp,hour_data_O1$Test_2,type="l",col="red")
lines(result_hour_O1$x,result_hour_O1$y, col="blue", type='p')
hour_data_O1$recovery <- result_hour_O1$y
write.csv(hour_data_O1, file = "/media/Moon/Thesis/DataCollection/Failure_Recovery/Cubic_Spline/Per_Hour/out-Test_2-O1.csv", row.names = FALSE)
#Per Hour - Outlier 5% DBSCAN (e=0.3) IF SVM
hour_data_O5 <- read.table("/media/Moon/Thesis/DataCollection/Failure_Recovery/Per_Hour/O5-Test_2.csv", header = TRUE, sep=',' , dec='.')
plot(hour_data_O5$timestamp,hour_data_O5$Test_2)
result_hour_O5 <-spline(hour_data_O5$Test_2, n = length(hour_data_O5$timestamp))
plot(hour_data_O5$timestamp,hour_data_O5$Test_2,type="l",col="red")
lines(result_hour_O5$x,result_hour_O5$y,col="blue", type='p')
hour_data_O5$recovery <- result_hour_O5$y
write.csv(hour_data_O5, file = "/media/Moon/Thesis/DataCollection/Failure_Recovery/Cubic_Spline/Per_Hour/out-Test_2-O5.csv", row.names = FALSE)
#Per Hour - Outlier 10% DBSCAN (e=0.2) IF
hour_data_O10 <- read.table("/media/Moon/Thesis/DataCollection/Failure_Recovery/Per_Hour/O10-Test_2.csv", header = TRUE, sep=',' , dec='.')
plot(hour_data_O10$timestamp,hour_data_O10$Test_2)
result_hour_O10 <-spline(hour_data_O10$Test_2, n = length(hour_data_O10$timestamp))
plot(hour_data_O10$timestamp,hour_data_O10$Test_2,type="l",col="red")
lines(result_hour_O10$x,result_hour_O10$y,col="blue", type='p')
hour_data_O10$recovery <- result_hour_O10$y
write.csv(hour_data_O10, file = "/media/Moon/Thesis/DataCollection/Failure_Recovery/Cubic_Spline/Per_Hour/out-Test_2-O10.csv", row.names = FALSE)
#-----------------------------------------------------------------
#Per Day - Outlier 1% DBSCAN (e=0.2)
day_data_O1 <- read.table("/media/Moon/Thesis/DataCollection/Failure_Recovery/Per_Day/O1-Test_2.csv", header = TRUE, sep=',' , dec='.')
plot(day_data_O1$timestamp,day_data_O1$Test_2)
result_day_O1 <-spline(day_data_O1$Test_2, n = length(day_data_O1$timestamp))
plot(day_data_O1$timestamp,day_data_O1$Test_2,type="l",col="red")
lines(result_day_O1$x,result_day_O1$y,col="blue", type='p')
day_data_O1$recovery <- result_day_O1$y
write.csv(day_data_O1, file = "/media/Moon/Thesis/DataCollection/Failure_Recovery/Cubic_Spline/Per_Day/out-Test_2-O1.csv", row.names = FALSE)
#Per Day - Outlier 5% IF(0.07)
day_data_O5 <- read.table("/media/Moon/Thesis/DataCollection/Failure_Recovery/Per_Day/O5-Test_2.csv", header = TRUE, sep=',' , dec='.')
plot(day_data_O5$timestamp,day_data_O5$Test_2)
result_day_O5 <-spline(day_data_O5$Test_2, n = length(day_data_O5$timestamp))
plot(day_data_O5$timestamp,day_data_O5$Test_2,type="l",col="red")
lines(result_day_O5$x,result_day_O5$y,col="blue", type='p')
day_data_O5$recovery <- result_day_O5$y
write.csv(day_data_O5, file = "/media/Moon/Thesis/DataCollection/Failure_Recovery/Cubic_Spline/Per_Day/out-Test_2-O5.csv", row.names = FALSE)
#Per Day - Outlier 10% DBSCAN(e=0.2)
day_data_O10 <- read.table("/media/Moon/Thesis/DataCollection/Failure_Recovery/Per_Day/O10-Test_2.csv", header = TRUE, sep=',' , dec='.')
plot(day_data_O10$timestamp,day_data_O10$Test_2)
result_day_O10 <-spline(day_data_O10$Test_2, n = length(day_data_O10$timestamp))
plot(result_day_O10$x,day_data_O10$Test_2,type="l",col="red")
lines(result_day_O10$x,result_day_O10$y,col="blue", type='p')
day_data_O10$recovery <- result_day_O10$y
write.csv(day_data_O10, file = "/media/Moon/Thesis/DataCollection/Failure_Recovery/Cubic_Spline/Per_Day/out-Test_2-O10.csv", row.names = FALSE)

#----------------------------------------------------------------
#Per Month - Outlier 1% SVM(0.01)
month_data_O1 <- read.table("/media/Moon/Thesis/DataCollection/Failure_Recovery/Per_month/O1-Test_2.csv", header = TRUE, sep=',' , dec='.')
plot(month_data_O1$timestamp,month_data_O1$Test_2)
result_month_O1 <-spline(month_data_O1$Test_2, n = length(month_data_O1$timestamp))
plot(month_data_O1$timestamp,month_data_O1$Test_2,type="l",col="red")
lines(result_month_O1$x,result_month_O1$y,col="blue", type='p')
month_data_O1$recovery <- result_month_O1$y
write.csv(month_data_O1, file = "/media/Moon/Thesis/DataCollection/Failure_Recovery/Cubic_Spline/Per_Month/out-Test_2-O1.csv", row.names = FALSE)
#Per Month - Outlier 5% DBSCAN (e=0.01)
month_data_O5 <- read.table("/media/Moon/Thesis/DataCollection/Failure_Recovery/Per_month/O5-Test_2.csv", header = TRUE, sep=',' , dec='.')
plot(month_data_O5$timestamp,month_data_O5$Test_2)
result_month_O5 <-spline(month_data_O5$Test_2, n = length(month_data_O5$timestamp))
plot(month_data_O5$timestamp,month_data_O5$Test_2,type="l",col="red")
lines(result_month_O5$x,result_month_O5$y,col="blue", type='p')
month_data_O5$recovery <- result_month_O5$y
write.csv(month_data_O5, file = "/media/Moon/Thesis/DataCollection/Failure_Recovery/Cubic_Spline/Per_Month/out-Test_2-O5.csv", row.names = FALSE)
#Per Month - Outlier 10% IF (c=0.1)
month_data_O10 <- read.table("/media/Moon/Thesis/DataCollection/Failure_Recovery/Per_Month/O10-Test_2.csv", header = TRUE, sep=',' , dec='.')
plot(month_data_O10$timestamp,month_data_O10$Test_2)
result_month_O10<-spline(month_data_O10$Test_2, n = length(month_data_O10$timestamp))
plot(month_data_O10$timestamp,month_data_O10$Test_2,type="l",col="red")
lines(result_month_O10$x,result_month_O10$y,col="blue", type='p')
month_data_O10$recovery <- result_month_O10$y
write.csv(month_data_O10, file = "/media/Moon/Thesis/DataCollection/Failure_Recovery/Cubic_Spline/Per_Month/out-Test_2-O10.csv", row.names = FALSE)
