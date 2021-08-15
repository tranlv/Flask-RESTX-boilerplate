REGISTRY   		:= registry.gitlab.com/hoovada/hoovada-python-base
REPO_NAME   	:= $$(/usr/bin/basename -s .git `git config --get remote.origin.url`)
GIT_COMMIT 		:= $$(git rev-parse --short HEAD)
GIT_BRANCH 		:= $$(git branch | grep \* | cut -d ' ' -f2)
DATE 			:= $$(date +'%d%b%Y')

BASE   			:= ${REGISTRY}:base-${GIT_COMMIT}-${GIT_BRANCH}-${DATE}

base:
	@docker build -t ${BASE} -f ./docker/base/Dockerfile .
	@docker push ${BASE}

deploy-staging:
	@kubectl set image deployment/base base=${BASE} -n <> --context=do-sgp1-test --record

all-staging: base deploy-staging

deploy-live:
	@kubectl set image deployment/base base=${BASE} -n <> --context=do-sgp1-production --record

all-live: base deploy-live

login:
	@docker login registry.gitlab.com

run-local:
	FLASK_APP=app.manage:flask_app python -m flask run
