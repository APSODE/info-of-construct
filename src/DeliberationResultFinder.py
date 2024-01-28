from typing import Optional, Union, Literal, Dict, List

from requests import Session, Response
from bs4 import BeautifulSoup
from bs4.element import PageElement, Tag

from dto.ResultData import ResultData
from dto.SearchData import SearchData

_PAYLOAD_TYPING = Dict[
    Union[
        Literal["rr_const_type"],
        Literal["rr_const_detail_type"],
        Literal["searchField"],
        Literal["searchKeyWord"],
        Literal["page"]
    ],
    str
]


class DeliberationResultFinder:
    def __init__(self):
        self._site_url = "https://partner.lh.or.kr/deliberate/deliberate_r.asp"
        self._search_request_url = "https://partner.lh.or.kr/deliberate/deliberate_innerList.asp"
        self._result_view_request_url = "https://partner.lh.or.kr/deliberate/deliberate_innerView.asp"
        self._session = self._create_session()

    @staticmethod
    def create_finder():
        return DeliberationResultFinder()

    @staticmethod
    def _create_session() -> Session:
        session = Session()
        return session

    @staticmethod
    def _replace_element_text(element: Union[Tag, PageElement]) -> str:
        return element.text.replace(
            "\n", ""
        ).replace(
            "\t", ""
        ).replace(
            "\r", ""
        ).replace(
            "\xa0", " "
        )

    @staticmethod
    def _get_site_html(site_response: Response) -> Optional[BeautifulSoup]:
        if site_response.ok:
            return BeautifulSoup(
                site_response.text,
                "html.parser"
            )
        else:
            raise ConnectionError()

    @staticmethod
    def _create_search_payload(search_keyword: str, page_num: int) -> _PAYLOAD_TYPING:
        return {
            "rr_const_type": "",
            "rr_const_detail_type": "",
            "searchField": "",
            "searchKeyWord": f"{search_keyword}",
            "page": page_num
        }

    @staticmethod
    def _create_result_view_payload(data_number: int) -> Dict[Literal["rr_idx"], int]:
        return {"rr_idx": data_number}

    def search(self, search_keyword: str, page_num: int = 1) -> List[SearchData]:
        search_response = self._session.post(
            url = self._search_request_url,
            data = self._create_search_payload(search_keyword = search_keyword, page_num = page_num)
        )

        search_response_html = self._get_site_html(site_response = search_response).find(
            "tbody", {"id": "tb_result"}
        ).find_all(
            "tr", {"class": "View"}
        )

        search_result_dtos = []

        for search_results_html in search_response_html:
            search_result_dtos.append(
                SearchData.serialize_data(
                    search_result_html = search_results_html.find_all("td")
                )
            )

        return search_result_dtos

    def get_result_view(self, data_number: int) -> ResultData:
        result_view_response = self._session.post(
            url = self._result_view_request_url,
            data = self._create_result_view_payload(data_number = data_number)
        )

        result_view_form_elements = self._get_site_html(
            site_response = result_view_response
        ).find(
            "tbody"
        ).find_all(
            "td"
        )

        return ResultData.serialize_data(
            result_view_html = result_view_form_elements
        )




