from uuid import uuid4
from models import MainRecordDao, SoftDeleteDao

# Environment Notes
# Tested using AWS RDS with same resulting exception on all engines.
# Engines: 
# - 5.7.mysql_aurora.2.10.2 
# - mysql_5.7.38
# - mysql_8.0.28

main_record = MainRecordDao.create({'id': uuid4()})  # <-- SQL syntax error if None is provided to create(); workaround by generating uuid here.
related = SoftDeleteDao.create({'main_record_id': main_record.id})

related.delete()  # <-- QueryException
