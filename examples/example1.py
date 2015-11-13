"""Example of the use of Accumulators.

http://trade.readthedocs.org/
https://github.com/rochars/trade
License: MIT

Copyright (c) 2015 Rafael da Silva Rocha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from __future__ import print_function

import trade

# create the asset that we are going to trade
asset = trade.Asset(name='Google Inc', symbol='GOOGL')

# create the accumulator to accumulate trades with the asset
accumulator = trade.Accumulator(asset)


print(accumulator.subject.name)
#>> Some asset

print(accumulator.state['quantity'])
#>> 0

print(accumulator.state['price'])
#>> 0

print(accumulator.state['results'])
#>> {}


# create a trade operation buying the asset
purchase = trade.Operation(
    subject=asset,
    quantity=10,
    price=650.73,
    date='2015-09-23'
)

# accumulate the trade
accumulator.accumulate(purchase)


print(accumulator.state['quantity'])
#>> 10

print(accumulator.state['price'])
#>> 650.73

print(accumulator.state['results'])
#>> {}


# create a new trade operation selling the asset
sale = trade.Operation(
    subject=asset,
    quantity=-5,
    price=656.77,
    date='2015-09-24'
)

# accumulate the new trade
accumulator.accumulate(sale)


print(accumulator.state['quantity'])
#>> 5

print(accumulator.state['price'])
#>> 650.73

print(accumulator.state['results'])
#>> {'trades': 30.199999999999818}
