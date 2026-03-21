# from flask import Blueprint, jsonify
from flask import Blueprint, render_template, request, redirect, url_for, request
from app.models.task import Task                                            #importing the Task object
from app.storage.sqlite_manager import get_tasks, save_tasks

#defining the blueprint, handles only URLs with prefix /tasks
# bp = Blueprint("tasks", __name__, url_prefix="/tasks")
bp = Blueprint("hub", __name__, url_prefix="/hub")

def _normalize_task_ids(tasks):
    for idx, t in enumerate(tasks, start=1):
        t["id"] = idx
    return tasks


@bp.route("/tasks", methods=["GET"])
def list_tasks():
    tasks = get_tasks()  # getting the data with the method used before in CLI
    tasks = _normalize_task_ids(tasks)
    save_tasks(tasks)
    return render_template("dashboard.html", tasks=tasks)  # render the HTML template and pass the variable 'tasks' to it

    #OLD VERSION
    #returning it as a JSON (web format)
    # return jsonify(tasks)
@bp.route("/add", methods=["POST"])
def add_task():
    # Get the data from the HTML form
    # title matches the name="title" in the HTML input
    title = request.form.get("title")

    tasks = get_tasks()
    tasks = _normalize_task_ids(tasks)

    # using the same logic as in CLI.py but ID matches position
    new_id = len(tasks) + 1
    new_task = Task.create(title, new_id)

    tasks.append(new_task.to_dict())
    tasks = _normalize_task_ids(tasks)
    save_tasks(tasks)

    return redirect(url_for("hub.list_tasks"))

@bp.route("/complete/<task_id>", methods= ["POST"])
def complete_task(task_id):             #same as in CLI we have similar logic
    tasks = get_tasks()                 #get the tasks
    search_id = int(task_id)
    for t in tasks:                     #find the task in var(tasks)
        if int(t.get("id", 0)) == search_id:
            t['completed'] = True       #mark it as completed
            break
    save_tasks(tasks)                   #save the tasks altogether

    return redirect(url_for("hub.list_tasks"))

@bp.route("/delete/<task_id>", methods=["POST"])
def delete_task(task_id):
    tasks=get_tasks()
    search_id = int(task_id)

    tasks = [t for t in tasks if int(t.get("id", 0)) != search_id]

    tasks = _normalize_task_ids(tasks)
    save_tasks(tasks)

    return redirect(url_for("hub.list_tasks"))

@bp.route("/uncomplete/<task_id>", methods= ["POST"])
def uncomplete_task(task_id):
    tasks = get_tasks()  # get the tasks
    search_id = int(task_id)
    for t in tasks:  # find the task in var(tasks)
        if int(t.get("id", 0)) == search_id:
            t['completed'] = False  # mark it as uncomplete
            break
    save_tasks(tasks)  # save the tasks altogether

    return redirect(url_for("hub.list_tasks"))


@bp.route("/reorder", methods=["POST"])
def reorder_tasks():
    payload = request.get_json(force=True, silent=True)
    if not payload or "order" not in payload:
        return ("Bad Request", 400)

    new_order = [int(i) for i in payload.get("order", [])]
    tasks = get_tasks()

    # build map by id in case tasks are previously unsorted
    task_map = {int(t.get("id", 0)): t for t in tasks}
    reordered = []

    # keep tasks exactly in client order, fallbacks handled with remaining tasks after loop
    for idx, task_id in enumerate(new_order, start=1):
        task = task_map.get(task_id)
        if task:
            task["id"] = idx
            reordered.append(task)

    # append tasks that weren't part of the request at the end
    left_ids = set(new_order)
    for task in tasks:
        tid = int(task.get("id", 0))
        if tid not in left_ids:
            reordered.append(task)

    reordered = _normalize_task_ids(reordered)
    save_tasks(reordered)
    return ("", 204)


@bp.route("/focus_mode/<task_id>", methods=["GET"])
def focus_mode(task_id):
    search_id = int(task_id)
    task = next((t for t in get_tasks() if int(t.get("id", 0)) == search_id), None)  # find the task by id
    time = request.args.get('time', default= 25, type= int)
    if not task:
        return redirect(url_for("hub.list_tasks"))  # if task not found, redirect to task list
    return render_template("focus_mode.html", task=task, time=time)  # render the focus mode template with the task details

@bp.route("/focus_setup", methods= ["GET"])
def focus_setup():
    tasks = get_tasks()
    return render_template("focus_setup.html", tasks=tasks)