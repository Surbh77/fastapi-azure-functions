import azure.functions as func
import logging
from fastapi import FastAPI
from WrapperFunction import app as fastapi_app


app = FastAPI()


# def fastapi_sam(req: func.HttpRequest) -> func.HttpResponse:
#     return func.AsgiMiddleware(app).handle(req)
#     logging.info('Python HTTP trigger function processed a request.')


app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)
# app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


# @app.route(route="fastapi_sam")
# def fastapi_sam(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')
#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')
#     if name:
#         return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#              status_code=200
#         )