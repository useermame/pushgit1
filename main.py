import os
from constants import *

# Убедитесь, что репозиторий чист
if repo.is_dirty():
    print("У вас есть несохранённые изменения. Пожалуйста, сохраните их перед созданием ветки.")

# Создание локальной ветки
new_branch = repo.create_head(new_branch_name)

# Переключение на новую ветку
new_branch.checkout()
with open('f.txt', 'r') as file:
    content = file.read()

content = content.replace('здарова', 'игорь')
with open('f.txt', 'w') as file:
    file.write(content)
os.system(f'git checkout {new_branch_name}')
os.system('git add .')
os.system("git commit - m 'easypush' ")
os.system("git push")
# Отправка новой ветки на удалённый репозиторий
origin = repo.remote(name='origin')  # Убедитесь, что 'origin' - это ваш удалённый репозиторий
origin.push(new_branch_name)