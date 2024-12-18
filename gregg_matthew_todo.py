### Imports
import argparse

def main_task():
    parser = argparse.ArgumentParser(
    description="A CLI tool that makes a TODO list ")
#### flags
    parser.add_argument(
    '--id', '-i',
    type=int,
    required=False,
    help="Choose a number from one to ten as a numbered task."
    )
    parser.add_argument(
    '--category', '-c',
    type=str,
    required=False,
    help="What type of task are you inputting"
    )

    parser.add_argument(
    '--description', '-d',
    type=str,
    required=False,
    help="Whatis the description of your task"
    )   
    parser.add_argument(
    '--status', '-s',
    type=str,
    required=False,
    help="Show what the staus is incomplete/complete/in progress"
    )
    parser.add_argument(
    '--update', '-u',
    type=int,
    required=False,
    help="What is the description of your task"
    )
    parser.add_argument(
    '--TODO2', '-t',
    type=str,
    required=False,
    help="change your to do lists"
    )
    parser.add_argument('-r', '--read-list', action='store_true')

    args = parser.parse_args()
    ### print what was inputted on screen
    print(f"{args.id=}")
    print(f"{args.category=}")
    print(f"{args.description=}")
    print(f"{args.status=}")
    print(f"{args.update=}")
    print(f"{args.TODO2=}")

### Print whatver you put on todo list to file
    with open("todo.txt", "a") as file:
        file.write(f"{args.id=}, \n")
        file.write(f"{args.category=}, \n")
        file.write(f"{args.description=}, \n")
        file.write(f"{args.status=}, \n")
        file.write(f"{args.update=}, \n")
        file.write(f"{args.TODO2=}, \n")


### Suposed to read whatever is on list and print it
    def print_whole_list():
        with open("todo.txt", 'r'):
            print(print_whole_list)

    # if args.read == True:
    #     print({"todo.txt"})

#### Update status of task
    replace_word = args.replace
    if '--update' == True:
        print(replace_word)
#### You must change the status to any of these three
    statues_change = ("Complete","Incomplete", "In progress")
    if statues_change != True:
        print(f"You must provide one of the following : {statues_change}")

main_task()

