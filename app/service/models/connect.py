class SessionHandler:
    def __init__(self, session_maker):
        self.session = None
        self.session_maker = session_maker

    def __enter__(self):
        """It's invoking ``connect`` method to create the connection"""
        self.session = connect(self.session_maker)
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        """It's invoking ``close`` method to close the connection"""
        close(self.session)


def connect(session_maker):
    """Create DB connection object"""
    return session_maker()


def close(session):
    if session is not None:
        """Close DB connection"""
        session.close()
