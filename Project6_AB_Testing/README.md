### Project 6: Analyse A/B Testing
<p align="center">
    <img width="600" height="300"
     src="https://images.ctfassets.net/zw48pl1isxmc/4QYN7VubAAgEAGs0EuWguw/165749ef2fa01c1c004b6a167fd27835/ab-testing.png">
</p>

Description:

This repository contains source code, implementing inferential
statistical methods for the analysis of A/B testing on data
provided by a company trying to figure out if a recent website
landing page change has lead to increased traffic of online paid
customers or not. 
    
The first part of the analysis uses conventional descriptive
statistics and bootstrapping techniques to find out
quantitative differences in the rate of conversion of unpaid
to paid customers when subjected to the different landing
pages. Subsequently, more methodical inferential and
hypothesis testing methods have been employed to show any
statistical significance of convertion rates over the
treatments. Finally, a logistic regression
model has been fit to the binary conversion target
variable and analysis was done to show if the landing
page predictor does infact affect the target
conversion rate variable.

Technology Used:

* Python 3

Libraries Used:

* numpy
* matplotlib
* seaborn
* statsmodels