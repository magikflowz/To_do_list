import pickle 

def todolist():
    to_do_list = []
    while(True): 
        print(to_do_list)
        listitems = input("Add things to your to do list: ")
        to_do_list.append(listitems)
        
        if (listitems ==  'quit'):
            to_do_list.append(listitems)
            new_list = ', '.join([str(elem) for elem in to_do_list])
            with open('todolist.txdt', 'w') as f:
                f.write("%s\n" % new_list)
                print("saved succesfully")
                break 
                
todolist()
