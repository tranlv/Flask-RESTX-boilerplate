# **Flask-RESTX-boilerplate**

The base code structure for Flask-RESTX


Development instruction
---

### Directory 



### Running service with docker

```bash
$ docker build -f ./docker/app/Dockerfile .
$ docker run <name of image> -p 5000:5000
```

### Code submission 
- Please branch out from dev or master, i.e.

```bash
$ git clone <>
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
We use [SemVer](http://semver.org/) for versioning.
