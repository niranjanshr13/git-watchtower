# git-watchtower
A git webhook that will automatically update a docker container when a push is made to a git repo.


Sketch:
github push => (has a email notification setup to notify the email) => cloudflare email routing send to cloudflare worker => cloudflare worker process the email header scanning for "Approved: Approved header" => send a post request to a a webapp that is underneath the cloudflare tunnel with Service Authentication setup. => a webapp that is in the docker container which has a docker socket connection that execute stop, rm, run command to a docker. 