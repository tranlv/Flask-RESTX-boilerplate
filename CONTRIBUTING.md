# **Instructions for contributors**

For bug reports or requests please submit an [issue](https://github.com/tranlyvu/Flask-RESTX-boilerplate/issues) and briefly add the issue into the [release notes]

For new feature contribution, please follow the following instruction:

1. Fork the repo https://github.com/tranlyvu/Flask-RESTX-boilerplate.git to your own github

2. Clone from your own repo

`$ git clone https://github.com/<your name>/Flask-RESTX-boilerplate.git`

3. Make sure you are at dev branch 

`$ git checkout main && git pull`

4. Create your feature/bug-fix branch

`$ git checkout -b <feature/bug>/<branch-name>`

Do remember to add your name into the [list of contributors](https://github.com/tranlyvu/Flask-RESTX-boilerplate/blob/master/CONTRIBUTORS.md) if you have not done so before going to step 5.

5. Commit your changes 

`$ git commit -am 'Add some new feature'`

6. Push to the branch 

`$ git push`

7. Go to your own repo and create a new Pull Request against 'master' branch

8. To sync your forked repo with my repo

```
$ git remote add upstream https://github.com/tranlyvu/Flask-RESTX-boilerplate.git
$ git checkout master
$ git merge upstream/master
```