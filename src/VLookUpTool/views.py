

from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView,FormView

from django.shortcuts import render_to_response
# Create your views here.
from VLookUpTool.forms import VlookupForm
  

class Vlookup(FormView):
    template_name = 'VLookUpTool/vlook_up.html'
    form_class = VlookupForm
    
    def set_difference_calc(self,field1,field2):
        print("work")
        list_index = field1 + field2
        union_result=sorted((set(field1) | set(field2)), key=list_index.index)
        intersection_result=sorted((set(field1) & set(field2)), key=list_index.index)
        differnce_A_B_result=sorted((set(field1) - set(field2)), key=list_index.index)
        difference_B_A_result=sorted((set(field2) - set(field1)), key=list_index.index)
        Symmetric_difference_result=sorted((set(field1) ^ set(field2)), key=list_index.index)
        
        context = {
           'field1':field1,
           'field2':field2,  
           'union_result':union_result, 
           'intersection_result':intersection_result,
           'differnce_A_B_result': differnce_A_B_result,
           'difference_B_A_result':difference_B_A_result,
           'Symmetric_difference_result': Symmetric_difference_result
           
            }
        
        return context
    
    def form_valid(self, form): 
        
        #import ipdb; ipdb.set_trace()
        print("work")
        field1 = form.cleaned_data['lookup_field1'].splitlines()
        field2 = form.cleaned_data['lookup_field2'].splitlines()
        
        
        context = self.set_difference_calc(field1, field2)
        
        context ['form'] = form
    
        return render(self.request, 'VLookUpTool/vlook_up.html', context)
    
