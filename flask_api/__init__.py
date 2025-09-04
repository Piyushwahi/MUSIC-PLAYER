from .app import create_app

app = create_app()   # create the Flask app here

__all__ = ["app"]
