from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from home.models import Task

# Create your views here.
def home(request):
   #return HttpResponse("Hii This is ur to do list app")
   return render(request,'home.html')

def addtask(request):
   context={'success':False}
   if request.method=='POST':
      title = request.POST.get('title')
      # desc = request.POST.get('desc')
      print(title)
      # ins=Task(taskTitle=title,taskdesc=desc)
      ins=Task(taskTitle=title)
      ins.save()
      context={'success':True}
   return render(request,'addtasks.html',context)

# def viewtask(request):
#     alltasks = Task.objects.all()
#     print("All tasks:")
#     for i in alltasks:
#         print(f"Title: {i.taskTitle}, Time: {i.time}")
#     context = {'tasks': alltasks}
#     return render(request, 'viewtasks.html', context)

def viewtask(request):
    alltasks = Task.objects.all()
    pending_tasks = Task.objects.filter(status='pending').order_by('time')
    completed_tasks = Task.objects.filter(status='completed').order_by('time')
    context = {
        'tasks': alltasks,
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'viewtasks.html', context)

def mark_as_done(request, id):
    print(f"Marking task {id} as done")  # Debugging print
    task = get_object_or_404(Task, id=id)
    task.status = 'completed'
    task.save()
    return redirect('viewtask')

def edittask(request, id):
    task = get_object_or_404(Task, id=id)  # Get the task by ID
    if request.method == "POST":
        task.taskTitle = request.POST.get('title')
      #   task.taskdesc = request.POST.get('desc')
        task.save()  # Save the updated task
        return redirect('viewtask')  # Redirect to view tasks page after editing
    return render(request, 'edittask.html', {'task': task})
 
def deletetask(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect('viewtask')  # Redirect after deletion
    return render(request, 'deletetask.html', {'task': task})