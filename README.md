# **Flask-RESTX-boilerplate**

<p align="center">
	<a href="https://saythanks.io/to/vutransingapore"><img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg"></a>
</p>


---
The boilerplate for the project using restful [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/) framework

---
Table of contents
---

1. [Directory Convention](#Directory-Convention)
2. [Development instruction](#Development-instruction) 
3. [Test and Code quality](#Test-and-Code-quality)
4. [Versioning](#Versioning)
5. [Contribution](#Contribution)


Directory Convention
---

### `/app`

#### `/app/manage.py`

- The entry point of the code

#### `/app/config.py`

- Store configuration from env variables

#### `/app/modules`

Flask-RESTX provides a way to use Flask’s blueprint. The main idea is to split your app into reusable namespaces. Here namespaces are organized in different modules

- /app/modules/sample_mod:  each module is split into MVC, i.e. controller, dto, view
	- /app/modules/sample_controller.py
	- /app/modules/sample_dto.py
	- /app/modules/sample_view.py

- /app/modules/sample_mod/datadef: validation layer
		
#### `app/extensions` 

we put everything else here, i.e. interfaces, cache, databases, ORM, i18n, monitor, logging, etc.


### `/docker`

- All related docker files


### `/sql`

- sql migration files

### `/test`

- unit test directory

### `/docs`

- Store documents files


Development instruction
---

### Running service with docker

```bash
$ docker build -f ./docker/app/Dockerfile .
$ docker run <name of image> -p 5000:5000
```

- Swagger is at /api/v1/openapi

### Test and Code quality

#### Unit test

```bash
$ pytest tests
```

#### Code quality

```bash
$ pylint ./app
$ mypy ./app
$ black ./tests
```

- API design: [guide](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design)
- Code style: [Pep8 coding style](https://peps.python.org/pep-0008/)
- import statement: better to import only necessary function not entire package, i.e. if you only need sqrt():
```bash
	Recommended:  		from math import sqrt
	Not recommended:  	import math
```
- Exception - EAFP principle: use except/try instead of if/else, and try to use specific exceptions instead of generic exception.


Versioning
---
We use [SemVer](http://semver.org/) for versioning. Please see CHANGELOG.md for more details.


Contribution
---

Please follow our contribution convention at [contribution instructions](https://github.com/tranlyvu/Flask-RESTX-boilerplate/blob/master/CONTRIBUTING.md) and [code of conduct](https://github.com/tranlyvu/
Flask-RESTX-boilerplate/blob/master/CODE-OF-CONDUCT.md).

To set up development environment, simply run:

```bash
$ pip install -r requirements.txt
```


You can also put a [vote to get the project](https://github.com/vinta/awesome-python/pull/2104) more visible to others.


If you like this project, you can buy buy me a [pizza](https://www.buymeacoffee.com/tranlv) to motivate me improve on the project.
