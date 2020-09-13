"""API endpoint to increment website page_views and report count back"""
import boto3
from fastapi import FastAPI
import uvicorn
from mangum import Mangum
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

dynamodb = boto3.resource('dynamodb', region_name="af-south-1")

table = dynamodb.Table('russ-website-stats')

app = FastAPI(title="DynamoDB API", version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*'],
)

class Visitors(BaseModel):
    """Visitors response model"""
    page_views: int

@app.get('/', response_model=Visitors)
def get_page_views_count():
    """Increments page_views count and then returns it back"""
    table.update_item(
        Key={
            'id': 1
        },
        UpdateExpression="SET page_views = if_not_exists(page_views, :start) + :inc",

        ExpressionAttributeValues={
            ':inc': 1,
            ':start': 0,
        },
        ReturnValues="UPDATED_NEW"
    )

    response = table.get_item(
        Key={
            'id': 1
        }
    )
    item = response['Item']
    return {'page_views': int(item['page_views'])}

dynamo_api = Mangum(app)

if __name__ == '__main__':
    uvicorn.run(app)
