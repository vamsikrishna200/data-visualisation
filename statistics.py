import statistics
import numpy
from scipy.stats import skew
sample=[10,20,30,40,50,60,60]
sample2=[73,43,65,23,67,879,34,89,34]
print("Mean of the sample is",statistics.mean(sample))
print("Mean of the sample2 is",statistics.mean(sample2))
print("Median of the sample is",statistics.median(sample))
print("Median of the sample2 is",statistics.median(sample2))
print("Mode of the sample is",statistics.mode(sample))
print("Mode of the sample2 is",statistics.mode(sample2))
print("Standard deviation of the sample is",statistics.stdev(sample))
print("Standard deviation of the sample2 is",statistics.stdev(sample2))
print("variance of the sample is",statistics.variance(sample))print("variance of the sample2 is",statistics.variance(sample2))
print("Covariance of the sample is",numpy.cov(sample))
print("Covariance of the sample2 is",numpy.cov(sample2))
q3,q1=numpy.percentile(sample, [75 ,25])
iqr=q3-q1
print("The interquartile range of the sample is",iqr)
q3,q1=numpy.percentile(sample2, [75 ,25])
iqr=q3-q1
print("The interquartile range of the sample2 is",q3-q1)
print("The skewness of the sample2 is")
print(skew(sample2, axis=0, bias=True))
output:
Median of the sample is 40
Median of the sample2 is 65
Mode of the sample is 60
Mode of the sample2 is 34
Standard deviation of the sample is 19.518001458970662
Standard deviation of the sample2 is 276.0184675786105
variance of the sample is 380.95238095238096
variance of the sample2 is 76186.19444444445
Covariance of the sample is 380.95238095238096Covariance of the sample2 is 76186.19444444447
The interquartile range of the sample is 30.0
The interquartile range of the sample2 is 39.0
The skewness of the sample is
-0.22234764798058884
The skewness of the sample2 is
2.44558983254843
