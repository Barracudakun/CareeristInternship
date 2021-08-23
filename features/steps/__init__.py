'''
POM:

Structure: 1 . base_page: including all the common use method. such as find_element, click, input_text...
           2.  pages: like main_page, cart_page, every page should have individual method, click , find_element...
           3. feature>steps : use BDD method to write the requirement

relationship between all the pages:
         1. pages like main_page, cart_page, heritage(继承) base_page
         2. feature>steps  heritage(继承) pages like main_page, cart_page

notes : Pages folder must use class Pages: > def xxx(self):
'''