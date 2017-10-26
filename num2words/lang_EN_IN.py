# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import unicode_literals
from .lang_EN import Num2Word_EN


class Num2Word_EN_IN(Num2Word_EN):
    def set_high_numwords(self, high):
        self.cards[10 ** 7] = "crore"
        self.cards[10 ** 5] = "lakh"


n2w = Num2Word_EN_IN()
to_card = n2w.to_cardinal
to_ord = n2w.to_ordinal
to_ordnum = n2w.to_ordinal_num


def main():
    for val in (15000,
                15 * 10 ** 5,
                15 * 10 ** 6,
                15 * 10 ** 7,
                15 * 10 ** 8,
                15 * 10 ** 9,
                15 * 10 ** 10):
        n2w.test(val)


if __name__ == "__main__":
    main()
