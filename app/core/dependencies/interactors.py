from dishka import Provider, provide, Scope

from app.application.interactors.general.get_contact_info import (
    GetContactInfoInteractor,
)
from app.application.interactors.user.create import CreateUserInteractor

from app.application.interactors.house.get_by_id import GetHouseByIdInteractor
from app.application.interactors.house.get_list import GetHouseListInteractor


class InteractorsPorivder(Provider):
    scope = Scope.REQUEST

    # USERS
    create_user = provide(CreateUserInteractor)

    # HOUSES
    get_house_list = provide(GetHouseListInteractor)
    get_house_by_id = provide(GetHouseByIdInteractor)

    # GENERAL
    get_settings = provide(GetContactInfoInteractor)
