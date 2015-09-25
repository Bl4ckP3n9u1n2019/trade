import trade

# create the asset and the operation
asset = trade.Asset('some asset')
operation = trade.Operation(date='2015-09-18', asset=asset, quantity=20, price=10)

# create a container with some comissions associated with it
comissions = {
    'some comission': 1,
    'other comission': 3,
}
container = trade.OperationContainer(operations=[operation], comissions=comissions)

# identify operations and prorate the comissions
container.identify_daytrades_and_common_operations()
container.prorate_comissions_by_daytrades_and_common_operations()

# create an accumulator for the asset
accumulator = trade.Accumulator(asset)

# accumulate the operation
operation = container.common_operations[asset]
accumulator.accumulate_operation(operation)

print(accumulator.quantity)
#>>20

print(accumulator.price)
#>>10.2
# the original price (10) plus the comissions
# the OperationContainer prorated

print(accumulator.price * accumulator.quantity)
#>>204
# 200 from the raw operation
# (20 quantity * 10 unitary price)
# + 4 from the total comissions
