from django.urls import path
from webapp.tasks_views.base import HomeView
from webapp.tasks_views.add import TaskAddView, TaskDetailView, ProjectTaskAddView
from webapp.tasks_views.delete_view import TaskDeleteView
from webapp.tasks_views.update_view import TaskUpdateView
from webapp.projects_views.base_project import HomeProjectView
from webapp.projects_views.add_project import ProjectDetailView, ProjectAddView
from webapp.projects_views.delete_project import ProjectDeleteView
from webapp.projects_views.delete_project import ConfirmDelete


urlpatterns = [
    path('', HomeView.as_view(), name='task_home'),
    path('tasks/add/', TaskAddView.as_view(), name='task_add'),
    path('tasks/delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('projects', HomeProjectView.as_view(), name='project_home'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/add/', ProjectAddView.as_view(), name='project_add'),
    path('projects/<int:pk>/tasks/add/', ProjectTaskAddView.as_view(), name='project_task_create'),
    path('projects/confirm_delete/<int:pk>', ConfirmDelete().confirm_delete, name='project_delete'),
    path('projects/delete/<int:pk>', ProjectDeleteView.as_view(), name='project_all_delete')
]

