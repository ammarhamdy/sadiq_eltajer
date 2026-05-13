from typing import TypeAlias
from model.Areas import Areas
from model.Cities import Cities
from model.Classifications import Classifications
from model.Neighborhoods import Neighborhoods
from model.Types import Types


AliveEntity: TypeAlias = (
    Areas
    | Cities
    | Neighborhoods
    | Types
    | Classifications
)