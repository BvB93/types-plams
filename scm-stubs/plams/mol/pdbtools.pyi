from typing import List, Any, IO

class PDBRecord:
    name: str
    value: List[str]
    model: List[Any]
    def __init__(self, s: str) -> None: ...
    def __str__(self) -> str: ...
    def is_multiline(self) -> bool: ...
    def extend(self, s: str) -> bool: ...

class PDBHandler:
    records: Dict[str, List[PDBRecord]]
    def __init__(self, textfile: Union[None, str, IO[str]] = ...) -> None: ...
    def singlemodel(self) -> bool: ...
    def read(self, f: IO[str]) -> None: ...
    def write(self, f: IO[str]) -> None: ...
    def calc_master(self) -> PDBRecord: ...
    def check_master(self) -> bool: ...
    def get_models(self) -> List[List[Any]]: ...
    def add_record(self, record: PDBRecord) -> None: ...
    def add_model(self, model: List[PDBRecord]) -> None: ...
