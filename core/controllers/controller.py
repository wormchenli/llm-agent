import os
import uuid
from dataclasses import dataclass

from flask import request
from injector import inject
from openai import OpenAI
from core.services import AppService
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam
from core.schemas.app_schema import CompletionRequest
from utils.responses import ResponseBody, HttpStatusCode

api_key = os.environ.get("API_KEY")
base_url = os.environ.get("BASE_URL")


@inject
@dataclass
class AppController:
    app_service: AppService

    def create_app(self):
        app = self.app_service.create_app()
        res_body = ResponseBody(
            status=HttpStatusCode.SUCCESS,
            data={"app_id": f"{app.id}"},
            message="App created successfully"
        )
        return res_body.to_response()

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        if not app:
            res_body = ResponseBody(
                status=HttpStatusCode.NOT_FOUND,
                data={},
                message="App not found"
            )
            return res_body.to_response()
        else:
            res_body = ResponseBody(
                status=HttpStatusCode.SUCCESS,
                data={
                    "id": f"{app.id}",
                    "name": app.name,
                    "icon": app.icon,
                    "description": app.description
                },
                message="App found successfully"
            )
            return res_body.to_response()

    def update_app(self, id: uuid.UUID):
        data = request.json
        updated = self.app_service.update_app(id, data)
        if updated:
            res_body = ResponseBody(
                status=HttpStatusCode.SUCCESS,
                data={},
                message="App updated successfully"
            )
            return res_body.to_response()
        else:
            res_body = ResponseBody(
                status=HttpStatusCode.FAILURE,
                data={},
                message="Failed to update app"
            )
            return res_body.to_response()

    def delete_app(self, id: uuid.UUID):
        deleted = self.app_service.delete_app(id)
        if deleted:
            res_body = ResponseBody(
                status=HttpStatusCode.SUCCESS,
                data={},
                message="App deleted successfully"
            )
            return res_body.to_response()
        else:
            res_body = ResponseBody(
                status=HttpStatusCode.FAILURE,
                data={},
                message="Failed to delete app"
            )
            return res_body.to_response()

    # delete
    def completion(self):
        query = request.json.get("query")
        reqValidate = CompletionRequest()
        if not reqValidate.validate():
            return reqValidate.errors
        # if not query:
        #     return {"success": False, "msg": "query is required", "data": ""}, 500

        client = OpenAI(api_key=api_key, base_url=base_url)

        # Create properly typed message objects
        system_message: ChatCompletionSystemMessageParam = {
            "role": "system",
            "content": "You are a helpful assistant"
        }
        user_message: ChatCompletionUserMessageParam = {
            "role": "user",
            "content": query
        }

        # Use the properly typed messages
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[system_message, user_message],
            stream=False
        )
        res_data = response.choices[0].message.content

        return {"success": True, "msg": "response completion successfully", "data": res_data}, 200

    def ping(self):
        """
        Ping the server to check if it's alive.
        """
        return {"success": True, "msg": "Pong", "data": "Pong"}, 200
