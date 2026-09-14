# Class Relationships: Association and Multiplicity

## Previous Work

[Part I - Classes and Objects](classObjectUML.md)

[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class

Class: Basketball

Description: My class is an object that represents one of the sports.

## New Related Class

Class: Brand

Description: Brands creates basketball and delivers it each with its own unique style.

## Association

Relationship: Basketball has brands

Explanation: Basketball has brands that creates and sells it

## Multiplicity

Multiplicity: One to Many

Explanation: Basketball has many brands and isnt the only one that has brands.

## UML Class Relationship Diagram

![Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation

[View Python Source](classRelationships.py)

## Test Run

![Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram

![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis

### What is the association between your two classes?

- The association between my two class is brand and basketball. A brand can be associated with many basketball. For example, my brand is Nike and the ball1 and ball2 is associated with Nike.

### What multiplicity did you choose and why?

- I choose one to many a brand can have zero or many basketball. For example, If I created a new brand, it may not have any basketball yet but Nike already have. Therefore, one to many is great to use.

### How did you implement the relationship in Python?

- I implemented the relationship by first creating a list. The brand1.basketball stores the objects related to brand. By using append, I added ball1 and ball2 to the list.

### Why did you store an object reference instead of copying its data?

- I stored the object so that Brand can access its data without copying the basketball's existing data.

### If your relationship uses many, why is a list appropriate?

- The relationship uses many because one brand can have many basketball. Also, a list is appropriate to use because it does not contain the names or copied information but rather the actual basketball references.