# trade.trade

This module contains the class definitions of Asset, Operation,
and Daytrade. You can use them by just:

```python
import trade
asset = trade.Asset()
```


## trade.trade.Asset
An asset represents anything that can be traded.

Asset objects can be created with or without a name.

### Attributes:
+ name: A string representing the name of the asset.
+ expiration_date: A string 'YYYY-mm-dd' representing the expiration date of the asset, if any.

### Methods:

#### _ _ init _ _ (self, name='', expiration_date=None):
Asset objects can be created empty or with name and expiration date.

#### _ _ deepcopy _ _ (self, memo)
Assets always return a reference to themselves when being copied, so they
are never really copied.


## trade.trade.Operation
An operation represents the purchase or sale of an asset.  

### Attributes:  
+ date: A string 'YYYY-mm-dd', the date the operation occurred.
+ asset: An Asset instance, the asset that is being traded.
+ quantity: A number representing the quantity being traded.
+ price: The raw unitary price of the asset being traded.
+ comissions: A dict of discounts. String keys and float values representing the name of the discounts and the values to be deducted from the operation.

### Properties:

#### real_value
Return the quantity * the real price of the operation.

#### real_price
Return the real price of the operation.

The real price is the price with all comissions and taxes already deducted or added.

#### total_comission
Return the sum of all comissions included in this operation.

#### volume
Return the quantity of the operation * its raw price.


## trade.trade.Daytrade
A daytrade operation.

Daytrades are operations of purchase and sale of an Asset on
the same date.

### Attributes:
+ asset: An asset instance, the asset that is being traded.
+ quantity: The traded quantity of the asset.
+ buy: A Operation instance representing the purchase of the asset.
+ sale: A Operation instance representing the sale of the asset.

### Properties

#### result


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
