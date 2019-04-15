import os
from util import get_config
import dingding_robot


def docker_compose_restart(project_name):
    # print current working dir info
    dingding_robot.send_start_deploy_msg(project_name)
    current_dir_info = 'ls -la'
    os.system(current_dir_info)

    # go to target project folder
    os.chdir(f'{get_config()["workspace"]}{project_name}')
    git_pull_cmd = 'git pull origin dev'
    os.system(git_pull_cmd)

    shut_down_docker_compose = 'docker-compose down'
    os.system(shut_down_docker_compose)

    remove_project_docker_image = f'docker rmi {project_name.lower()}:latest'
    os.system(remove_project_docker_image)

    docker_compose_restart_cmd = 'docker-compose up -d'
    os.system(docker_compose_restart_cmd)
    dingding_robot.send_finish_deploy_msg(project_name)
