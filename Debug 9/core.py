import pandas

# A program that I wrote to test multiple machine learning algorithms on two different datasets
# It is very broken throughout the code, in multiple places

def getUseableData(path):
    print("Getting data from the dataset")
    import pandas as pd

    zDataFrame = pd.DataFrame(path)
    for column in zDataFrame.columns:
        numNull = zDataFrame[column].isnull().sum()
        fiftenPercent = 0.15 * zDataFrame.shape[0]
        if numNull > fiftenPercent:
            zDataFrame = zDataFrame.drop(column, axis=1)
            continue
        try:
            try:
                zDataFrame[column].fillna(0)
            except Exception:
                zDataFrame[column] = zDataFrame[column].fillna(zDataFrame[column].mode())
        except Exception:
            print(f"Error with Column {str(column)}")
    return zDataFrame


def encodeData(zDataFrame):
    print("Cleaning the Data")
    import pandas as pd
    COLUMNS = zDataFrame.columns
    CATEGORICAL = [column for column in COLUMNS if zDataFrame[column].dtype == "O"]
    for column in CATEGORICAL:
        encoded = pd.get_dummies(zDataFrame[column], prefix='encoded')
        zDataFrame = zDataFrame.drop(column, axis=1)
        zDataFrame = zDataFrame.join(encoded)
    return zDataFrame


def featureSelection(zDataFrame:pandas.DataFrame, TARGET):
    print("Choosing the best features")
    import pandas as pd
    from sklearn.feature_selection import SelectKBest, chi2
    oldX = zDataFrame.drop(TARGET, axis=1)
    y = zDataFrame[TARGET]
    X = SelectKBest(chi2, k=25).fit_transform(oldX, y)
    X = pd.DataFrame(X)
    return X, y


def getModels():
    print('Getting ML algorithms')
    # Import the classification algorithms that will be tested
    from sklearn.linear_model import (
        RidgeClassifier,
        LogisticRegression,
        SGDClassifier,
        Perceptron,
        PassiveAggressiveClassifier,
    )
    from sklearn.discriminant_analysis import (
        LinearDiscriminantAnalysis,
        QuadraticDiscriminantAnalysis,
    )
    from sklearn.svm import LinearSVC, NuSVC, SVC
    from sklearn.gaussian_process import GaussianProcessClassifier
    from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier
    from sklearn.naive_bayes import (
        GaussianNB,
        MultinomialNB,
        ComplementNB,
        BernoulliNB,
        CategoricalNB,
    )
    from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
    from sklearn.ensemble import (
        AdaBoostClassifier,
        BaggingClassifier,
        ExtraTreesClassifier,
        GradientBoostingClassifier,
        RandomForestClassifier,
        StackingClassifier,
        VotingClassifier,
    )

    # TODO - Make not garbage
    # Commented out models need to be fixed, currently don't work / take ~30 seconds
    # All other models need to be optimized
    # Imports Required Models
    # ("SVM", SVC())
    MODELS = [("LR", LogisticRegression(solver="liblinear"))]
    MODELS.append(("SVM", SVC(max_iter=None)))
    MODELS.append(("LDA", LinearDiscriminantAnalysis()))
    MODELS.append(("KNN", KNeighborsClassifier()))
    MODELS.append(("CART", DecisionTreeClassifier()))
    MODELS.append(("NB", GaussianNB()))
    MODELS.append(("PAR", PassiveAggressiveClassifier()))
    MODELS.append(("RIDGE", RidgeClassifier()))
    MODELS.append(("SGDC", SGDClassifier()))
    MODELS.append(("PER", Perceptron()))
    # MODELS.append(('QDA', QuadraticDiscriminantAnalysis()))
    MODELS.append(("LinSVC", LinearSVC(dual=False)))
    MODELS.append(("NuSVC", NuSVC()))
    # MODELS.append(('GPC', GaussianProcessClassifier())) # Takes a long time
    # MODELS.append(('RNC', RadiusNeighborsClassifier()))
    MODELS.append(("MNB", MultinomialNB()))
    MODELS.append(("CompNB", ComplementNB()))
    MODELS.append(("BNB", BernoulliNB()))
    # MODELS.append(('CatNB', CategoricalNB()))
    MODELS.append(("ETC", ExtraTreeClassifier()))
    MODELS.append(("ADA", AdaBoostClassifier()))
    MODELS.append(("BAG", BaggingClassifier()))
    MODELS.append(("ETsC", ExtraTreesClassifier()))
    MODELS.append(("GBC", GradientBoostingClassifier()))
    MODELS.append(("RF", RandomForestClassifier()))
    return MODELS


def testModels(X, y, MODELS):
    print('Testing the algorithms')
    from sklearn.model_selection import cross_val_score
    from datetime import datetime

    RESULTS = {}

    def test_Model(name, model):
        SCORES = []
        start = datetime.now()
        for _ in range(10):
            crossValidated = cross_val_score(model, X, y, scoring="accuracy", cv=2)
            SCORES.append(crossValidated.mean())
        end = datetime.now() - start
        average = sum(SCORES)
        average /= 10
        RESULTS[name] = (average, end)

    # Test each classification model 10 times, timing how long it takes
    [test_Model(i, j) for i, j in MODELS]

    test_Results = {{name: [scoreTime[0] * 100, scoreTime[1].total_seconds()] for name, scoreTime in RESULTS.items()}}
    return test_Results


def testClassificationAlgorithms(pathToDF, targetOfDataSet, cli):
    X, y = featureSelection(encodeData(getUseableData(pathToDF)), targetOfDataSet)
    modelsUsed = getModels()

    # The line below allows for the file to be run as a CLI command
    results_Test_Classifications = testModels(X, y, modelsUsed)
    if cli:
        import json
        print(
            "Here are the test results for each algorithm tested:\n"
            + json.loads(results_Test_Classifications, indent=4)
        )

if __name__ == "__main__":
    testClassificationAlgorithms('Debug 9/titanic.csv', 'Survived', True)
    testClassificationAlgorithms('Debug 9/spaceTitanic.csv', 'Transported', True)
