import gzip
import json 
from pathlib import Path
from typing import Collection
import math

import numpy as np
import scipy.spatial

def diametre_not_fast(x: Collection[float], y: Collection[float]) -> float:
	diam = 0.0
	for i, (x1, y1) in enumerate(zip(x, y, strict=True)):
		for x2, y2 in zip(x[i+1 :], y[i+1 :]):
			dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
			if dist > diam:
				diam = dist
	return diam

def diametre_fast(x: Collection[float], y: Collection[float]) -> float:
	X = np.array(x)
	Y = np.array(y)

	return np.sqrt(
		np.max(
			(X.reshape(-1, 1) - X.reshape(1, -1)) ** 2
			+ (Y.reshape(-1, 1) - (Y.reshape(1, -1))) ** 2
		)
	)


if __name__ == "__main__":
	x, y = json.load(gzip.open(Path(__file__).parent / "assets" / "data.gz", "rt"))
	print(diametre_not_fast(x,y))
	#print(diametre_fast(x,y))