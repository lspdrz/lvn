from datetime import datetime
from io import StringIO
from typing import TextIO, Dict, List, Union

from pianosdk.api_response import ApiResponse
from pianosdk.base_api import BaseApi
from pianosdk.configuration import Configuration
from pianosdk.httpwrap import HttpCallBack
from pianosdk.utils import _json_deserialize, _encode_parameter


class PublisherAuditApi(BaseApi):
    def __init__(self, config: Configuration, http_callback: HttpCallBack = None) -> None:
        super().__init__(config, http_callback)

    def get_audit(self, aid: str = None, uid: str = None, action_type: str = None, _from: str = None, until: str = None, limit: int = None, offset: int = None, api_token: str = None) -> ApiResponse[Dict]:
        _url_path = '/id/api/v1/publisher/audit/user'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {
            'aid': _encode_parameter(aid),
            'uid': _encode_parameter(uid),
            'action_type': _encode_parameter(action_type),
            'from': _encode_parameter(_from),
            'until': _encode_parameter(until),
            'limit': _encode_parameter(limit),
            'offset': _encode_parameter(offset),
            'api_token': _encode_parameter(api_token)
        }

        _headers = {
            'api_token': self.config.api_token,
            'Accept': 'application/json'
        }

        _parameters = {

        }

        _body = None
        _files = None

        _request = self.config.http_client.build_request('GET',
                                                         _query_url,
                                                         headers=_headers,
                                                         query_parameters=_query_parameters,
                                                         parameters=_parameters,
                                                         json=_body,
                                                         files=_files)
        _response = self._execute_request(_request)
        _result = _json_deserialize(_response)
        return _result

