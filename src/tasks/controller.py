from src.tasks.dtos import TaskSchema
from src.tasks.models import TaskModel

from sqlalchemy.orm import Session
from fastapi import HTTPException


""" To create a new task"""

def create_task(body : TaskSchema, db : Session):
    data = body.model_dump()
    new_task = TaskModel(title = data["title"], description = data["description"], is_completed = data["is_completed"])
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    
    return {"status" : "Task created successfully" , "data" : new_task}


"""To retrieve tasks"""

def get_tasks(db:Session):
    tasks = db.query(TaskModel).all()
    return {"status": "All Tasks", "data" : tasks}


"""to retrieve one task """

def get_one_task(task_id : int, db:Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task :
        raise HTTPException(status_code = 404, detail = "Task not found")
    return {"status" : "Task Fetched", "data" : one_task}
    
    
""" TO UPDATE TASK """
    
def update_task(body : TaskSchema, task_id : int, db : Session) :
    one_task = db.query(TaskModel).get(task_id)
    if not one_task :
        raise HTTPException(status_code = 404, detail = "Task not found")
        
    body = body.model_dump()
    for field, value in body.items():
        setattr(one_task, field, value)        
        
    db.add(one_task)
    db.commit()
    db.refresh(one_task)
    
    return {"status" : "Updated the Value", "data" : one_task}
    
    
""" To delete Task """

def delete_task(task_id : int, db : Session) :
    one_task = db.query(TaskModel).get(task_id)
    if not one_task :
        raise HTTPException(status_code = 404, detail = "Task not found")
    db. delete(one_task)
    db.commit()
    return {"status" : "Deleted the Task", "data" : one_task}