# **hoovada-python-restful-base**

The base code structure for restful flask


Development instruction
---

### DB set up

```bash
CREATE USER IF NOT EXISTS <user>@'%' IDENTIFIED BY <password>;
CREATE DATABASE IF NOT EXISTS hoovada;
GRANT ALL PRIVILEGES ON hoovada.* TO <user>@'%';
FLUSH PRIVILEGES;

// import data
$ mysql -u username -p hoovada < data.sql
```
- Migration with (flask-migrate](https://flask-migrate.readthedocs.io/en/latest/) or put query command in sql/


### Running service

#### with docker

```bash
$ docker build -f ./docker/app/Dockerfile .
$ docker run <name of image> -p 5000:5000
```

#### bare metal

```bash
// For macos

$ brew install libmemcached 
$ cd /tmp
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ sha256sum /tmp/Miniconda3-latest-Linux-x86_64.sh 
$ bash /tmp/Miniconda3-latest-Linux-x86_64.sh -b -p /usr/share/miniconda3 
$ sudo ln -s /usr/share/miniconda3/bin/conda /usr/bin/

$ conda create --name hoovada
$ conda env list
$ conda activate hoovada

$ conda install -c conda-forge pypy3.6
$ ln -s $HOME/.conda/envs/hoovada/bin/pypy3 $HOME/.conda/envs/hoovada/bin/python
// For Macos, the location might be $HOME/miniconda/envs/hoovada/bin/pypy3

$ pypy3 -m ensurepip
$ pypy3 -m pip install --upgrade pip

// install cryptography https://cryptography.io/en/latest/installation/#rust

$ pip3 install -r <path to project>/requirements.txt --ignore-installed

$ source env.dev
$ env FLASK_APP=app.manage:flask_app pypy3 -m flask run
```
- If you face with mixed-content issues https vs http, change api = HTTPSApi() to api=Api() in app/apis.py.


#### docker-compose
```bash
// You need to build every time you update code
$ cd <path to project>
$ docker-compose build

// Docker-compose up will run 4 dockers: API, socketio, DB and adminer for DB UI, REMEMBER to re-build before re-rerun
$ docker-compose up

// Some other useful commands
$ docker-compose ps
$ docker-compose logs <name of container>

// to completely wipe out the set-up
$ docker-compose stop
$ docker-compose rm
```
- Swagger:  http://localhost:5000/api/v1/openapi
- adminer:  http://localhost:80, user/password/db: dev/hoovada/hoovada


### Environment setup

- Create a file .env in root path with all variable you need, please do not push .env to source code


### Code submission 
- Please branch out from dev or master, i.e.

```bash
$ git clone https://gitlab.com/hoovada/hoovada-base-service.git
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
- Then you can create MR with the source branch is your branch and the target branch is dev/master branch.


### Code quality
- API design convention: please follow [this guide](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design)
- Code style: Please follow  Pep8 coding style
- Third-party library:  Please add library + version into app/requirements.txt 
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
```
$ pip3 install pylint
$ pylint <your files>
```

- Save your packages to app/requirements
```
$ pip3 freeze > <path to project>/app/requirements.txt
```


Versioning
---
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://gitlab.com/hoovada/hoovada-python-base/-/tags). 
