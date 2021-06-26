from locatieserver.schema.utils import Point, point_matcher


def test_point_regex():

    x = point_matcher.findall("POINT(5.10696041 52.06415055)")

    assert len(x[0]) == 2


def test_point():
    centroide_ll = Point("POINT(5.10696041 52.06415055)")

    assert centroide_ll.x == "5.10696041"
    assert centroide_ll.y == "52.06415055"
