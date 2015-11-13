# events
Copyright (c) 2015 Rafael da Silva Rocha  
https://github.com/rochars/trade  
https://python-trade.appspot.com

events: A default set of events for the trade module.

This plugin provides a standard set of events for the trade module.
Events are subclasses of trade.Occurrence. They are passed to
Accumulator and Porfolio objects to change asset accumulation data.

It contains the definitions of:
- Event
- StockSplit
- BonusShares

Events can be accumulated by Portfolio objects just like any other
occurrence. Like any other Occurrence subclass, each event must
for implement a update_container() method that receives a
trade.Accumulator object. This method will contain the logic for the
update on the accumulator state.


## Event(Occurrence)
An occurrence that change the state of one or more assets.

This is a base class for events.

### Attributes:
+ date: A string 'YYYY-mm-dd', the date the event occurred.
+ asset: The target asset of the event.


## StockSplit(Event)
A stock split.

This class represents both stock splits and reverse stock splits.
Stock splits are represented by values greater than 1.
Reverse stock splits are represented by values between 0 and 1.

### Methods:

#### update_container(self, accumulator)
Performs a split or a reverse split on the stock.


## class BonusShares(Event)
Bonus shares.

### Methods:

#### update_container(self, accumulator)
Add stocks received as bonus shares do the accumulator.


## License
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
