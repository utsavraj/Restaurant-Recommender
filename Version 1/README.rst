Restaurant-Recommender @Version 1
=====

Based on a budget, recommends you what to buy and how much from a single menu.


Description
-------

Accepts input file named as 'input.txt' (one already added for testing)

**INPUT FILE INFO:**

* First line is the budget. *NOTE*: The budget cannot be negative.
* The next lines are menu items and their corresponding prices seperated by '*' for allignment.


**EXAMPLE**::

    100
    Ichiraku Ramen***************42 
    EndGame Coke 0***************06
    Warai Azami******************02
    Potato Chips*****************11


**OUTPUT FILE INFO:**

* First few lines shows the menu items and their corresponding quantities to buy.
* Last line shows the total spending. This can be equal to the budegt or LOWER.

**EXAMPLE**::

    **RECOMMENDATION**
    Potato Chips x 1
    Warai Azami x 2
    Ichiraku Ramen x 2

    Total Spending: $ 99.00
    
    
Known areas for improvement:
-------
* Goes through highest prices first and does not take other combination into account.
    
**EXAMPLE:**
For input::

      1000
      Onigiri**********************450
      WacDonald Burger*************200
      Water************************350
      
@Version 1 Output::

      **RECOMMENDATION**
      Onigiri x 2

      Total Spending: $ 900.00
      
Better Output::

      Onigiri x 1
      Water x 1
      WacDonald Burger x 1
      
      Total Spending: $ 1000.00    
      
      
Ideas for @Version 2
-------

* Budget can be in different currency.
* Accept multiple menus and give different recommendations based on the menu.
* Accept multiple txt files.


