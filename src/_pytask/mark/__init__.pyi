from pathlib import Path
from typing import Any
from typing_extensions import deprecated
from _pytask.mark.expression import Expression
from _pytask.mark.expression import ParseError
from _pytask.mark.structures import Mark
from _pytask.mark.structures import MarkDecorator
from _pytask.tree_util import PyTree

from _pytask.session import Session
import networkx as nx

def select_by_after_keyword(session: Session, after: str) -> set[str]: ...
def select_by_keyword(session: Session, dag: nx.DiGraph) -> set[str]: ...
def select_by_mark(session: Session, dag: nx.DiGraph) -> set[str]: ...

class MarkGenerator:
    @deprecated(
        "'@pytask.mark.produces' is deprecated starting pytask v0.4.0 and will be removed in v0.5.0. To upgrade your project to the new syntax, read the tutorial on product and dependencies: https://tinyurl.com/pytask-deps-prods.",  # noqa: E501
        category=FutureWarning,
        stacklevel=1,
    )
    @staticmethod
    def produces(objects: PyTree[str | Path]) -> None: ...
    @deprecated(
        "'@pytask.mark.depends_on' is deprecated starting pytask v0.4.0 and will be removed in v0.5.0. To upgrade your project to the new syntax, read the tutorial on product and dependencies: https://tinyurl.com/pytask-deps-prods.",  # noqa: E501
        category=FutureWarning,
        stacklevel=1,
    )
    @staticmethod
    def depends_on(objects: PyTree[str | Path]) -> None: ...
    @deprecated(
        "'@pytask.mark.task' is deprecated starting pytask v0.4.0 and will be removed in v0.5.0. Use '@task' from 'from pytask import task' instead.",  # noqa: E501
        category=FutureWarning,
        stacklevel=1,
    )
    @staticmethod
    def task(
        name: str | None = None,
        *,
        id: str | None = None,  # noqa: A002
        kwargs: dict[Any, Any] | None = None,
        produces: PyTree[Any] | None = None,
    ) -> None: ...
    def __getattr__(self, name: str) -> MarkDecorator | Any: ...

MARK_GEN = MarkGenerator()

__all__ = [
    "Expression",
    "MARK_GEN",
    "Mark",
    "MarkDecorator",
    "MarkGenerator",
    "ParseError",
    "select_by_keyword",
    "select_by_mark",
    "select_by_after_keyword",
]
