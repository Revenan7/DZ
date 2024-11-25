from fastapi import APIRouter, Depends;
from sqlalchemy.orm import Session;
from database import get_db;
from services import user as UserService;
from DTO import user as UserDTO;
from models import user;
from typing import List;


router = APIRouter();

@router.post('/', tags=["user"])
async def create(data: UserDTO.User, db: Session = Depends(get_db)):
    #Создать пользователя
    return UserService.create_user(data, db);

@router.get('/{id}', tags=["user"])
async def get(id: int, db: Session = Depends(get_db)):
    #Получить пользователя по ID
    return UserService.get_user(id, db);

@router.put('/{id}', tags=["user"])
async def update(id: int, data: UserDTO.User, db: Session = Depends(get_db)):
    #Обновить данные пользователя
    return UserService.update(data, db, id);

@router.delete('/{id}', tags=["user"])
async def delete(id: int, db: Session = Depends(get_db)):
    #Удалить пользователя по ID
    return UserService.remove(db, id);

@router.get('/', tags =["test"])
async def get_all(db: Session = Depends(get_db)):
    #Ну короче всё вывести
    return UserService.get_all(db);
