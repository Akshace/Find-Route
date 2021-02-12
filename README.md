# Assignment 1 _ REPORT

CASE-1 route_pichu.py : NAVIGATION

Approach:

1. Started by reading the code, and used debugger on PyCharm to understand the initial code.
2. Expanded the provided return statements to better understand the code.
3. Initially, found that there was no check on visited states. Created check list in moves function for it and added
   it in if statement to avoid those positions while traversing.
4. The search problem implements DFS as a stack is used.
5. It can be changed to queue implementation by using fringe.pop(0), and will act as BFS.
6. At a node, where there are multiple paths avaiable, the algorithm traverses through each path. If a path is blocked,
   the stacks pops the elements until the diverging node is reached.
7. Initial code provided was getting stuck once it traversed through a blocked path as there was no check for traversed states.


Challenges faced:

1. How to give argument variable like map.txt? 
Ans - Edit configurations

2. How to stop pichu from traversing to already visited states?
Ans - A check list with already visited states appended.

3. If a blocked path is traversed, how to manage the string which should return the final path?
Ans - This was little time taking. Problem was if a wrong path is taken then how do I remove the wrong strings appended till the
	  from the diverging node. I associated every new state traversed with a path string. For eg. One up move - "U", 
	  next up state -  "UU". Because of this, the diverging node has the path till its position. If a blocked path is traversed,
      and stack pops and returns to the diverging node, all the blocked path strings will be removed.

	  
CASE-2 arrange_pichus.py : Hide-and-Seek

Approach:

1. Started by reading the code, and used debugger on PyCharm to understand the initial code.
2. Expanded the provided return statements to better understand the code.
3. Initially, found that there was no check on already kept pichus and code was just looking for '.' and placing pichus.
4. First, I tried reducing the row and column by 1 to check the working of code, it worked only till 6 pichus, because none of 
   them were being arranged in same row or column. Once k = 7 was given, code failed. 	
5. Tried to figure out how to enable positions which are behind 'X' and not seen by pichus.
6. As once I could get all the avaiable positions once pichus are placed, I could place next pichus.

Challenges:

1. How to get the avaiable positions left once a pichu is placed?
Ans - Created a new board similar in dimensions to original board, with all 1's. These 1's initially marked the available
      positions on the board. Once a pichu was placed, I used functions check_rows and check_col to mark the flag board with 0's
	  on the positions which was blocked by the placed pichu.
	  
	  Created a new .py file named "Flag_Test.py" to check the implementation of this part. Once tested, incorporated it 
	  into arrange_pichus.py.

2. How to start marking 1's and 0's originating from pichu?
Ans - If a pichu is at (2,2), I cannot check for blocked positions from range(0,2), but had to do it for range(2,0), as I had to 
	  proceed from pichu's perspective. So I used a decrementing range with input as (start, end, step) and gave step as -1. This 
	  solved the problem.
	  
3. How to use the updated flag board in placing pichus?
Ans - In successors function, added a new argument as check_board which was this flag_board. Now while placing pichus I could use
      flag board to discard blocked positions.

4. How to update flag board after placing pichus?
Ans - In add_pichus function, I used the row and column received from successors function to feed it to my check_rows and check_col
	  function to get the flag board updated.