# <b>Restaurant</b>

Write a code for orders management to handle the orders. The main menu has three options: add order, remove order and exit program, and in the add order option should show a sub-menu with the _restaurant menu_.

The ___restaurant menu___ has 4 categories and 3 options for each one:
> | Category | Options |
> |:---------|:--------|
> | Protein | (1) Option_1.1<br> (2) Option_1.2<br>(3) Option_1.3 |
> | Accompaniment | (1) Option_2.1<br> (2) Option_2.2<br>(3) Option_2.3 |
> | Salad | (1) Option_3.1<br> (2) Option_3.2<br>(3) Option_3.3 |
> | Juice | (1) Option_4.1<br> (2) Option_4.2<br>(3) Option_4.3 |

<!-- TODO Replace Option_N.N with their real option -->

## <b>Requeriments:</b>

1. The _orders list_ should implements a __FIFO__ (First In, First Out) data structure.

2. When the user selects a menu must write the code for each selection. <b>Example:</b> ```'1231'``` stands for: _option 1_ for protein, _option 2_ for accompaniment, _option 3_ for salad and _option 1_ for juice.

<!-- TODO Replace the options in the example. -->

3. The list cannot have repeated orders.

4. The software can queue up to 5 orders, when a sixth order is entered the program must not added, instead should print a message ```"We are full! Can't add more orders"```.

5. The _Remove order_ option in the main menu should "dequeue" the oldest queued order. If there aren't pending orders, should print a message ```"We are empty! No orders left"```.

### <b>Required concepts (_Hints_):</b>

> - <span style="color:lightblue">While:</span> for the program remain running until the user selects the _Exit_ option.
> - <span style="color:lightblue">Queues:</span> A global list must enqueue the orders at the time they are being entered. Search the ```queue``` data structure.
> - <span style="color:lightblue">Input + If-else:</span> To implement a menu must have a variable for the entered option, and switch between if-else sentences to execute the selected option.

---