#============================================ FOR LOOP ======================================
from sympy import Ne


squares = ["red", "yellow", "green", "purple", "blue"]
print(squares)
for i in range (0,5):
    squares[i] = "white"
    print(squares)

#============================================ENUMERATE======================================
Genres = ["rock", "R&B", "Soundtrack", "R&B", "Soul", "Pop"]
for i,Genres in enumerate(Genres):
    print(i,Genres)


#============================================ WHILE LOOP =========================================

squares = ["orange", "orange", "purple", "orange", "blue"]
Newsquares = []   #EMPTY LIST
print(Newsquares)

i=0
while(squares[i]=="orange"):
    Newsquares.append(squares[i])
    i=i+1
print(Newsquares)


#========================================other FOR LOOP example=================================
squares=['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)