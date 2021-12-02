# Import all the models, so that Base has them before being imported by Alembic
# Added NoQA to the lines so linter will skip them

from app.db.base_class import Base  # noqa
from app.db.tables.users import *  # noqa
from app.db.tables.ingredients import *  # noqa
from app.db.tables.measurements import *  # noqa
from app.db.tables.nutrition import *  # noqa
from app.db.tables.recipes import *  # noqa
