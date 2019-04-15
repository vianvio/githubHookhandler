# githubHookhandler
github web hook handler

# deploy
1. clone target project with ssh remote
2. add deploy key to project
3. add push hook to project with callback url http(s)://server/githubWebhook/\<ProjectName\>
4. start hook handler server


## add deploy key to new server if deployed
https://developer.github.com/v3/guides/managing-deploy-keys/
## 'Host key verification failed.' for deploy key
ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts
