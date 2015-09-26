# trade.operation_container

This module contains the class definitions of the OperationContainer.
The OperationContainer is used to group operations and then perform
tasks on them.


## trade.operation_container.OperationContainer
A container for operations.

An OperationContainer is used to group operations, like operations
that occurred on the same date, and then perform tasks on them. The
OperationContainer can:

- Separate the daytrades and the common operations of a group of
  operations that occurred on the same date by using the method:

    * identify_daytrades_and_common_operations()

- Prorate a group of taxes proportionally for all daytrades and
  common operations, if any, by using the method:

    * prorate_comissions_by_daytrades_and_common_operations()

### Attributes:
+ date: A string 'YYYY-mm-dd' representing the date of the operations on the container.
+ operations: A list of Operation instances.
+ comissions: A dict with discount names and values to be deducted from the operations.
+ daytrades: a dict of Daytrade objects, indexed by the daytrade asset.
+ common_operations: a dict of Operation objects, indexed by the operation asset.

### Properties

#### total_comission_value(self):
Returns the sum of values of all comissions.

#### volume(self):
Returns the total volume of the operations in the container.

### Methods

#### fetch_positions(self):
Fetch the positions resulting from the operations.

Fetch the position is a complex process that needs to be
better documented. What happens is as follows:
- Separate all daytrades and common operations;
- Group all common operations with one asset into a single Operation, so in the end you only have one operation per asset (on self.common_operations);
- Group all daytrades with one asset into a single Daytrade, so in the end you only have one daytrade per asset;
- put all common operations in self.common_operations, a dict indexed by the operation's asset name;
- put all daytrades in self.daytrades, a dict indexed by the daytrade's asset name;
- Prorate all comissions of the container for the common operations and the purchase and sale operation of every daytrade;
- Find the taxes to be applied to every common operation and to every purchase and sale operation of every daytrade.

After this method:
- the raw operations list of the container remains untouched;
- the container common_operations list is filled with all common operations of the container, with all information about comissions and taxes to be applied to each operation;
- the container daytrades list is filled with all daytrades of the container, with all information about comissions and taxes to be applied to every purchase and sale operation of every daytrade.

#### prorate_comissions_by_daytrades_and_common_operations(self):
Prorates the container's comissions by its operations.

This method sum the discounts in the comissions dict of the
container. The total discount value is then prorated by the
daytrades and common operations based on their volume.

#### prorate_comissions_by_operation(self, operation):
Prorates the comissions of the container for one operation.

The ratio is based on the container volume and the volume of
the operation.

#### identify_daytrades_and_common_operations(self):
Separates operations into daytrades and common operations.

After this process, the attributes 'daytrades' and
'common_operations'  will be filled with the daytrades
and common operations found in the container operations list,
if any. The original operations list remains untouched.

#### extract_daytrade(self, operation_a, operation_b):
Extracts the daytrade part of two operations.

1. Find what is the purchase and what is the sale
2. Find the daytraded quantity; the daytraded
quantity is always the smallest absolute quantity
3. Update the operations that originated the
daytrade with the new quantity after the
daytraded part has been extracted; One of
the operations will always have zero
quantity after this, being fully consumed
by the daytrade. The other operation may or
may not end with zero quantity.
4. create the Daytrade object
5. If this container already have a Daytrade
with this asset, we merge this daytrade
with the daytrade in self.daytrades -
in the end, there is only one daytrade per
asset per OperationContainer.

#### add_to_common_operations(self, operation):
Adds an operation to the common operations list.

#### merge_operations(self, existing_operation, operation):
Merges one operation with another operation.

#### find_taxes_for_positions(self):
Gets the taxes for every position on the container.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
