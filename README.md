# Path_Planning_Algorithms

Source Code: The code has been divided into four main functions namely:
1. The environment setup consisting of an obstacle in the shape of tetrominoes.
   <img width="407" alt="image" src="https://github.com/malaviyaneha/Path_Planning_Algorithms/assets/116248447/fbf08151-4760-4a71-924a-4593a39d2185">

3. A function for Breadth First Search was implemented. We know that it follows the queue
algorithm. Queue follows the FIFO (First in First out) methodology.
• This further has another function known as isValid where we check whether the
neighboring cells have an obstacle. This will return to us the validity of visiting that
cell in our path.
• In the main function, we have a queue where we pop out the first element and
assign that to x,y, and the third element as our path.
• If this x, and y are the goal coordinates then we return to the path. However, if not,
then we run a for loop to iterate 4 times for each neighboring cell and execute the
isValid function. These values are then appended and a path is calculated for the
point robot to follow in order to reach the goal location.

<img width="348" alt="image" src="https://github.com/malaviyaneha/Path_Planning_Algorithms/assets/116248447/45fe142c-afc8-4dc5-aa67-b3bf774f4cb6">

3. Another function was created for Depth First Search.
• We know that in DFS it follows the logic of stack which is FIFO(First in First out).
Therefore, the only difference between the codes of BFS and DFS would be while
popping a value out of the queue.

<img width="352" alt="image" src="https://github.com/malaviyaneha/Path_Planning_Algorithms/assets/116248447/0fc8452b-f8f9-4017-b825-4cff922b82ab">

4. Next in line, we have the Dijkstra search. Here, we calculate the shortest distance between
the starting position and the goal position.

<img width="370" alt="image" src="https://github.com/malaviyaneha/Path_Planning_Algorithms/assets/116248447/872cd170-7669-49e7-9d7a-361682b294e3">

