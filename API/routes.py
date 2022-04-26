"""
Empty module docstring
"""
from API import app


@app.route('/api/v1', methods=['GET'])
@app.route('/', methods=['GET'])
def api_home() -> str:
    """Handles get requests to /api/v1 route

    Returns
    -------
    str:
        A string showing the welcome message : 'Hello from flask e-commerce api!'
    """

    return "Hello from flask e-commerce api!", 200