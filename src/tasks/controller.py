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

def get_one_task(db : Session):
    