from PAC3.src.NaiveBayes import naiveBayes;

# Load file
l = list(map(lambda l: (l.strip()).split(','),
            open('../data/Wholesale customers.csv', 'r').readlines()))

for row in l:
    row[1] = 'Channel:' + row[0] + ' ' + 'Region: ' + row[1]

l = [row[1:] for row in l ]

# Naive bayes accuracy
naiveBayesAccuracy, predictions = naiveBayes(l, ratioTests=5)

# Print accuracy and predictions
print('naiveBayesAccuracy. :', naiveBayesAccuracy , '%')
