from pyproj import Transformer
transformer_4326_to_2154 = Transformer.from_crs(4326, 2154)


def project_4326_to_2154(*, lat: float, long: float) -> tuple[float, float]:
    return transformer_4326_to_2154.transform(lat, long)
