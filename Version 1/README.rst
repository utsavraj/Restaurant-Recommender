Restaurant-Recommender @Version 1
=====

Based on a budget, recommends you what to buy and how much from a single menu.


Description
-------

Accepts input file named as 'input.txt' (one already added for testing)

INPUT FILE INFO:
* 
* 

EXAMPLE:
    100 
    Ichiraku Ramen***************42 
    EndGame Coke 0***************06
    Warai Azami******************02
    Potato Chips*****************11

ach YAML file represents an ordered list of HTTP requests along with
the expected responses. This allows a single file to represent a
process in the API being tested. For example:

* First line is the budget. NOTE: The budget cannot be negative.
* The next lines are menu items and their corresponding prices seperated by '*' for allignment.
* Delete a resource.
* Retrieve a resource again to confirm it is gone.
