from app.models.task import Task
from app.storage.sqlite_manager import save_tasks, get_tasks
import argparse

#to run the command in the CLI use: "python CLI.py {argument} + "{additional task_name/id}"
def main():
    parser = argparse.ArgumentParser(
        description="YourHub CLI – manage tasks and notes"
    )
    subparsers = parser.add_subparsers(dest="command")

    #<--------------KOMENDY-------------->
    # add-task command
    add_task_parser = subparsers.add_parser("add-task")
    add_task_parser.add_argument("title", help="Task title")

    #delete-task command 
    delete_task_parser=subparsers.add_parser("delete-task")
    delete_task_parser.add_argument("task_id", help="ID of the task to delete")

    #complete-task command
    complete_task_parser = subparsers.add_parser("complete-task")
    complete_task_parser.add_argument("task_id", help="ID of the task to complete")

    #uncomplete-task command
    uncomplete_task_parser = subparsers.add_parser("uncomplete-task")
    uncomplete_task_parser.add_argument("task_id", help="ID of the task to uncomplete")

    # list-tasks command
    subparsers.add_parser("list-tasks")

    args = parser.parse_args()

    print(args)

    # <--------------LOGIKA-------------->
    if args.command == "add-task":          #if the user typed list-task in the CLI -> run this block
        new_task = Task.create(args.title)

        tasks = get_tasks()                 #we are getting the tasks from the JSON file
        tasks.append(new_task.to_dict())    #adding the new task to the dictionary
        save_tasks(tasks)                   #and saving it all together

    elif args.command == "list-tasks":      #if the user typed list-task in the CLI -> run this block
        tasks=get_tasks()

        if not tasks:                       #if file "data.JSON" has no tasks -> "No tasks found"
            print("No tasks found.")
            return

        print("\nListing tasks:")
        for t in tasks:                                     #pritns out each task with the status ✔ / ✗ depending on completion
            status = "✔" if t["completed"] else "✗"         # <---stąd
            print(f"[{status}] {t['id']} — {t['title']}")   #{status} zapożyczony wyżej, {id}, {nazwa taska}

    elif args.command == "delete-task":
        tasks= get_tasks()
        before= len(tasks)

        tasks= [t for t in tasks if t["id"] != args.task_id]    #overwrites the {tasks} by IDs that are not like the ones given 1ST STEP
        if len(tasks) == before:                                #asseses whether the updated local data is similar to the one before
            print("Task not found")                             #if the data hasn't changed the overwriting doesn't occur
        else:
            save_tasks(tasks)                                   #applies the changes made above to the JSON file 2ND STEP
            print("Task succesfully deleted!")

    elif args.command == "complete-task":
        tasks=get_tasks()
        found= False

        for t in tasks:
            if t["id"] == args.task_id:
                if t["completed"]:
                    print("Task already completed!")
                    return
                t['completed']=True
                found= True
                break
        if found:
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Task not found.")

    elif args.command == "uncomplete-task":
        tasks= get_tasks()
        found= False

        for t in tasks:
            if t["id"] == args.task_id:
                if not t["completed"] :
                    print("Choose a completed task!")
                    return
                t['completed']=False
                found= True
                break
        if found:
            save_tasks(tasks)
            print("Task marked as uncompleted!")
        else:
            print("Task not found.")

if __name__ == "__main__":
    main()