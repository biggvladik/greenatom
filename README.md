
---
  - get - получаем имя файла и дату его создания по UUID
  - post - создаем корзину(YYYY-MM-DD) в minio загружаем туда файлы и добавляем информацию о них в БД
  - delete - удаляем файлы из minio и БД по UUID

      ![image](https://user-images.githubusercontent.com/65870349/175832322-74539a48-6b45-4128-a4b8-35a4a9d52b4c.png)



---

# Installation
- install requirements
- change settings.py
- uvicorn app:app --reload
 
