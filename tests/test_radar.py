# coding: utf-8

'''
    tests.test_radar
    ~~~~~~~~~~~~~~~~

    Tests radar.
'''

from datetime import datetime

from yufou import radar


def test_round_to_5_minutes():
    for minute in range(0, 5):
        d = datetime.utcnow().replace(minute=minute)
        assert 0 == radar.round_to_5_minutes(d).minute

    for minute in range(6, 10):
        d = datetime.utcnow().replace(minute=minute)
        assert 5 == radar.round_to_5_minutes(d).minute


def test_image():
    expected = ('http://image.nmc.cn/product'
                '/2015/201506/20150627/RDCP/medium'
                '/SEVP_AOC_RDCP_SLDAS_EBREF_AZ9010_'
                'L88_PI_20150627055500000.GIF')
    d = datetime(year=2015, month=6, day=27, hour=5, minute=55)
    assert expected == radar.image('AZ9010', at=d)


def test_radar_station_from_city():
    assert radar.radar_station_from_city(u'广州') is not None
    assert radar.radar_station_from_city('somewhere') is None


def test_radar_station_from_radar_no():
    assert radar.radar_station_from_radar_no('AZ9010') is not None
    assert radar.radar_station_from_radar_no('invalid-no') is None
