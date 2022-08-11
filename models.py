from datetime import datetime, timezone
from typing import List

from masoniteorm.models import Model
from masoniteorm.relationships import has_many, belongs_to
from masoniteorm.scopes import UUIDPrimaryKeyMixin, SoftDeletesMixin


class MainRecordDao(Model, UUIDPrimaryKeyMixin):
    __uuid_version__ = 4
    __table__ = "main_records"

    @has_many('id', 'main_record_id')
    def softdelete_records(self):
        return SoftDeleteDao


class SoftDeleteDao(Model, UUIDPrimaryKeyMixin, SoftDeletesMixin):
    __uuid_version__ = 4
    __table__ = "softdelete_records"

    @belongs_to('main_record_id', 'id')
    def main_record(self):
        return MainRecordDao