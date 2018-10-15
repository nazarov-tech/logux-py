# Contributing

You are very much welcome to help with this project! 💛

However, here's some ground rules:

- Respect [Berlin Code of Conduct](https://berlincodeofconduct.org/).

- Don't use any language other than English.
This affects code, commit messages, issues, comments and everything else.

- Don't use any Python other than 3.7 or 3.7+.

- Your commit messages should follow [these 7 rules](https://chris.beams.io/posts/git-commit/).

- Follow [GitLab Flow](https://docs.gitlab.com/ee/workflow/gitlab_flow.html).

- On the code review keep in mind [thoughtbot rules](https://github.com/thoughtbot/guides/tree/master/code-review).


## Setup for development

1. Fork the `logux` repo on GitHub.
2. Clone your fork locally:
```bash
    $ git clone git@github.com:nazarov-tech/logux-py.git
```
3\. Install your local copy into a virtualenv.
Assuming you have virtualenvwrapper installed,
this is how you set up your fork for local development:

```bash
$ mkvirtualenv logux
$ cd logux/
$ python setup.py develop
```

4\. Create a branch for local development:
```bash
$ git checkout -b name-of-your-bugfix-or-feature
```
Now you can make your changes locally.

5\. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox:
```bash
$ flake8 logux tests
$ python setup.py test or py.test
$ tox
```
   To get flake8 and tox, just pip install them into your virtualenv.

6\. Commit your changes and push your branch to GitHub:
```bash
$ git add .
$ git commit -m "Your detailed description of your changes."
$ git push origin name-of-your-bugfix-or-feature
```
7\. Submit a pull request through the GitHub website.

## Build & upload to PyPi

TODO
