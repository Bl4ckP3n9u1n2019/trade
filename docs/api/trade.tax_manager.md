# trade.tax_manager

## trade.tax_manager.TaxManager
The base TaxManager.

A TaxManager object reads an operation and returns the
correspondent percentual taxes for that operation. Since taxes
(and also the way they are applied) may vary greatly from one
context to another, this class just implements a dumb interface
for the tax discovery process, always returning a empty dict of
taxes.

Every OperationContainer object has a reference to an instance
of this TaxManager. If your app need to apply taxes to your
Operation objects, then you should extend this class and inform
the new TaxManager to your OperationContainer by

    operation_container_object.tax_manger = your_tax_manager_object

The OperationContainer always access the TaxManager when
fetch_positions() is called. Behind the scenes the container
calls this methods from the TaxManager object:

    tax_manager.get_taxes_for_operation(operation)
    tax_manager.get_taxes_for_daytrade(operation)

for every operation and daytrade present on the container.

### Methods:

#### get_taxes_for_operation(self, operation):
Return a empty dictionary.

#### get_taxes_for_daytrade(self, operation):
Return a empty dictionary.


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  
