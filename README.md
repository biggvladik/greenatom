
---
  - get /frames{file_uuid} - получаем имя файла и дату его создания по UUID
  - post /frames - создаем корзину(YYYY-MM-DD) в minio загружаем туда файлы и добавляем информацию о них в БД ( Сделал его защищенным )
  - delete /frames{file_uuid} - удаляем файлы из minio и БД по UUID
  - post /token - создаем JWT token
  - post /users - регистрируем нового пользователя и добавляем его в БД
  
  
  
  

      ![image](https://user-images.githubusercontent.com/65870349/176893442-ee46bb78-d7ad-428b-a036-3283cfc930ee.png)






---

# Installation
- pip install -r requirements.txt
- change settings.py
- run database.py
- uvicorn app:app --reload
 
