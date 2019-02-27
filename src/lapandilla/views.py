from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.core.urlresolvers import resolve

# Create your views here.


class IndexView(View):
	"""Define template view for facebook login"""
	app_name = None
	template_name = 'index.html'
	
	def get(self,request, *args,**kwargs):

		return render(request, self.template_name)
