import os
import re

from .conftest import infra_dir_path, root_dir


class TestDockerfileCompose:

    def test_infra_structure(self):
        assert 'infra' in os.listdir(root_dir), (
            f'Проверьте, что в пути {root_dir} указана папка `infra`'
        )
        assert os.path.isdir(infra_dir_path), (
            f'Проверьте, что {infra_dir_path} - это папка, а не файл'
        )

    def test_docker_compose_file(self):
        try:
            with open(f'{os.path.join(infra_dir_path, "docker-compose.yaml")}', 'r') as f:
                docker_compose = f.read()
        except FileNotFoundError:
            assert False, f'Проверьте, что в директорию {infra_dir_path} добавлен файл `docker-compose.yaml`'


