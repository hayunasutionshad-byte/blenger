import os
from flask import Flask, request, Response
import requests

app = Flask(__name__)

TARGET = "https://bot-api.junofficial.biz.id"

@app.route("/", defaults={"path": ""}, methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"])
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"])
def proxy(path):
    url = f"{TARGET}/{path}"

    # Forward the incoming query string and request body.
    headers = {
        key: value
        for key, value in request.headers
        if key.lower() not in {"host", "content-length"}
    }

    try:
        upstream = requests.request(
            method=request.method,
            url=url,
            params=request.args,
            data=request.get_data(),
            headers=headers,
            cookies=request.cookies,
            allow_redirects=False,
            timeout=30,
        )

        excluded = {"content-encoding", "content-length", "transfer-encoding", "connection"}
        response_headers = [
            (key, value)
            for key, value in upstream.headers.items()
            if key.lower() not in excluded
        ]

        return Response(
            upstream.content,
            status=upstream.status_code,
            headers=response_headers,
        )

    except requests.RequestException as exc:
        return {"error": "Upstream API request failed", "detail": str(exc)}, 502


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
