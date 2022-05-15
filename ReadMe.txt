1) To create the proper python environment for this flask run a virtual environment.
2) Create a venv in the directory where this script will run, with either
    python -m venv <name_of_venv>
    python3 -m venv <name_of_venv>
3) Activate the venv:
    On mac/Linux: source name_of_venv/Scripts/activate
    On windows: name_of_venv\Scripts\activate
4) After activiating the venv, to create the proper dependencies in the venv, run either
    pip install -r requirements.txt
    pip3 install -r requirments.txt
5) Change port number in LimitService.py if desired
6) To run server:
    python .\LimitService.y
7) See ClientTest.py to understand usage
