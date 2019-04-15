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

    shut_down_docker_compose = 'docker-compose down'
    os.system(shut_down_docker_compose)

    remove_project_docker_image = f'docker rmi {project_name.lower()}:latest'
    os.system(remove_project_docker_image)

    docker_compose_restart_cmd = 'docker-compose up -d'
    os.system(docker_compose_restart_cmd)
    return
