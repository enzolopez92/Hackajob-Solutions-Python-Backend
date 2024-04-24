class Solution:
    def run(self, n, m, movies):
        # Initialize a list to store the stack
        stack = list(range(1, n+1))
        
        # Initialize an empty list to store the output
        output = []
        
        # Iterate through the movies to watch
        for movie in movies:
            # Find the index of the movie in the stack
            index = stack.index(movie)
            
            # Append the number of movies above the current movie to the output list
            output.append(index)
            
            # Remove the movie from the stack
            stack.pop(index)
            
            # Add the movie back to the top of the stack
            stack.insert(0, movie)
        
        # Convert the output list to a comma-separated string
        movies_array = ",".join(map(str, output))
        
        return movies_array