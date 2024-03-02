# -*- coding: utf-8 -*-
import unittest

from gilded_rose import *


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [NormalItem(vest, 1, 2), NormalItem(vest, 9, 19), NormalItem(vest, 4, 6), ]
        gr = GildedRose(items)

        gr.update_quality()
        assert(gr.get_items_by_name(vest) == [NormalItem(vest, 0, 1), NormalItem(vest, 8, 18), NormalItem(vest, 3, 5)])

    def test_vest_item_should_decrease_after_two_days(self):
        vest = "+5 Dexterity Vest"
        vest2 = "+6 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6), Item(vest2, 3, 5)]
        gr = GildedRose(items)

        gr.update_quality()
        gr.update_quality()
        assert(gr.get_items_by_name(vest2) == [Item(vest2, 1, 3)])
        assert(gr.get_items_by_name(vest) == [Item(vest, -1, 0), Item(vest, 7, 17), Item(vest, 2, 4)])

    def test_aged_brie_should_decrease_after_a_day(self):
        agedbrie = "Aged Brie"
        items = [Item(agedbrie, 1, 52)]
        gr = GildedRose(items)
        gr.update_quality()
        assert(gr.get_items_by_name(agedbrie) == [NormalItem(agedbrie,0, 52)])
        #gr.update_quality()
        #assert(gr.get_items_by_name(agedbrie) == [Item(agedbrie, -1, 5)])

    def test_sulfurus_after_a_day(self):
        backStage = "Sulfuras, Hand of Ragnaros"
        items = [Item(backStage, 1, 74)]
        gr = GildedRose(items)
        gr.update_quality()
        assert(gr.get_items_by_name(backStage) == [Item(backStage, 1, 74)])
        #gr.update_quality()
        #assert(gr.get_items_by_name(agedbrie) == [Item(agedbrie, -1, 5)])

    def test_item(self):
        nitem = NormalItem("normalitem", 4, 3)
        nitemTwo = NormalItem("normalitem", 4, 3)
        assert(nitem == nitemTwo)

if __name__ == '__main__':
    unittest.main()
