import turtle#turtle module is imported
import pandas#pandas module is imported as well
s=turtle.Screen()#Screen class is present in turtle module
image=r"C:\Users\LENOVO\OneDrive\Desktop\oh1\blank_states_img.gif"#r is meant for raw string,which means that \ is not seen as an escape character
#but as raw string
s.addshape(image)#the addshape is a method used by s object of Screen class to add image's shape to the screen
turtle.Turtle(image)#this can be used to add the given image to the screen

df=pandas.read_csv(r"D:\us-states-game-start\50_states.csv")#this is used to read csv file and convert that into pandas dataframe
# print(df)
list_of_states=df.state.to_list()#this is used to convert a column(which is a series datatype)into list,only series datatype can be converted into list
# print(list_of_states)
guessed_states=[]
missed_state=[]
while len(guessed_states)<50:#the loop runs until all all are guessed
    answer_state=s.textinput(title=f"{len(guessed_states)}/50",prompt="Guess another state").title()#this is like input function in python
    #fstring is used to reflect dynamic strings....title() means,1st letter will also be capital
    if answer_state in list_of_states:#if answer_state is in list_of_states list
        guessed_states.append(answer_state)#answer_state is appended to guessed_state list
        t=turtle.Turtle()#now turtle is created using Turtle class present in turtle module
        t.penup()#pen is made up using penup method of t object which is object of Turtle class
        t.hideturtle()#now the turtle is hidden using hideturtle method of t object which is of Turtle class
        dm=df[df.state==answer_state]#this means that only the records correspondinf to the rows where df.state ==answer_state would be selected
        #and stored in variable dm
        t.goto(int(dm.x),int(dm.y))#then turtle goes to a particular position using x and y column of the dataframe by converting that into
        #integer
        t.write(dm.state.item())#then the turtle object should write the state name respectively over that coordinate....item() reads just the
        #item and not its datatype and other things,item() basically converts series datatype to normal datatype

    if answer_state=='Exit':
        for a in list_of_states:#for a in list_of_states list if a is not in guessed_states then it is added in missed state lisst,a dataframe is
            #created out of that and added to csv
            if a not in guessed_states:
                missed_state.append(a)
        #the above for loop can be replaced with missed_state=[a for a in list_of_states if a not in guessed_states]
        new_data=pandas.DataFrame(missed_state)
        new_data.to_csv("D:/missedstates.csv")
        break






