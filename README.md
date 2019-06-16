# Shopping-Cart-Exercise

The input values are being treated as strings by python even though integers are being inputted.

I have added the price per pound attribute for all the items as indicated in the additional challenges exercise.  For the sake of this exercise the even numbered id's are in 'price_per_pound' and the odd numbered id's are not.  Therefore, if an even number item is entered, the clerk will not be asked to input the weight of the item.

I have also added code to handle errors if a wrong input is entered.  For example, the current products list has only 21 items. If the clerk enters 24 by mistake the code would normally error. To prevent this I have made the code adapt to wrong entries. In summary, if the clerk enters an input that is not one of the ID's assigned to a product, the system will prompt the clerk to re-enter.  Similarly if a wrong weight is entered (a string that can't be converted to float or integer)for the 'price_per-pound' items, the system will classify that as an invalid entry.  Finally, the the system will recognize both 'DONE' or 'done' to finish the order.