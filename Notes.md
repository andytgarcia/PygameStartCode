#Programming Notes

#Principles of Programming

Ideas and concepts to help you succeed in programming

- ***Always keep program in a working state AT ALL TIMES***
- Attempt to code small additions. Don't implement too much detail or functionality
- Each idea/addition should be implemented in its own function definition
- Name functions and variables meaningfully
- If something breaks...***STOP***. Seek help or begin to debug
- It is okay to not know how to do something! Look it up
  - [Pygame Help](https://www.pygame.org/docs/ref/draw.html)
  - [Python Help](https://www.w3scho;s.com/python/)

##Create Task Requirements

- **A purpose** - why did you write this application
- **A List** - a list and how it reduced complexity or how you could not write the app without one
- **A Function**
  - *Sequence* - code that runs over several lined over
  - *Selection* - if statements
  - *Iteration* - looping
  - *Parameter*- input to the function
    - This input must change the result of the function

### Parameter

What is a parameter?

```python
def function(x, y):

```

x and y in the above function definition are parameters

### For Looping through a List

Assume the following list

```python
bullets = []

bullets.append((100, 100, 5))
bullets.append((400, 300, 5))
bullets.append((340, 560, 5))
```

How do we loop through this bullet list?

```python
for currentBullet in bullet:
    #code to process each bullet goes here
    #each bullet will be stored in variable currentBullet
```

In general. it looks like

```python
for temporaryVariable in listName:
    #code to process each item as stores in temporary variable
```

Things we may for loop through a list for:
 - draw all things in a list
 - check everything for collisions
 - choose something from the list based upon some criteria
   - choose a hard question for quiz game
   - take a look at all player one's bullets
 - see if something is true about the list
   - in Wordle, check the word against every letter to see if its correct