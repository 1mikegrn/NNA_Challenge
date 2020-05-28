import numpy as np
import pandas as pd

class BruteForce():
    """Brute Force approach to solve NNA_challenge problem."""
    def __init__(self, points):
        self.labels = [x[0] for x in points]
        self.data = np.array([x[1] for x in points])

    def query_radius(self, radius, method):
        """Uses NumPy broadcasing to run calculation at a lower level for faster 
        run times if method='np' (by default). Pure Python option is available 
        if method='py'.
        """
        if method == 'np':
            self.square_distance = pd.DataFrame(
                columns=self.labels, 
                index=self.labels,
                data=np.sum(
                    (self.data[np.newaxis,:,:] - self.data[:,np.newaxis,:])**2,
                    axis=-1
                ) 
            )
                
            res = dict()
            for i in self.labels:
                series = self.square_distance[i]
                res[i] = list(series[(series <= radius**2) & (series > 0)].index)
            return res

        # Really only used to demonstrate effectiveness of KDTree.
        elif method == 'py':
            res = dict()
            for i, r in enumerate(self.data):
                for j, c in enumerate(self.data):
                    d = sq_dist(r, c)
                    if (d <= radius**2) and (d > 0):
                        try:
                            res[self.labels[i]].append(self.labels[j])
                        except:
                            res[self.labels[i]] = []
                            res[self.labels[i]].append(self.labels[j])

            return res
        
def sq_dist(p0, p1):
    return sum([(x[0]-x[1])**2 for x in zip(p0, p1)])

# test on random data
if __name__ == "__main__":
    x = np.random.random_sample(size=(5,3))
    x = [('#'+str(i), a) for i, a in enumerate(x)]
    BruteForce(x).query_radius(0.25, method='np')