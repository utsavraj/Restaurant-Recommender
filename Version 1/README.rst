Restaurant-Recommender @Version 1
=====

Based on a budget, recommends you what to buy and how much from a single menu.


Description
-------

Accepts input file named as 'input.txt' (one already added for testing)

INPUT FILE INFO:
* Create a resource.
* Retrieve a resource.
* Delete a resource.
* Retrieve a resource again to confirm it is gone.
* First line is the budget. *NOTE*: The budget cannot be negative.
* The next lines are menu items and their corresponding prices seperated by '*' for allignment.


To get started, after cloning the `repository`_, you should install the
development dependencies::

    100 

If you prefer to keep things isolated you can create a virtual
environment::

    $ virtualenv gabbi-venv
    $ . gabbi-venv/bin/activate
    $ pip install -r requirements-dev.txt

