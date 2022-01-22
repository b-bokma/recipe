# Import all the schemas, so that Base has them before being imported by Alembic
# Added NoQA to the lines so linter will skip them

from .base_class import Base  # noqa
# from .tables.ingredients import *  # noqa
# from .tables.measurements import *  # noqa
# from .tables.nutrition import *  # noqa
# from .tables.recipes import *  # noqa
from .tables.users import *  # noqa
