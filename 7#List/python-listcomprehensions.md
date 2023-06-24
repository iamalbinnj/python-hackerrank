Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z. Please use list comprehensions rather than multiple loops, as a learning exercise.

### Example
x=1
y=1
z=2
n=3

Print an array of the elements that do not sum to .
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]

### Input Format

Four integers x,y,z and n, each on a separate line.

### Constraints

Print the list in lexicographic increasing order.

### Sample Input 0
```
1
1
1
2
```
### Sample Output 0
```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```
### Sample Input 1
```
2
2
2
2
```
### Sample Output 1
```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
```
Solution Link : [problem.py](./problem.py)