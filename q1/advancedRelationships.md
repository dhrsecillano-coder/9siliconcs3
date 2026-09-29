# Advanced Class Relationships

## Previous Activities

[classAttrib](classAttributesMethods.md)

[classRel](classRelationships.md)

## Existing System Description:

## Inheritance Relationship

Parent: Sport

Child: Basketball

Explanation: Basketball is one type of a sport. The parent sports stores general attributes while the basketball only displays specific attributes.

## Inheritance UML

![Inheritance](images/inheritanceDiagram.png)

## Composition/Aggregation

Relationship: Aggregation

Explanation: The game can still exist outside in basketball system. If basketball is removed, the game is still present. Therefore the game HAS-A weak relationship with basketball.

## Advanced UML Diagram

![Advanced UML](images/advancedClassDiagram.png)

## Python Implementation

[Source Code](advancedRelationships.py)

## Test Run

![Test](images/advancedTestRun.png)

## Object Diagram

![Objects](images/advancedObjectDiagram.png)

## Reflection

### 1. Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.

- Basketball is a specific type of sports making the IS-A relationship suitable. Sports is the parent class and the child class Basketball inherits some attributes like venue, and number of players.

### 2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.

- Using the (super().__init__()) avoided the repitition or duplication codes in basketball by reusing the attributes such as Name, Players, Equipments and a lot more.

### 3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.

- It is aggregation because game can exist on its own even without a specific basketball.

### 4. What is the difference between Association from Part III and the advanced relationship you implemented?

- Part 3 focuses more on the links of independent objects while part 4 is more on gaining a deeper understanding in how these codes can be reused through inheritance or dependency.

### 5. How does your design follow the DRY principle?

- My design avoids repeating codes by using or placing these shared attributes and reusing using the (super().__init__()) code.