from django.test import TestCase
from django.test import Client
from VLookUpTool.forms import VlookupForm

# Create your tests here.

class VlookupTestCase(TestCase):
    """ Test Vlookup Form Validation """
    def test_vlookup_addform_validation(self):
            
            
            """ vlookup Form Demo Data """
            lookup_data = {
                'lookup_field1' :['Computer','CPU','Hard Disk','Printer','Keyboard'],
                'lookup_field2' :['Android','Python','Os','IOS','Linux']
                }
            
            
            lookup_form = VlookupForm(lookup_data)
            self.assertTrue(lookup_form.is_valid())
            
            """ Check VlookUp Form isvalid """
             
            lookup_data1 = {
                'lookup_field1' :[],
                'lookup_field2' :['Android','Python','Os','IOS','Linux']
                }
             
            lookup_form1 = VlookupForm(lookup_data1)
            self.assertFalse(lookup_form1.is_valid()) 
            
            """ Check VlookUp Form isvalid """
            lookup_data2 = {
                'lookup_field1' :['Computer','CPU','Hard Disk','Printer','Keyboard'],
                'lookup_field2' :[]
                }
             
            lookup_form2 = VlookupForm(lookup_data2)
            self.assertFalse(lookup_form2.is_valid()) 
            
            """ Check VlookUp Form isvalid """
            lookup_data3 = {
                'lookup_field1' :[],
                'lookup_field2' :[]
                }
             
            lookup_form3 = VlookupForm(lookup_data3)
            self.assertFalse(lookup_form3.is_valid()) 
            
            
            
            

            
            
          

    def test_vlookup_form_post_differentfield_validation(self):
       
       """Different records produced in lookupfield1 & lookupfield2  """
        
       lookup_data = {
                'lookup_field1' : 'Computer\r\nCPU\r\nHard Disk\r\nPrinter\r\nKeyboard',
                'lookup_field2' : 'Android\r\nPython\r\nOS\r\nLinux\r\nIOS'
                }
       lookup = Client()
       response = lookup.post('/',lookup_data)
       self.assertEqual(response.status_code, 200 )
       
       """ Post Vlookup Add Form  Demo Data """
       post_response = self.client.post('/', lookup_data, follow=True)
       union_rs = post_response.context[1]['union_result']
       Symmetric_difference_result = post_response.context[1]['Symmetric_difference_result']
       intersection_result = post_response.context[1]['intersection_result']
       differnce_A_B_result = post_response.context[1]['differnce_A_B_result']
       difference_B_A_result = post_response.context[1]['difference_B_A_result']
     
       """Expected output scenario"""
       self.assertEqual(['Computer','CPU','Hard Disk','Printer','Keyboard','Android','Python','OS','Linux','IOS'],union_rs)
       self.assertEqual(['Computer','CPU','Hard Disk','Printer','Keyboard','Android','Python','OS','Linux','IOS'],Symmetric_difference_result )
       self.assertEqual([],intersection_result)
       self.assertEqual(['Computer','CPU','Hard Disk','Printer','Keyboard'],differnce_A_B_result)
       self.assertEqual(['Android','Python','OS','Linux','IOS'],difference_B_A_result)
       
       
    def test_vlookup_form_post_fields_validation(self):
        
       """lookupfield1 only one record and lookupfield2 one records are same """ 
       lookup_data2 = {
                'lookup_field1' : 'Computer\r\nCPU\r\nHard Disk\r\nPrinter\r\nKeyboard',
                'lookup_field2' : 'Computer\r\nPython\r\nOS\r\nLinux\r\nIOS'
                }
       lookup = Client()
       response = lookup.post('/',lookup_data2)
       self.assertEqual(response.status_code, 200 )
       
       """ Post Vlookup Add Form  Demo Data """
       post_response = self.client.post('/', lookup_data2, follow=True)
       union_rs = post_response.context[1]['union_result']
       Symmetric_difference_result = post_response.context[1]['Symmetric_difference_result']
       intersection_result = post_response.context[1]['intersection_result']
       differnce_A_B_result = post_response.context[1]['differnce_A_B_result']
       difference_B_A_result = post_response.context[1]['difference_B_A_result']
       
       """Expected output scenario"""
       self.assertEqual(['Computer','CPU','Hard Disk','Printer','Keyboard','Python','OS','Linux','IOS'],union_rs)
       self.assertEqual(['CPU','Hard Disk','Printer','Keyboard','Python','OS','Linux','IOS'],Symmetric_difference_result )
       self.assertEqual(['Computer'],intersection_result)
       self.assertEqual(['CPU','Hard Disk','Printer','Keyboard'],differnce_A_B_result)
       self.assertEqual(['Python','OS','Linux','IOS'],difference_B_A_result)   
       
    def test_vlookup_form_post_samefields_validation(self):
        
       """lookupfield1  record and lookupfield2 records are same """  
       lookup_data3 = {
                'lookup_field1' : 'Computer\r\nCPU\r\nHard Disk',
                'lookup_field2' : 'Computer\r\nCPU\r\nHard Disk'
                }
       lookup = Client()
       response = lookup.post('/',lookup_data3)
       self.assertEqual(response.status_code, 200 )
       
       """ Post Vlookup Add Form  Demo Data """
       post_response = self.client.post('/', lookup_data3, follow=True)
       union_rs = post_response.context[1]['union_result']
       Symmetric_difference_result = post_response.context[1]['Symmetric_difference_result']
       intersection_result = post_response.context[1]['intersection_result']
       differnce_A_B_result = post_response.context[1]['differnce_A_B_result']
       difference_B_A_result = post_response.context[1]['difference_B_A_result']
       
       """Expected output scenario"""
       self.assertEqual(['Computer','CPU','Hard Disk'],union_rs)
       self.assertEqual([],Symmetric_difference_result )
       self.assertEqual(['Computer','CPU','Hard Disk'],intersection_result)
       self.assertEqual([],differnce_A_B_result)
       self.assertEqual([],difference_B_A_result)
       
    def test_vlookup_form_post_single_variable_validfield1(self):
        
           """lookupfield1 only one record is placed and  lookupfield2 more than 1 records (Checking possibilities)"""  
        
           lookup_data4 = {
                'lookup_field1' : 'Computer',
                'lookup_field2' : 'Android\r\nCPU\r\nHard Disk'
                }
           lookup = Client()
           response = lookup.post('/',lookup_data4)
           self.assertEqual(response.status_code, 200 )
           
           """ Post Vlookup Add Form  Demo Data """
           post_response = self.client.post('/', lookup_data4, follow=True)
           union_rs = post_response.context[1]['union_result']
           Symmetric_difference_result = post_response.context[1]['Symmetric_difference_result']
           intersection_result = post_response.context[1]['intersection_result']
           differnce_A_B_result = post_response.context[1]['differnce_A_B_result']
           difference_B_A_result = post_response.context[1]['difference_B_A_result']
           
           """Expected output scenario"""
           self.assertEqual(['Computer','Android','CPU','Hard Disk'],union_rs)
           self.assertEqual(['Computer','Android','CPU','Hard Disk'],Symmetric_difference_result )
           self.assertEqual([],intersection_result)
           self.assertEqual(['Computer'],differnce_A_B_result)
           self.assertEqual(['Android','CPU','Hard Disk'],difference_B_A_result)
           
    def test_vlookup_form_post_single_variable_validfield2(self):
        
        
           """ lookupfield1 more than 1 records and lookupfield2 only one record is placed  (Checking possibilities)"""
           lookup_data5 = {
                'lookup_field1' : 'Android\r\nCPU\r\nHard Disk',
                'lookup_field2' : 'Computer'
                }
           lookup = Client()
           response = lookup.post('/',lookup_data5)
           self.assertEqual(response.status_code, 200 )
           
           """ Post Vlookup Add Form  Demo Data """
           post_response = self.client.post('/', lookup_data5, follow=True)
           union_rs = post_response.context[1]['union_result']
           Symmetric_difference_result = post_response.context[1]['Symmetric_difference_result']
           intersection_result = post_response.context[1]['intersection_result']
           differnce_A_B_result = post_response.context[1]['differnce_A_B_result']
           difference_B_A_result = post_response.context[1]['difference_B_A_result']
           
           """Expected output scenario"""
           self.assertEqual(['Android','CPU','Hard Disk','Computer'],union_rs)
           self.assertEqual(['Android','CPU','Hard Disk','Computer',],Symmetric_difference_result )
           self.assertEqual([],intersection_result)
           self.assertEqual(['Android','CPU','Hard Disk'],differnce_A_B_result)
           self.assertEqual(['Computer'],difference_B_A_result)
           
       
    def test_vlookup_form_post_Number_validation(self):
        
        
           """ lookupfield1, lookupfield2 Numbers are placed (Checking possibilities)"""
        
           lookup_data6 = {
                'lookup_field1' : '1\r\n2\r\n3',
                'lookup_field2' : '4'
                }
           lookup = Client()
           response = lookup.post('/',lookup_data6)
           self.assertEqual(response.status_code, 200 )
           
           """ Post Vlookup Add Form  Demo Data """
           post_response = self.client.post('/', lookup_data6, follow=True)
           union_rs = post_response.context[1]['union_result']
           Symmetric_difference_result = post_response.context[1]['Symmetric_difference_result']
           intersection_result = post_response.context[1]['intersection_result']
           differnce_A_B_result = post_response.context[1]['differnce_A_B_result']
           difference_B_A_result = post_response.context[1]['difference_B_A_result']
           
           """Expected output scenario"""
           self.assertEqual(['1','2','3','4'],union_rs)
           self.assertEqual(['1','2','3','4',],Symmetric_difference_result )
           self.assertEqual([],intersection_result)
           self.assertEqual(['1','2','3'],differnce_A_B_result)
           self.assertEqual(['4'],difference_B_A_result)  
           
    def test_vlookup_form_post_uppercase_validation(self):
        
        
           """ lookupfield1, lookupfield2 Numbers Case Sensitive (Checking possibilities)"""
           lookup_data7 = {
                'lookup_field1' : 'ANDROID\r\nandroid\r\nHARD DISK',
                'lookup_field2' : 'ANDROID\r\nhard disk\r\nPYTHON'
                }
           lookup = Client()
           response = lookup.post('/',lookup_data7)
           self.assertEqual(response.status_code, 200 )
           
           """ Post Vlookup Add Form  Demo Data """
           post_response = self.client.post('/', lookup_data7, follow=True)
           union_rs = post_response.context[1]['union_result']
           Symmetric_difference_result = post_response.context[1]['Symmetric_difference_result']
           intersection_result = post_response.context[1]['intersection_result']
           differnce_A_B_result = post_response.context[1]['differnce_A_B_result']
           difference_B_A_result = post_response.context[1]['difference_B_A_result']
           
           """Expected output scenario"""
           self.assertEqual(['ANDROID','android','HARD DISK','hard disk','PYTHON'],union_rs)
           self.assertEqual(['android','HARD DISK','hard disk','PYTHON',],Symmetric_difference_result )
           self.assertEqual(['ANDROID'],intersection_result)
           self.assertEqual(['android','HARD DISK',],differnce_A_B_result)
           self.assertEqual(['hard disk','PYTHON',],difference_B_A_result)
    
    
            
    def test_vlookup_form_post_symbols_validation(self):
        
        
           """ lookupfield1, lookupfield2 Symbol  (Checking possibilities)"""
           lookup_data8 = {
                'lookup_field1' : '&\r\n%\r\n!',
                'lookup_field2' : '*\r\n&\r\n^'
                }
           lookup = Client()
           response = lookup.post('/',lookup_data8)
           self.assertEqual(response.status_code, 200 )
           
           """ Post Vlookup Add Form  Demo Data """
           post_response = self.client.post('/', lookup_data8, follow=True)
           union_rs = post_response.context[1]['union_result']
           Symmetric_difference_result = post_response.context[1]['Symmetric_difference_result']
           intersection_result = post_response.context[1]['intersection_result']
           differnce_A_B_result = post_response.context[1]['differnce_A_B_result']
           difference_B_A_result = post_response.context[1]['difference_B_A_result']
           
           """Expected output scenario"""
           self.assertEqual(['&','%','!','*','^'],union_rs)
           self.assertEqual(['%','!','*','^',],Symmetric_difference_result )
           self.assertEqual(['&'],intersection_result)
           self.assertEqual(['%','!',],differnce_A_B_result)
           self.assertEqual(['*','^',],difference_B_A_result)
           
           
    
    