# Class Attributes and Methods

**Name:** Don Hill R. Secillano

**Section:** Silicon

**Last Name:** Secillano

**Date:** September 8, 2026

## Previous Design

Link to my previous activity:

[classObjectUML.md](classObjectUML.md)

## Design Revision

- No major changes were needed from my original design.

## Visibility Decisions

| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| Brand | string | public | To know the brand of the ball |
| Size | Integer | public | To know the size of the ball |
| Weight | Decimal | public | To know the weight of the ball|
| Serial Number | String | private | Used privately to know the exact specific ball |

## Updated UML Class Diagram

![Class Diagram](images/classDiagramSG5.png)

## Python Implementation

[View Python Source](classImplementation.py)

## Test Run

![Test Run](images/classTestRun.png)

## Object Diagram

![Object Diagram](images/objectDiagram.png)

## Analysis

### Why did you make your chosen attribute private?

- I made serial number private because it is the identity of the object and I dont want to have it changed in the code.

### Which method changes the state of your object?

- the method that changes the state of my object is the change_size().

### How did your two objects demonstrate that instances are independent?

- It shows that when I changed the basketball 1's size, it only affects the basketball 1 and not basketball 2. This shows that whenever I want to change something in an object 1, it will not affect other objects.

### What is the difference between your class diagram and your object diagram?

- My class diagram shows the properties and the type of data it is. It also shows the methods and parameters. On the other hand, the object diagram shows the attributes and its values.