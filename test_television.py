import unittest
from television import Television


class MyTestCase(unittest.TestCase):

    def test_init(self):
        tv = Television()
        self.assertFalse(tv._Television__status)
        self.assertFalse(tv._Television__muted)
        self.assertEqual(tv._Television__volume, Television.MIN_VOLUME)
        self.assertEqual(tv._Television__channel, Television.MIN_CHANNEL)


    def test_power(self):
        tv = Television()
        self.assertFalse(tv._Television__status)
        tv.power()
        self.assertTrue(tv._Television__status)
        tv.power()
        self.assertFalse(tv._Television__status)


    def test_mute(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()
        self.assertEqual(tv._Television__volume, 2)
        tv.mute()
        self.assertTrue(tv._Television__muted)
        self.assertEqual(tv._Television__volume, 0)
        tv.mute()
        self.assertFalse(tv._Television__muted)
        self.assertEqual(tv._Television__volume, 2)


    def test_channel_up(self):
        tv = Television()
        tv.power()
        self.assertEqual(tv._Television__channel, Television.MIN_CHANNEL)
        tv.channel_up()
        self.assertEqual(tv._Television__channel, Television.MIN_CHANNEL + 1)
        tv.channel_up()
        self.assertEqual(tv._Television__channel, Television.MIN_CHANNEL + 2)
        tv.channel_up()
        self.assertEqual(tv._Television__channel, Television.MIN_CHANNEL + 3)
        tv.channel_up()
        self.assertEqual(tv._Television__channel, Television.MIN_CHANNEL)


    def test_channel_down(self):
        tv = Television()
        tv.power()
        tv.channel_down()
        self.assertEqual(tv._Television__channel, Television.MAX_CHANNEL)
        tv.channel_down()
        self.assertEqual(tv._Television__channel, Television.MAX_CHANNEL - 1)
        tv.channel_down()
        self.assertEqual(tv._Television__channel, Television.MAX_CHANNEL - 2)
        tv.channel_down()
        self.assertEqual(tv._Television__channel, Television.MAX_CHANNEL - 3)
        tv.channel_down()
        self.assertEqual(tv._Television__channel, Television.MAX_CHANNEL)


    def test_volume_up(self):
        tv = Television()
        tv.power()
        tv.mute()
        tv.volume_up()
        self.assertFalse(tv._Television__muted)
        self.assertEqual(tv._Television__volume, 1)
        tv.volume_up()
        self.assertEqual(tv._Television__volume, 2)
        tv.volume_up()
        self.assertEqual(tv._Television__volume, 2)


    def test_volume_down(self):
        tv = Television()
        tv.power()
        tv.mute()
        tv.volume_up()
        tv.volume_up()
        self.assertFalse(tv._Television__muted)
        self.assertEqual(tv._Television__volume, 2)
        tv.volume_down()
        self.assertEqual(tv._Television__volume, 1)
        tv.volume_down()
        self.assertEqual(tv._Television__volume, 0)
        tv.volume_down()
        self.assertEqual(tv._Television__volume, 0)


if __name__ == '__main__':
    unittest.main()
