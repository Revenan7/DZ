from models.user import User as UserModel  ;
from sqlalchemy.orm import Session;
from DTO.user import User as UserDTO;  


def create_user(data: UserDTO, db: Session):
    #Создать пользователя в базе данных
    new_user = UserModel(name=data.name); 

    try:
        db.add(new_user);
        db.commit();
        db.refresh(new_user);
    except Exception as e:
        print(f"Ошибка при создании пользователя: {e}");
        raise;
    return new_user;



def get_user(id: int, db: Session):
    #Получить пользователя по ID
    try:
        return db.query(UserModel).filter(UserModel.id == id).first();
    except Exception as e:
        print(f"Ошибка при получении пользователя с ID {id}: {e}");
        raise;


def update(data: UserDTO, db: Session, id: int):
    #Обновить данные пользователя
    user = db.query(UserModel).filter(UserModel.id == id).first();

    if not user:
        raise ValueError(f"Пользователь с ID {id} не найден");

    user.name = data.name;

    try:
        db.add(user) ;
        db.commit();
        db.refresh(user);
    except Exception as e:
        print(f"Ошибка при обновлении пользователя с ID {id}: {e}");
        raise;

    return user;


def remove(db: Session, id: int):
    #Удалить пользователя по ID
    try:
        user = db.query(UserModel).filter(UserModel.id == id).first();

        if not user:
            raise ValueError(f"Пользователь с ID {id} не найден");

        db.delete(user);
        db.commit();
    except Exception as e:
        print(f"Ошибка при удалении пользователя с ID {id}: {e}");
        raise;

    return {"message": f"Пользователь с ID {id} успешно удалён"};

def get_all(db: Session):
    #Всё выводит
    return db.query(UserModel).all();