import os


def docker_compose_restart(project_name):
    # print current working dir info
    print(project_name)
    current_dir_info = 'ls -la'
    os.system(current_dir_info)

    # go to target project folder
    os.chdir(f'/root/projects/{project_name}')
    git_pull_cmd = 'git pull origin dev'
    os.system(git_pull_cmd)
    docker_compose_restart_cmd = 'docker-compose restart'
    os.system(docker_compose_restart_cmd)
    return
