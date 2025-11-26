from dishka.async_container import make_async_container

from app.core.dependencies.base import BaseProvider
from app.core.dependencies.interactors import InteractorsPorivder
from app.core.dependencies.repositories import RepositoriesProvider

container = make_async_container(
    BaseProvider(), RepositoriesProvider(), InteractorsPorivder()
)
