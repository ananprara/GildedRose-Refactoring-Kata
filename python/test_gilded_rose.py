# -*- coding: utf-8 -*-
"""
Tests for Gilded Rose inventory system
"""
import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    """Test suite for the Gilded Rose inventory system"""

    def test_regular_item_before_sell_date(self):
        """Regular items should degrade by 1 before sell date"""
        items = [Item("Regular Item", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(9, items[0].quality)

    def test_regular_item_on_sell_date(self):
        """Regular items should degrade by 2 on sell date"""
        items = [Item("Regular Item", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_regular_item_after_sell_date(self):
        """Regular items should degrade by 2 after sell date"""
        items = [Item("Regular Item", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_regular_item_zero_quality(self):
        """Item quality should never go negative"""
        items = [Item("Regular Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_item_names_dont_change(self):
        """Item names should never change"""
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)


if __name__ == '__main__':
    unittest.main()
