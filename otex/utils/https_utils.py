from typing import Literal, Any
from dataclasses import dataclass

@dataclass
class Call:
    url: str # URL to which HTTP call will be made
    http_method: Literal["POST", "GET"] 
    body: dict # body of HTTP request
    attribute: str # a
    detail: dict

@dataclass
class Response:
    result: Any
    attribute: str
    detail: dict