# компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, DateTime, Integer, ForeignKey
# импортируем модуль для связки таблиц
from sqlalchemy.orm import relationship, backref
# класс конструктор для работы с декларативным стилем работы SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
# импортируем модель продуктов для связки моделей
from models.product import Products

# инициализация декларативного стиля
Base = declarative_base()


class Order(Base):
    