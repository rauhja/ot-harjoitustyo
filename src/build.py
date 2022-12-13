from initialize_database import CreateDatabase


def build():
    """Function to create the database from the invoke command

    """
    CreateDatabase().initialize_database()


if __name__ == "__main__":
    build()
