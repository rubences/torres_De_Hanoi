def move(tf,td):
  global towers
  text=str(towers[tf][-1])+" : "+tf+" => "+td
  towers[td].append(towers[tf][-1])

  del towers[tf][-1]
  moves.append(text)
  
def validate(tf,td):
  try:
    if towers[tf]!=[] :
      if towers[td]==[]:
        return True
      elif towers[tf][-1]<towers[td][-1]:
        return True
    else:
      return False
  except:
    return False
def out():
  for i in range(num-1,-1,-1):
    try:
      a=towers["A"][i]
    except:
      a="|"
    try:
      b=towers["B"][i]
    except:
      b="|"
    try:
      c=towers["C"][i]
    except:
      c="|"
    print("   ",a,"      ",b,"      ",c,sep="")
  print(" -----  -----  -----\n   A      B      C")
print("INSTRUCTION:\nThis is a simulator for the famous Towers Of Hanoi problem. \n\nWhen it asks you for a move enter the tower to move a ring from and the tower to move it to. \n\nFor example enter 'AB' to move the topmost ring from tower A to tower B.\n\nThe number of a disc indicates its size.\n\nEnter 'q' once you are done and it will show you a summary of your moves!\n\n Here is a link if you need more info about the towers of hanoi problem :\n https://www.hackerearth.com/blog/developers/tower-hanoi-recursion-game-algorithm-explained/ \n\n")
num=int(input("Enter number of rings:"))
moves=[]
finalArray=[i for i in range(num,0,-1)]
towers={"A":list(finalArray),"B":[],"C":[]}
out()
ans=input("Enter move (capital letters only):")
while ans!="Q":

  if validate(ans[0],ans[1]):
    move(ans[0],ans[1])
    out()
    if towers["C"]==finalArray:
      print("Yay! You did it!")
      break
  else:
    print("That is not allowed. Make sure you are moving from a tower which has atleast 1 disc and make sure you put only a smaller disc on a larger one.")
  ans=input("Enter move :")
  ans=ans.upper().replace(" ","")
print("The minimum moves for this is",(num**2)-(num-1),"moves.\nYou took",len(moves),"moves. They are as follow:")
for i in moves:
  print(i)