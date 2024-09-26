# Rectangle Class: User Guide
## Introduction
The Rectangle class allows you to create and work with rectangles of different sizes. You can define rectangles using either whole numbers (like 5, 10) or decimal numbers (like 3.5, 7.2). This guide will walk you through how to create a rectangle, calculate its area and perimeter, and compare it with other rectangles.

## Creating a Rectangle
To create a rectangle, you need to provide the width and height. Both the width and height must be non-negative numbers (zero or greater).

### Example:

```python
# Creating a rectangle with whole numbers (integers)
rectangle1 = Rectangle(5, 10)

# Creating a rectangle with decimal numbers (floats)
rectangle2 = Rectangle(3.5, 7.2)
```
In the example above, rectangle1 has a width of 5 and a height of 10. rectangle2 has a width of 3.5 and a height of 7.2.

## What Can You Do with a Rectangle?
### Get the Dimensions
You can easily find out the width and height of your rectangle.

```python
# Get the width and height
rectangle1.get_width()   # Returns 5
rectangle1.get_height()  # Returns 10
```

### Set New Dimensions
If you want to change the width or height of your rectangle, you can update them using simple commands:

```python
# Set new width and height
rectangle1.set_width(8)
rectangle1.set_height(12)
```
Now, rectangle1 has a width of 8 and a height of 12.

### Calculate the Area
The area of a rectangle is the amount of space inside it. You can calculate the area using the get_area method:

```python
# Calculate the area
rectangle1.get_area()  # Returns 96 (because 8 * 12 = 96)
```

### Calculate the Perimeter
The perimeter is the total distance around the outside of the rectangle. To calculate the perimeter:

```python
# Calculate the perimeter
rectangle1.get_perimeter()  # Returns 40 (because 2 * (8 + 12) = 40)
```

### Compare Two Rectangles
You can compare two rectangles to see if they have the same size, or which one is bigger.

 - Equality Check: Check if two rectangles are exactly the same size (same width and height).

 - Size Comparison: Find out if one rectangle is smaller or larger than another based on the area.

 ```python
 rectangle1 == rectangle2  # Returns False (because their sizes are different)
rectangle1 < rectangle2  # Compares the areas and returns True or False
```

### Iterate Over Dimensions
You can loop through the dimensions of a rectangle if you want to process them in some way.

```python
# Loop through the dimensions
for dimension in rectangle1:
    print(dimension)  # Prints out the length and width
```

Summary of Key Features
- Easy Creation: Define a rectangle with a width and height.
- Get/Set Dimensions: Access or update the width and height anytime.
- Area & Perimeter: Quickly calculate the area and perimeter.
- Compare Rectangles: Check if two rectangles