# from flask import Blueprint, jsonify
from flask import Blueprint, render_template, request, redirect, url_for    #changed jsonify to render_template
from app.models.task import Task                                            #importing the Task object
from app.storage.sqlite_manager import get_tasks, save_tasks

#defining the blueprint, handles only URLs with prefix /tasks
# bp = Blueprint("tasks", __name__, url_prefix="/tasks")
bp = Blueprint("hub", __name__, url_prefix="/hub")

@bp.route("/tasks", methods=["GET"])
def list_tasks():
    tasks = get_tasks() #getting the data with the method used before in CLI
    return render_template("dashboard.html", tasks=tasks) #render the HTML template and pass the variable 'tasks' to it

    #OLD VERSION
    #returning it as a JSON (web format)
    # return jsonify(tasks)
@bp.route("/add", methods=["POST"])
def add_task():
    # Get the data from the HTML form
    # title matches the name="title" in the HTML input
    title = request.form.get("title")

    # using the same logic as in CLI.py
    new_task = Task.create(title)

    # saving the task to the JSON
    tasks = get_tasks()                 #same as in CLI I'm attaching the existing tasks to a variable
    tasks.append(new_task.to_dict())    #then appending the new one from above
    save_tasks(tasks)                   #and saving them altogether

    return redirect(url_for("hub.list_tasks"))

@bp.route("/complete/<task_id>", methods= ["POST"])
def complete_task(task_id):             #same as in CLI we have similar logic
    tasks = get_tasks()                 #get the tasks
    for t in tasks:                     #find the task in var(tasks)
        if t["id"] == task_id:
            t['completed'] = True       #mark it as completed
            break
    save_tasks(tasks)                   #save the tasks altogether

    return redirect(url_for("hub.list_tasks"))

@bp.route("/delete/<task_id>", methods=["POST"])
def delete_task(task_id):
    tasks=get_tasks()

    tasks = [t for t in tasks if t["id"] != task_id]

    save_tasks(tasks)

    return redirect(url_for("hub.list_tasks"))

@bp.route("/uncomplete/<task_id>", methods= ["POST"])
def uncomplete_task(task_id):
    tasks = get_tasks()  # get the tasks
    for t in tasks:  # find the task in var(tasks)
        if t["id"] == task_id:
            t['completed'] = False  # mark it as uncomplete
            break
    save_tasks(tasks)  # save the tasks altogether

    return redirect(url_for("hub.list_tasks"))

@bp.route("/focus_mode/<task_id>", methods=["GET"])
def focus_mode(task_id):
    task = next((t for t in get_tasks() if t["id"] == task_id), None)  # find the task by id

    if not task:
        return redirect(url_for("hub.list_tasks"))  # if task not found, redirect to task list
    return render_template("focus_mode.html", task=task)  # render the focus mode template with the task details