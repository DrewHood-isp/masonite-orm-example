"""BuildNewDb Migration."""

from masoniteorm.migrations import Migration


class BuildNewDb(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("main_records") as table:
            table.uuid('id')
            table.primary('id')

            table.timestamps()

        with self.schema.create("softdelete_records") as table:
            table.uuid('id')
            table.primary('id')

            table.uuid("main_record_id")
            table.foreign("main_record_id").references("id").on("main_records")

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop_table_if_exists("main_records")
        self.schema.drop_table_if_exists("softdelete_records")
