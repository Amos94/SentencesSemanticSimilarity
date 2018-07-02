import sklearn.cluster import KMeans


class Clustering():

    numOfClusters = 0
    randomState = 0

    def __init__(self, numOfClusters, randomState):
        self.numOfClusters = numOfClusters
        self.randomState = randomState

    def KMeans(self, X):
        kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

        kmeans.labels_
        kmeans.predict([[0, 0], [4, 4]])
        kmeans.cluster_centers_

        return kmeans

    def personalizedClusterintg(self):
        pass
