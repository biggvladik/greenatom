
from fastapi.testclient import TestClient
from app import app
from database import Inbox
from settings import setting
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from schemas import test_picture



client = TestClient(app)

def test_get_picture():
    session = Session(bind=create_engine(setting.database_url))

    random_uuid = session.query(Inbox.name, Inbox.code_id, Inbox.created_on).first()

    res = test_picture.parse_obj(random_uuid)

    random_uuid = res.code_id
    results = {
      "name": res.name,
      "created_on": res.created_on.strftime("%Y-%m-%dT%H:%M:%S.%f")
    }
    response = client.get(f"/frames/{random_uuid}")
    assert response.status_code == 200
    assert response.json() == results

