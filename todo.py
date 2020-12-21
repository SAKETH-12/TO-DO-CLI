


import sys
import os.path
from datetime import datetime


def addTodo(todow):
                                                                  # This function adds a New Todo in the todo.txt file.
    if os.path.isfile('todo.txt'):                                # If todo.txt exists then add task in first line.
        try:
            with open("todo.txt",'r') as todoFileRead:
                previousTodos = todoFileRead.read()
            with open("todo.txt",'w') as todoFileWrite:
                todoFileWrite.write(todow + "\n" + previousTodos)
        except IOError:
            print("File not accessible")
    else:
        try:                                                      # If not then creates a new file and adds the task.
            with open("todo.txt",'w') as todoFileWrite:
                todoFileWrite.write(todow + '\n')
        except IOError:
            print("File not accessible")
    print('Added todo: "{}"'.format(todow))
    
    
    
    
def showTodoList():

	                                                              # Function to List and print the available todos' in the latest added order
    if os.path.isfile('todo.txt'):
        try:
            with open("todo.txt",'r') as todoFileRead:
                data=todoFileRead.readlines()
            noOfLines=len(data)
            printString=""
            for line in data:
                printString += '[{}] {}'.format(noOfLines, line)
                noOfLines -= 1
            sys.stdout.buffer.write(printString.encode(sys.stdout.encoding))   # Print the Tasks according to encoding of user 
        except IOError:
                print("File not accessible")
    else:
	    print ("There are no pending todos!")
        
def printHelp():

    # This function prins Usage Section when no argument is passed or when asked for help.
	todohelp='''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics'''
	sys.stdout.buffer.write(todohelp.encode(sys.stdout.encoding))		# Print according to encoding of users output stream
    
def delTodo(number):

	# This function is used to delete the task from the todos List. (If available)
    if os.path.isfile('todo.txt'):
        
        try:
            
            with open("todo.txt",'r') as todoFileRead:
                data=todoFileRead.readlines()
            noOfLines=len(data)
            if number>noOfLines or number<=0:
                print(f"Error: todo #{number} does not exist. Nothing deleted.")
            else:
                try :
                    with open("todo.txt",'w') as todoFileWrite:
                        for line in data:
                            if noOfLines != number:
                                todoFileWrite.write(line)
                            noOfLines -= 1
                    print(f"Deleted todo #{number}")
                except IOError:
                    print("File not accessible")
        except IOError:
            print("File not accessible")
            
    else:
        
	    print("Error: todo #{} does not exist. Nothing deleted.".format(num))
    
def todoMarkAsDone(number):
                                                        # Function to mark the given task as Done. (If available)
    if os.path.isfile('todo.txt'):
        try:
            with open("todo.txt",'r') as todoFileRead:
                data=todoFileRead.readlines()
            count=len(data)
            if number>count or number<=0:
                print("Error: todo #{} does not exist.".format(number))
            else:
                try:
                    with open("todo.txt",'w') as todoFileWrite:
                        if os.path.isfile('done.txt'):
                            try:                        # Produces output according to the availability of done.txt file.
                                with open("done.txt",'r') as doneFileRead:
                                    doneData=doneFileRead.read()
                                with open("done.txt",'w') as doneFileWrite:
                                    for line in data:
                                        if count==number:
                                            doneFileWrite.write("x "+datetime.today().strftime('%Y-%m-%d')+" "+line)
                                        else:
                                            todoFileWrite.write(line)
                                        count-=1
                                    doneFileWrite.write(doneData)
                            except IOError:
                                print("File not accessible")
                        else:
                            try:
                                with open("done.txt",'w') as doneFileWrite:
                                    for line in data:
                                        if count==number:
                                            doneFileWrite.write("x "+datetime.today().strftime('%Y-%m-%d')+" "+line)
                                        else:
                                            todoFileWrite.write(line)
                                        count-=1
                            except IOError:
                                print("File not accessible")
                                
                except IOError:
                        print("File not accessible")

                print("Marked todo #{} as done.".format(number))
        except IOError:
                print("File not accessible")
                
    else:
	    print("Error: todo #{} does not exist.".format(number))
        
def generateReport():

	# Function to Generate the Report.
	countTodo=0
	countDone=0
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as todoFileRead:
	    	todoData=todoFileRead.readlines()
	    countTodo=len(todoData)
	if os.path.isfile('done.txt'):
	    with open("done.txt",'r') as doneFileRead:
	    	doneData=doneFileRead.readlines()
	    countDone=len(doneData)
	line =datetime.today().strftime('%Y-%m-%d') + " Pending : {} Completed : {}".format(countTodo,countDone)
	sys.stdout.buffer.write(line.encode(sys.stdout.encoding))
    
def start(): 
                                                                                                
    if len(sys.argv) == 1:            # if there are no arguments
        printHelp()
    elif sys.argv[1] == 'help':
        printHelp()
    elif sys.argv[1]=='ls':
        showTodoList()
    elif sys.argv[1]=='add':
        if len(sys.argv)>2:
            addTodo(sys.argv[2])
        else:
            print("Error: Missing todo string. Nothing added!")
    elif sys.argv[1]=='del':
        if len(sys.argv)>2:
            delTodo(int(sys.argv[2]))
        else:
            print("Error: Missing NUMBER for deleting todo.")
    elif sys.argv[1]=='done':
        if len(sys.argv)>2:
            todoMarkAsDone(int(sys.argv[2]))
        else:
            print("Error: Missing NUMBER for marking todo as done.")
    elif sys.argv[1]=='report':
        generateReport()
    else:
        print('Option Not Available. Please use "./todo help" for Usage Information')
    
    

if __name__ == "__main__": 
    start()
    


    


    


    