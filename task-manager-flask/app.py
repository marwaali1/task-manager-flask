from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []  


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=["POST"])
def add_task():
    title = request.form.get("task")  
    if title != "": 
        newtask = {"id": len(tasks) + 1, "title": title, "done": False}
        tasks.append(newtask)  
    return redirect(url_for("index"))  


@app.route('/done/<int:task_id>')
def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True 
            break
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    for task in tasks:
        if task["id"]==task_id:
            tasks.remove(task)
            break
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
