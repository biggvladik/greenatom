
---
  - get - получаем имя файла и дату его создания по UUID
  - post - создаем корзину(YYYY-MM-DD) в minio загружаем туда файлы и добавляем информацию о них в БД
  - delete - удаляем файлы из minio и БД по UUID






# Installation
- install requirements
- change settings.py
- uvicorn app:app --reload
 
