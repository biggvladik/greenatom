from fastapi.testclient import TestClient
from main import app
from database import Inbox,database_url
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from schemas import test_picture



client = TestClient(app)

def test_get_picture():
    session = Session(bind=create_engine(database_url))

    picture = session.query(Inbox.name, Inbox.code_id, Inbox.created_on).first()

    res = test_picture.parse_obj(picture)

    random_uuid = res.code_id
    results = {
      "name": res.name,
      "created_on": res.created_on.strftime("%Y-%m-%dT%H:%M:%S.%f")
    }
    response = client.get(f"/frames/{random_uuid}")
    assert response.status_code == 200
    assert response.json() == results



def test_delete_picture():
    session = Session(bind=create_engine(database_url))

    picture = session.query(Inbox.name, Inbox.code_id, Inbox.created_on).first()
    res = test_picture.parse_obj(picture)

    random_uuid = res.code_id

    response = client.delete(
        f"/frames/{random_uuid}"
    )

    delete_picture = session.query(Inbox.name, Inbox.code_id, Inbox.created_on).filter(Inbox.code_id == random_uuid).all()

    assert response.status_code == 200
    assert delete_picture == []
    assert response.json() == {}
    old_picture = Inbox(
        code_id = res.code_id,
        name =  res.name,
        created_on =  res.created_on
    )
    session.add(old_picture)
    session.commit()

# post не получилось затестить ( не понял как писать для UploadFile тесты )




