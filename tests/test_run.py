from unittest.mock import patch

import mongomock
from fastapi.testclient import TestClient

from config import DB_NAME_TEST, DB_COLLECTION_NAME_TEST, DB_HOST_TEST, DB_PORT_TEST
from db.mongo import default_rows
from fastapi_app.run import app
from fastapi_app.models.validators import DEFAULT_RESPONSE, MSG_PHONE_NUM_INVALID_LEN
from fastapi_app.models.validators import MSG_PHONE_NUM_INVALID_CODE, MSG_EMAIL_INVALID, MSG_DATE_INVALID
from .testcases import testcases_valid, responses_valid, testcases_date_invalid
from .testcases import testcases_email_invalid, testcases_default_response

client = TestClient(app)


def test_get_form():
    db_client_test = mongomock.MongoClient(f'mongodb://{DB_HOST_TEST}:{DB_PORT_TEST}/')
    current_db_test = db_client_test[DB_NAME_TEST]
    current_db_test.drop_collection(DB_COLLECTION_NAME_TEST)
    collection_test = current_db_test[DB_COLLECTION_NAME_TEST]
    collection_test.insert_many(default_rows)

    with patch("fastapi_app.run.collection", collection_test):
        for testcase, test_response in zip(testcases_valid, responses_valid):
            response = client.post("/get_form/", params=testcase)
            assert response.status_code == 200
            assert response.json() == test_response

        for testcase in testcases_date_invalid:
            response = client.post("/get_form/", params=testcase)
            assert response.status_code == 400
            assert response.json() == {"detail": MSG_DATE_INVALID}

        for testcase in testcases_email_invalid:
            response = client.post("/get_form/", params=testcase)
            assert response.status_code == 400
            assert response.json() == {"detail": MSG_EMAIL_INVALID}

        for testcase in testcases_default_response:
            response = client.post("/get_form/", params=testcase)
            assert response.status_code == 400
            assert response.json() == DEFAULT_RESPONSE

        response = client.post("/get_form/", params={"phone_num": "700000"})
        assert response.status_code == 400
        assert response.json() == {"detail": MSG_PHONE_NUM_INVALID_LEN}

        response = client.post("/get_form/", params={"phone_num": "90000000000"})
        assert response.status_code == 400
        assert response.json() == {"detail": MSG_PHONE_NUM_INVALID_CODE}
