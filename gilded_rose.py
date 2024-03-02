# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def __eq__(self, other):
        return self.name == other.name and self.sell_in == other.sell_in and self.quality == other.quality

    def check_negative_quality(self):
        if self.quality < 0:
            self.quality = 0

#using the strategy pattern. Referenced from lecture 3/1/2024
class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
        self.degrade = 1

    def update_quality(self):
        if (self.quality > 0):
            if (self.sell_in < 0):
                self.quality = self.quality - self.degrade*2
            else:
                self.quality = self.quality - self.degrade
        self.check_negative_quality()

    def update_sell_in(self):
        self.sell_in = self.sell_in - 1

class ConjuredItem(NormalItem):
    def update_quality(self):
        if (self.quality > 0):
            self.quality = self.quality - self.degrade*2

        self.check_negative_quality()

    def update_sell_in(self):
        self.sell_in = self.sell_in - 1

class AgedBrieItem(NormalItem):
    def update_quality(self):
        self.check_negative_quality()
        if (self.quality < 50):
            self.quality = self.quality + 1

    def update_sell_in(self):
        self.sell_in = self.sell_in - 1

class SulfurusItem(NormalItem):
    def update_quality(self):
        self.check_negative_quality()

    def update_sell_in(self):
        return

class BackStagePassItem(NormalItem):
    def update_quality(self):
        self.check_negative_quality()
        if self.quality < 50:
            self.quality = self.quality + 1
            if self.sell_in < 11:
                if self.quality < 50:
                    self.quality = self.quality + 1
            if self.sell_in < 6:
                if self.quality < 50:
                    self.quality = self.quality + 1
        if self.sell_in <= 0:
            self.quality = self.quality - self.quality
    def update_sell_in(self):
        self.sell_in = self.sell_in - 1


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def get_items_by_name(self, name):
        it = []
        for i in self.items:
            if i.name == name:
                it.append(NormalItem(i.name, i.sell_in, i.quality))
        return it

    def process_items(self, items):
        it = []
        for i in items:
            if i.name == "Aged Brie":
                it.append(AgedBrieItem(i.name, i.sell_in, i.quality))
            elif i.name == "Sulfuras, Hand of Ragnaros":
                it.append(SulfurusItem(i.name, i.sell_in, i.quality))
            elif i.name == "Conjured":
                it.append(ConjuredItem(i.name, i.sell_in, i.quality))
            elif i.name == "Backstage passes to a TAFKAL80ETC concert":
                it.append(BackStagePassItem(i.name, i.sell_in, i.quality))
            else:
                it.append(NormalItem(i.name, i.sell_in, i.quality))
        return it
    def update_quality(self):
        processed_items = self.process_items(self.items)
        self.items = []
        for processed_item in processed_items:
            processed_item.update_sell_in()
            processed_item.update_quality()
            self.items.append(processed_item)
#        for item in self.items:
#            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
#                if item.quality > 0:
#                    if item.name != "Sulfuras, Hand of Ragnaros":
#                       item.quality = item.quality - 1
#            else:
#                if item.quality < 50:
#                    item.quality = item.quality + 1
#                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
#                        if item.sell_in < 11:
#                            if item.quality < 50:
#                                item.quality = item.quality + 1
#                        if item.sell_in < 6:
#                            if item.quality < 50:
#                                item.quality = item.quality + 1
#            if item.name != "Sulfuras, Hand of Ragnaros":
#                item.sell_in = item.sell_in - 1
#           if item.sell_in < 0:
#                if item.name != "Aged Brie":
#                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
#                        if item.quality > 0:
#                            if item.name != "Sulfuras, Hand of Ragnaros":
#                                item.quality = item.quality - 1
#                    else:
#                        item.quality = item.quality - item.quality
#                else:
#                    if item.quality < 50:
#                        item.quality = item.quality + 1
