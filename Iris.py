'''
############################################################################################################

Script that plots the properties of the different flowers in the famous Iris data set using matplotlib.

The dataset can be downloaded from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data, or can be imported using
data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

############################################################################################################
'''
from typing import Dict, List
import csv
from collections import defaultdict
from typing import NamedTuple
import requests
from matplotlib import pyplot as plt

Vector = List[float]

class LabeledPoint(NamedTuple):
    point: Vector
    label: str
    
def distance(v: Vector, w: Vector) -> float:
    """Computes the distance between v and w"""
    return math.sqrt(squared_distance(v, w))

def parse_iris_row(row: List[str]) -> LabeledPoint:
    """
    sepal_length, sepal_width, petal_length, petal_width, class
    """
    measurements = [float(value) for value in row[:-1]]
    # class is e.g. "Iris-virginica"; we just want "virginica"
    label = row[-1].split("-")[-1]
    return LabeledPoint(measurements, label)
    
with open('iris.data') as f:
    reader = csv.reader(f)
    iris_data = [parse_iris_row(row) for row in reader]
    
# We'll also group just the points by species/label so we can plot them
points_by_species: Dict[str, List[Vector]] = defaultdict(list)
for iris in iris_data:
    points_by_species[iris.label].append(iris.point)
    
    
metrics = ['sepal length', 'sepal width', 'petal length', 'petal width']
pairs = [(i, j) for i in range(4) for j in range(4) if i < j]
marks = ['+', '.', 'x'] # we have 3 classes, so 3 markers
fig, ax = plt.subplots(2, 3)

for row in range(2):
    for col in range(3):
        i, j = pairs[3 * row + col]
        
        ax[row][col].set_title(f"{metrics[i]} vs {metrics[j]}", fontsize=8)
        ax[row][col].set_xticks([])
        ax[row][col].set_yticks([])


        for mark, (species, points) in zip(marks, points_by_species.items()):
            xs = [point[i] for point in points]
            ys = [point[j] for point in points]
            ax[row][col].scatter(xs, ys, marker=mark, label=species)
    
    
ax[-1][-1].legend(loc='lower right', prop={'size': 6})
plt.show()
