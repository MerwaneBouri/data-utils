from shapely.geometry import shape, Polygon


def remove_orverlap(*, poly1: shape, poly2: shape) -> tuple[shape, shape]:
    intersection = poly1.intersection(poly2)
    return poly1, poly2.difference(intersection)


def remove_orverlap_many(*polys: shape) -> tuple[shape, ...]:
    out = list(polys)
    for i in range(len(polys)):
        poly1 = polys[i]
        for j in range(i + 1, len(polys)):
            poly2 = polys[j]
            res_poly1, res_poly2 = remove_orverlap(poly1, poly2)
            out[i] = res_poly1
            out[j] = res_poly2
    return tuple(out)
