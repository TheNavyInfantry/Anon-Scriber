# Anon Scriber
Anon Scriber is a web application where people can anonymously share posts of a memoir of themselves or of someone

---

### Project Status
Anon Scriber is still under heavy development. There can be breaking changes, but I am trying to keep them as minimum as possible.

### Requirements

* Python 3.9


* Other required packages in requirements.txt

---

### How To Run

* Clone this repository.

```bash
$ git clone --recursive https://github.com/TheNavyInfantry/Anon-Scriber.git

$ cd Anon-Scriber
```


* Install `virtualenv`:
```bash
$ pip install virtualenv
```

* Open a terminal in the project root directory and run:
```bash
$ virtualenv venv
```

* Then run the command:
```bash
$ source venv/bin/activate
```

* Then install the dependencies:
```bash
$ (venv) pip3 install -r requirements.txt
```

* Then setup the database:
```bash
$ (venv) python
```

```python
    >>> from anon_scriber import db

    >>> db.create_all()
```

* Then setup the flask: (<b>NOTE: export is used in Linux</b>)
```bash
$ (venv) export FLASK_APP=app.py

$ (venv) export FLASK_DEBUG=True
```



* Finally start the web server:
```bash
$ (venv) flask run
```

* This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
