

#  TODO: For later use
# def get_training_programs():
#     with sqlite3.connect(Connection.db_path) as conn:
#         conn.row_factory = model_factory(TrainingProgram)
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         SELECT tp.id, tp.name,
#         tp.description,
#         tp.start_date,
#         tp.end_date,
#         tp.max_num
#         FROM hrapp_trainingprogram tp;
#         """)

#         return db_cursor.fetchall()
