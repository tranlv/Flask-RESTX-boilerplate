# **Flask-RESTX-boilerplate**

The base code structure for Flask-RESTX

Directory 
---

### `/app`

#### `/app/manage.py`

- The entry point of the code

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

### Recommended code contribution and submission 

- The live branch should be named **master**

- The main feature branch is named **dev** where development is branched out from dev

```bash
$ git checkout -b dev origin/dev
$ git checkout -b <your branch name> dev

// do your development

$ git add --all 
$ git commit -s -am "your message"

// You might also need to rebase from upstream remote branch before pushing
$ git rebase upstream/dev

// To push your branch
$ git push -u origin <your branch name>
```

- Then you can create MR with the source branch is your branch and the target branch is dev. When we release, we merge dev into master, tag them and deploy.


### Code quality
- API design convention:  follow [this guide](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design)
- Code style: Pep8 coding style
- Third-party library: add library + version into app/requirements.txt 
- Quote: Please use either ‘’ or “” but not both
- import statement:
	- Please use full path import
	- Recomend to import only necessary function not entire package, i.e. if you only need sqrt():
	```
		Recommended:  		from math import sqrt
		Not recommended:  	import math
	```

- Status code: Please use English only, i.e. in send_error and send_result.
- Exception - EAFP principle: use except/try instead of if/else, also if possible please use specific exceptions instead of generic exception.
- Please use clear commit message
- Please add unit test for your code
- Plese use pylint before pushing code

```bash
$ pip3 install pylint
$ pylint <your files>
```

- Save your packages to app/requirements

```bash
$ pip3 freeze > <path to project>/app/requirements.txt
```

Versioning
---
We use [SemVer](http://semver.org/) for versioning.
