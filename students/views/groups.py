
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView, DeleteView
from django.utils.translation import ugettext as _

from ..models import Group, Student
from ..util import paginate


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/groups_confirm_delete.html'

    def get_success_url(self):
        return u'%s?status_message=%s' % (reverse('groups'),
        _(u"Group deleted successfully!"))


def groups_list(request):
    groups = Group.objects.all()
    order_by = request.GET.get('order_by', '')
    if order_by in ('title',):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    # paginate groups
    context = paginate(groups, 2, request, {}, var_name='groups')

    return render(request, 'students/groups_list.html', context)

def groups_add(request):
    if request.method == 'POST':
        if request.POST.get('add_button') is not None:
            errors = {}
            data = {}


            title = request.POST.get('title','').strip()
            if not title:
                errors['title'] = _(u'Group field is required')
            else:
                groups_count = Group.objects.filter(title=title)
                if len(groups_count) != 0:
                    errors['title'] = _(u'A group of that name already exists')
                data['title'] = title

            leader = request.POST.get('leader','').strip()
            if not leader:
                pass
            else:
                students = Student.objects.filter(pk=leader)
                leaders = Group.objects.filter(leader=leader)
                if len(students) != 1:
                    errors['leader'] = _(u'Select correct student')
                elif len(leaders) != 0:
                    errors['leader'] = _(u'This student is the leader of another group')
                else:
                    data['leader'] = students[0]

            if not errors:
                group = Group(**data)
                group.save()

                return HttpResponseRedirect(
                    u'%s?status_message=%s' %
                    (reverse('groups'), _(u"Group added successfully!")))

            else:
                return render(request, 'students/groups_add.html',
                    {'students': Student.objects.all().order_by('last_name'),
                     'errors': errors})

        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(
                u'%s?status_message=%s!' %
                (reverse('group'), _(u"Adding a group canceled!")))
    else:
        # initial form render
        return render(request, 'students/groups_add.html',
            {'students': Student.objects.all().order_by('last_name')})



    return render(request, 'students/groups_add.html',
        {'students': Student.objects.all().order_by('last_name')})

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
