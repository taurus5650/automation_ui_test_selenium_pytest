import json

from logger import Logger
import allure
import requests
import textwrap


class ApiRequest:
    logger = Logger.setup_logger()

    def __int__(self, waiting_time=None):
        self.waiting_time = waiting_time
        self.request_session = requests.Session
        self.logger = self.logger

    @allure.step("[{method}] {url}]")
    def _send_request(self, method: str, url: str, **kwargs):
        acceptable_waiting_time = kwargs.pop(
            "waiting_time", None
        ) or self.waiting_time

        try:
            response = self.request_session.request(method, url, **kwargs)
            self._debug_log(response)
            duration = response.elapsed.total_seconds()
            assert duration <= acceptable_waiting_time, (
                f"Response Time > {acceptable_waiting_time}s, Cost: {duration}s"
            )
        except requests.exceptions.RequestException as e:
            response = None
            self.logger.error(
                f"Request Error > url: [{method}] {url}, kwargs: {kwargs}, error: {str(e)}")
        return response

    def _debug_log(self, response: requests.Response):
        request_body = response.request.body
        if request_body:
            request_body = json.loads(request_body)

        try:
            result = json.dumps(response.json(), indent=4, ensure_ascii=False)
        except json.JSONDecodeError:
            result = response.text

        def format_header(x): return "\n".join(
            f"{key}: {val}" for key, val in x.items()
        )

        self.logger.debug(textwrap.dedent('''
                    ---------------- request ----------------
                    {request.method} {request.url}
                    {request_header}
                    Request Body :
                    {request_body}
                    ---------------- response ----------------
                    {resp.status_code} {resp.reason} {resp.url}
                    {resp_header}
                    Duration : {resp_duration}
                    Response Context :
                    {resp_result}
                    ''').format(
            request=response.request,
            request_body=json.dumps(request_body, indent=4, ensure_ascii=False),
            resp=response,
            resp_result=result,
            resp_duration=response.elapsed.total_seconds(),
            request_header=format_header(response.request.headers),
            resp_header=format_header(response.headers),
        ))
