from fastapi import FastAPI, Depends, Response, status

from db.mongo import collection
from fastapi_app.models.validators import FormModel, DEFAULT_RESPONSE

app = FastAPI()


@app.post("/get_form/", status_code=200)
async def get_form(response: Response, params: FormModel = Depends()):
    search_form = {key: value for key, value in params if value}

    if not search_form:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return DEFAULT_RESPONSE

    found = [*collection.aggregate([{"$match": search_form}, {"$project": {'_id': False}}])]

    return found if found else DEFAULT_RESPONSE
