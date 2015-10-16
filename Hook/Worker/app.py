from flask import Flask, jsonify, request
import hmac
import hashlib
import json

from rq import Queue
from rq.job import Job, JobStatus
from redis import Redis

from HookTest.test import cmd

app = Flask()

def parse_request(request):
    return request

def check_signature(body, signature, secret):
    """ Check the signature sent by a request with the body

    :param body: Raw body of the request
    :param signature: Signature sent by github
    :param secret: Secret salt

    :return: Security check status
    :rtype: bool
    """
    signature = '{0}'.format(
        hmac.new(
            bytes(secret, encoding="utf-8"),
            body,
            hashlib.sha1
        ).hexdigest()
    )
    if signature == secret:
        return True
    else:
        return False

@app.route("/rest/api/hooktest", methods=["PUT"])
def submit():
    """

    :return:
    """
    code, resp = 401, {"message": "error"}

    if check_signature(request.data, request.headers.get("HookTest-Secure-X"), app.config.secret) :
        code, status = 200, {"message": "queued"}

        data = json.loads(request.data.decode('utf-8'))
        data["secret"] = app.config["secret"]

        redis_conn = Redis(app.config["redis"])
        q = Queue(connection=redis_conn)
        job = q.enqueue_call(
            func=cmd,
            kwargs=data,
            timeout=3600,
            result_ttl=86400
        )
        status["job_id"] = job.get_id()

    response = jsonify(status)
    response.status_code = code
    return response

@app.route("/rest/api/hooktest/<id>", methods=["DELETE"])
def delete():
    """

    :return:
    """
    return jsonify(status="success")

def run(secret="", domain="localhost", debug=False, port=5000, redis="127.0.0.1"):
    app.config["secret"] = secret
    app.config["DOMAIN"] = domain
    app.run(debug=debug, port=port)

if __name__ == "__main__":
    run()