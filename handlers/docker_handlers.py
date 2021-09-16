import os
from util import get_config
from dingding_robot import deploy_message

async def handle_docker_restart(project_name):
    current_working_dir = os.getcwd()

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

    # back to git hook server dir
    os.chdir(current_working_dir)
    await deploy_message.send_finish_deploy_msg(project_name)