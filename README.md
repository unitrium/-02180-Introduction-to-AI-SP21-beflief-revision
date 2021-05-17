# 02180 - Introduction to AI - SP21 - BELIEF REVISION ASSIGNMENT

Assignement for the course 02180 Introduction to AI.   

The goal of this assignment is to implement a belief revision agent.

## Description

This code create a belief base. Then you can add beliefs in it, check logical entailment thanks to the resolution algorithm and do contraction, revision and expansion.

## Requirements

Run the following command to install all the requirements:
```python
pip install -r requirements.txt
```

The two main requirements for this code are:
* python 3.8
* sympy 1.8

## How to run the code

The following command is used to run the code
```python
python main.py
```
Then, you will have different possible actions:
```python
add #to add a belief to the belief base
display #to display the current belief base
clear #to clear the belief base
quit #to stop the agent
```

To add a belief you can use the following symbols:
```python
~ #NOT ~p
& #AND p&q
| #OR p|q
>> #implies p>>q
() #Parenthesis to structure the belief p>>(q&r)
```

## How to run the tests

To be able to run the test you need the following package:  
It is already installed if you have run the requirements.txt file
* pytest 6.2.3

Then, the following command is used to run the tests
```python
python test.py
```

