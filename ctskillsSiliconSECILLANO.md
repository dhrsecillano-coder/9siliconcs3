# Computational Thinking Exercise

## [Smart School Canteen Queue]

**Name:** Don Hill R. Secillano

**Section:** Silicon

**Last Name:** Secillano

**Date:** August 20, 2026

## Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

Some students take too long to decide what to order.
The cashier has to manually calculate totals and give change.
There is no system to track which food items are running out.
Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

### Step 1: Identify the Big Problem

Main Problem: The canteen will take too long to serve the students they ordered.

### Step 2: Identify three to four Sub-Problems

Please list possible sub-problems:

1. Some students take too long to decide what to order.

2. The cashier has to manually calculate totals and give change.

3. There is no system to track which food items are running out.

### Step 3: Define Computational Thinking Approaches

For each sub-problem, apply CT skills:

1. Time usage because of students deciding what to order
2. The cashier has to manually calculate totals and give change.
3. There is no system to track which food items are running out.


CT Skill
1. Pattern Recognition
2. Decomposition
3. Alorithm Design


Example Solution
1. Use what the students usually choose, the canteen can prefer foods or items that are popular.
2. First select the food, then calculate the total and finally give the change.
3. Create a process by which they will record the stocks, check the remaining items and alert the canteen staffs on what to do.



### Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem

START
    
    Set Total = 0

    Input number of items
    For each item
        Input item price
        Total = Total + item price
    End for
    
    Display "Total amount: ", Total

    If cash given >= Total
        change = cash given - Total
        Display "Change: ", change
    Else
        Display "Not Enough Cash"
    End if

End