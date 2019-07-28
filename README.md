# Movie Recommendation using PySpark

This project is used to monitor the Web log data which is processed by Apache Spark Streaming. The Spark Streaming program would read the logs and searches for 404 as status. If status 404 is found, it would display them on the screen with the details.

Language used   : Python 3.7

Framework       : Apache Spark 2.3

Libraries needed : Pyspark, sys

# Program setup

## getData.sh

## trainSaveModel.py

## predict.py


# Running the project locally

  - Clone the repository
    ```sh
    git clone https://github.com/ksashok/Spark-Web-Log-Analysis.git
    ```
  - Go to the project folder and download the datasets needed. 
    ```sh
    .\getData.sh
    ```
  - Train the model using the datasets
    ```sh
    spark-submit trainSaveModel.py
    ```
  - Predict 
    ```sh
    spark-submit predict.py 5
    ```


# Sample Output

```
"Philadelphia Story
"Seventh Seal
"Spring
Yojimbo (1961)
Clerks II (2006)
Six Degrees of Separation (1993)
Freeway (1996)
Laura (1944)
City Lights (1931)
"Walk in the Clouds
Idiocracy (2006)
"Insider
"5
"Passion of the Christ
Ip Man (2008)
```
