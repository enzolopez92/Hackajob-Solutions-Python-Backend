# Movie Collection Back End Challenge 

Your task is to create an application for a client that has a big movie collection. He organises the collection in a big stack. When he wants to watch a movie he locates it in the stack and removes it. After he is finished watching the movie, he places it back at the top. Since the stack of movies is big, he will need to know the position of each movie.

He likes to know for each movie how many other movies are above it in the stack and, with this information he can calculate the position in the stack. Each movie is identified by a number printed on the box.

Implement a program that will keep track of the position for each movie. Each time he removes a movie from the stack, your program should print the number of movies that were placed above it before it was removed. After the movie is watched it is placed at the top of the stack.

## INPUT

int        n
                ^^ the number of movies in the stack

int        m
                ^^ the number of movies he wants to watch

int[]        movies
                ^^ an array with m integers a1 . . . am (1 <= ai <= n) representing the identification numbers of movies that he wants to watch

We assume assume that the initial stack contains the movies with numbers 1, 2, . . . , n in increasing order, where the movie with label 1 is at the top of the stack.

## OUTPUT

string        movies_array
                     ^^ array with m integers separated by comma, where the i-th integer gives the number of movie boxes above the box with label ai, immediately before this box is removed from the stack.

Note: After each find, the movie box is placed at the top of the stack.

## CONSTRAINTS

1 <= n, m <= 100 000

## EXAMPLE 1

### Input

3
3
[3,1,1]

### Output
"2,1,0"

## EXAMPLE 2

### Input

5
3
[4,4,5]

### Output

"3,0,4"