from .Users import Users, User

users = Users("database.db", "users")

__all__ = ("Users", "User", "users")
