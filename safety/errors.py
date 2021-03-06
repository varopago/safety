class DatabaseFetchError(Exception):
    pass


class DatabaseFileNotFoundError(DatabaseFetchError):
    pass


class InvalidKeyError(DatabaseFetchError):
    pass


class TooManyRequestsError(DatabaseFetchError):
    pass
