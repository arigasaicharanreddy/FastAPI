from src.utils.db import get_db
from src.tasks.dtos import TaskSchema, TaskResponseSchema, TaskListResponseSchema
from src.tasks import controller
from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session 
from typing import List


task_routes = APIRouter(prefix = "/tasks")


@task_routes.post("/create", status_code= status.HTTP_201_CREATED)
def create_task(body: TaskSchema, db: Session = Depends(get_db)):
    return controller.create_task(body, db)


@task_routes.get("/all_tasks", response_model = TaskListResponseSchema ) 
def get_all_tasks(db : Session = Depends(get_db)) :
    return controller.get_tasks(db)

@task_routes.get()
