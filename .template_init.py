from torchbuilder import init
from rich import print
import os


path = init.get_project_path(__file__)
os.mkdir(f'{path}/logs')
os.mkdir(f'{path}/saved_models')
os.mkdir(f'{path}/results')

init.init_git_repo(path)
init.init_uv_project(path)
print(f"[green]Successfully initialized the project 🎉[/green]")
