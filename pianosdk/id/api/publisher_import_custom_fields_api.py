from datetime import datetime
from io import StringIO
from typing import TextIO, Dict, List, Union

from pianosdk.api_response import ApiResponse
from pianosdk.base_api import BaseApi
from pianosdk.configuration import Configuration
from pianosdk.httpwrap import HttpCallBack
from pianosdk.utils import _json_deserialize, _encode_parameter
from pianosdk.id.models.import_cf_result import ImportCFResult


class PublisherImportCustomFieldsApi(BaseApi):
    def __init__(self, config: Configuration, http_callback: HttpCallBack = None) -> None:
        super().__init__(config, http_callback)

    def import_cf(self, authorization: str = None, aid: str = None, header_size: int = None, body: Union[TextIO, StringIO, None] = None) -> ApiResponse[ImportCFResult]:
        _url_path = '/id/api/v1/publisher/import/customFields/history'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {
            'aid': _encode_parameter(aid),
            'header_size': _encode_parameter(header_size)
        }

        _headers = {
            'Authorization': authorization,
            'api_token': self.config.api_token,
            'Accept': 'application/json'
        }

        _parameters = {

        }

        _body = None
        _files = {
            'file': body
        }

        # Dirty hack for uploading file content API
        _query_parameters.update(**_parameters)
        _parameters = {}
        _request = self.config.http_client.build_request('POST',
                                                         _query_url,
                                                         headers=_headers,
                                                         query_parameters=_query_parameters,
                                                         parameters=_parameters,
                                                         json=_body,
                                                         files=_files)
        _response = self._execute_request(_request)
        _result = _json_deserialize(_response, ImportCFResult)
        return _result

