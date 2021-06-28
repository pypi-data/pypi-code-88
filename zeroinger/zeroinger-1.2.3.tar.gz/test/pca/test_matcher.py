from unittest import TestCase
from zeroinger.pca import PcaMatcher


class TestPcaMatcher(TestCase):
    def test_adcode2area(self):
        matcher = PcaMatcher()

        area = matcher.adcode2area('659009')
        print(area)
        assert str(area) == '新疆维吾尔自治区__昆玉市'
        area = matcher.adcode2area('6590061')
        print(area)
        assert area is None

    def test_list_street_village_by_name(self):
        matcher = PcaMatcher()
        area_with_village_list = matcher.list_street_village_by_name('浙江省杭州市西湖区')
        print(area_with_village_list)
        assert len(area_with_village_list) == 1

        area_with_village_list = matcher.list_street_village_by_name('碑林区')
        print(area_with_village_list)
        assert len(area_with_village_list) == 1

        area_with_village_list = matcher.list_street_village_by_name('杭州市')
        print(area_with_village_list)
        assert len(area_with_village_list) > 1

        area_with_village_list = matcher.list_street_village_by_name('西湖区')
        print(area_with_village_list)
        assert len(area_with_village_list) > 1

    def test_list_street_village_by_code(self):
        matcher = PcaMatcher()
        area_with_village_list = matcher.list_street_village_by_adcode('130435')
        print(area_with_village_list)
        assert len(area_with_village_list) == 1

        area_with_village_list = matcher.list_street_village_by_adcode('130400')
        print(area_with_village_list)
        assert len(area_with_village_list) > 1

