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
5. [Motivation](#Motivation)


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

### Recommended code contribution and submission 

- The live branch should be named **master** or **main**

- The main feature branch is named **dev** where development is branched out from dev

```bash
$ git checkout -b dev origin/dev
$ git checkout -b <your branch name> dev

# do your development

$ git add --all 
$ git commit -s -am "your message"

# You might also need to rebase from upstream remote branch before pushing
$ git rebase upstream/dev

# Save new packages to app/requirements
$ pip3 freeze > <path to project>/app/requirements.txt

# To push your branch
$ git push -u origin <your branch name>
```

- Then you can create MR with the source branch is your branch and the target branch is dev. 
- When we release, we merge dev into master, tag them and deploy.


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


Motivation
---
If you like this project, you can buy buy me a [pizza](https://www.buymeacoffee.com/tranlv) to motivate me improve on the project.
