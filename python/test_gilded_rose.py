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

    def test_aged_brie_before_sell_date(self):
        """Aged Brie increases in quality before sell date"""
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_aged_brie_on_sell_date(self):
        """Aged Brie increases in quality by 2 on sell date"""
        items = [Item("Aged Brie", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_aged_brie_after_sell_date(self):
        """Aged Brie increases in quality by 2 after sell date"""
        items = [Item("Aged Brie", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_aged_brie_maximum_quality(self):
        """Aged Brie quality should not exceed 50"""
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_aged_brie_near_maximum_quality(self):
        """Aged Brie quality should cap at 50"""
        items = [Item("Aged Brie", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_never_changes(self):
        """Sulfuras never changes in quality or sell_in"""
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_backstage_pass_long_before_sell_date(self):
        """Backstage passes increase by 1 when > 10 days"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_backstage_pass_medium_before_sell_date(self):
        """Backstage passes increase by 2 when <= 10 days"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_backstage_pass_close_to_sell_date(self):
        """Backstage passes increase by 3 when <= 5 days"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(13, items[0].quality)

    def test_backstage_pass_on_sell_date(self):
        """Backstage passes quality drops to 0 after concert"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_backstage_pass_after_sell_date(self):
        """Backstage passes quality stays at 0 after concert"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_backstage_pass_maximum_quality(self):
        """Backstage passes quality should not exceed 50"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_conjured_item_before_sell_date(self):
        """Conjured items degrade twice as fast before sell date"""
        items = [Item("Conjured Mana Cake", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_conjured_item_on_sell_date(self):
        """Conjured items degrade four times as fast on sell date"""
        items = [Item("Conjured Mana Cake", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

    def test_conjured_item_after_sell_date(self):
        """Conjured items degrade four times as fast after sell date"""
        items = [Item("Conjured Mana Cake", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

    def test_conjured_item_minimum_quality(self):
        """Conjured items quality never goes below 0"""
        items = [Item("Conjured Mana Cake", 5, 1)]
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
