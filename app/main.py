from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db
import math
from fastapi import HTTPException, status
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Car API!"}

@app.get("/cars/", response_model=List[schemas.CarResponse])
def get_cars(page: int = 1, page_size: int = 10, min_year: int = None, max_year: int = None, db: Session = Depends(get_db)):
    try:

        query = db.query(models.Car)

        # Aplicar filtros por año
        if min_year:
            query = query.filter(models.Car.year >= min_year)
        if max_year:
            query = query.filter(models.Car.year <= max_year)
            

        # Contar el total de autos que cumplen con los filtros
        total_items = query.count()

        # Si no hay autos, devolvemos un 404
        if total_items == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No cars found")

        # Aplicar paginación
        query = query.offset((page - 1) * page_size).limit(page_size)
        cars = query.all()

        return cars

    except HTTPException:
        
        raise

    except Exception as e:
        
        print(f"Error inesperado: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An error occurred: {str(e)}")


@app.post("/cars/", response_model=dict)
def create_cars(cars: List[schemas.CarCreate], db: Session = Depends(get_db)):
    # Verificar si la lista de autos está vacía
    if len(cars) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No car data provided")

    # Contador de registros añadidos
    added_records = 0

    try:
        # Agregar cada auto a la base de datos
        for car_data in cars:
            car = models.Car(**car_data.dict())  # Convertir de Pydantic a SQLAlchemy
            db.add(car)
            added_records += 1

        # Guardar cambios en la base de datos
        db.commit()

        # Contar el total de registros después de la inserción
        total_records = db.query(models.Car).count()

        return {"added_records": added_records, "total_records": total_records}

    except Exception as e:
        db.rollback()  # Revertir cambios en caso de error
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An error occurred: {str(e)}")