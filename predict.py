from pyspark.mllib.recommendation import MatrixFactorizationModel
from pyspark import SparkContext
import sys

sc = SparkContext()
sc.setLogLevel("ERROR")

def predict(userID):

    completeMovies = sc.textFile('datasets/ml-latest-small/movies.csv')
    header2 = completeMovies.first()
    completeMovies = completeMovies.filter(lambda line : line != header2)\
        .map(lambda line : line.split(","))
    

    model = MatrixFactorizationModel.load(sc, "target/model")

    completeRDD = sc.textFile('datasets/ml-latest-small/ratings.csv')
    header = completeRDD.first()

    completeRDD = completeRDD.filter(lambda line : line != header)\
    .map(lambda line : line.split(","))\
    .map(lambda line : (line[0],line[1],line[2]))

    userRatedMovies = completeRDD.filter(lambda line : line[0] == userID).map(lambda line : line[1]).collect()

    userUnrated = completeMovies.filter(lambda line : line[0] not in userRatedMovies).map(lambda line : (userID,line[0]))

    predict = model.predictAll(userUnrated).map(lambda line : [str(line[1]), line[2]]).sortBy(lambda line : line[1], ascending=False)

    movies = predict.join(completeMovies)

    output = movies.map(lambda line : line[1][1]).take(15)

    for i in output:
        print(i)


if __name__ == '__main__':
    userID = sys.argv[1]
    predict(userID)


