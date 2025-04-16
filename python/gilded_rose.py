# -*- coding: utf-8 -*-
"""
Gilded Rose Inventory System
"""


class GildedRose:
    """
    The Gilded Rose inventory management system that handles
    the daily update of quality and sell-in values for items.
    """
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """Update the quality and sell_in values for all items in inventory."""
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                # Legendary items never change
                continue

            # Update sell_in for all non-legendary items
            item.sell_in -= 1

            if item.name == "Aged Brie":
                self._update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_pass(item)
            elif item.name.startswith("Conjured"):
                self._update_conjured_item(item)
            else:
                self._update_regular_item(item)

    def _update_aged_brie(self, item):
        """Update Aged Brie quality which increases over time."""
        self._increase_quality(item)
        
        # Quality increases twice as fast after sell date
        if item.sell_in < 0:
            self._increase_quality(item)

    def _update_backstage_pass(self, item):
        """Update Backstage pass quality which increases over time at variable rates."""
        self._increase_quality(item)
        
        # Quality increases more as the concert approaches
        if item.sell_in < 11:
            self._increase_quality(item)
        
        if item.sell_in < 6:
            self._increase_quality(item)
        
        # Quality drops to 0 after the concert
        if item.sell_in < 0:
            item.quality = 0

    def _update_regular_item(self, item):
        """Update regular item quality which decreases over time."""
        self._decrease_quality(item)
        
        # Quality degrades twice as fast after sell date
        if item.sell_in < 0:
            self._decrease_quality(item)
            
    def _update_conjured_item(self, item):
        """Update conjured item quality which decreases twice as fast as regular items."""
        # Conjured items degrade twice as fast
        self._decrease_quality(item)
        self._decrease_quality(item)
        
        # Quality degrades twice as fast after sell date (so 4x regular)
        if item.sell_in < 0:
            self._decrease_quality(item)
            self._decrease_quality(item)

    def _increase_quality(self, item):
        """Increase item quality by 1 without exceeding the maximum value."""
        if item.quality < 50:
            item.quality += 1

    def _decrease_quality(self, item):
        """Decrease item quality by 1 without going below zero."""
        if item.quality > 0:
            item.quality -= 1


class Item:
    """
    An item in the Gilded Rose inventory system.
    """
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
