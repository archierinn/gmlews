# GMELWS

## Deploy to Heroku
- Register at Heroku ([Click here](https://signup.heroku.com/)) and install heroku CLI ([Click here](https://devcenter.heroku.com/articles/heroku-cli))
- Install git (if not installed yet)
- Clone this project and run this script:
```bash
heroku login
heroku update
heroku plugins:install @heroku-cli/plugin-manifest
heroku apps:create --manifest
heroku addons:create heroku-postgresql:hobby-dev
heroku config:set DISABLE_COLLECTSTATIC=0
git push heroku heroku:master
heroku ps:scale web=1
heroku config:set DISABLE_COLLECTSTATIC=1
```
- Access the web with the provided url (bla2 deployed to heroku), you can change the web url in the settings on your heroku project dashboard
