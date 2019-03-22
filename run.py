"""Application entry point"""
from project.views.home_route import app

if __name__ == "__main__":
    app.run(debug=True)