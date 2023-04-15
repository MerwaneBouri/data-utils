import gzip
import json 
from pathlib import Path
import scipy.spatial
from typing import Collection
import numpy as np 


if __name__ == "__main__":
	x, y = json.load(gzip.open(Path(__file__).parent / "assets" / 
"data.gz", "rt"))
