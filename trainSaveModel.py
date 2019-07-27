from pyspark import SparkContext
from pyspark.mllib.recommendation import ALS

sc = SparkContext()


completeRDD = sc.textFile('datasets/ml-latest-small/ratings.csv')
header = completeRDD.first()

completeRDD = completeRDD.filter(lambda line : line != header)\
    .map(lambda line : line.split(","))\
    .map(lambda line : (line[0],line[1],line[2]))

trainingRDD, testRDD = completeRDD.randomSplit([0.7,0.3])


model = ALS.train(trainingRDD,rank=10,iterations=10)

model.save(sc, "target/model")
