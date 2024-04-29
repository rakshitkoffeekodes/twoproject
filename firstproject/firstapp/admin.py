from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")


class SubCategoryAdmin(admin.ModelAdmin):
    def Popup(self, obj):
        form_url = reverse('accept_reject_form', args=[obj.pk])
        print(form_url)
        return format_html("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
                  integrity="sha512-iBBXm8fW90+nuLcSKlbmrPcLa0OT92xO1BIsZ+ywDWZCvqsWgccV3gFoRBv0z+8dLJgyAHIhR35VZc2oM/gI1w=="
                  crossorigin="anonymous" referrerpolicy="no-referrer"/>
        </head>
        <body>
                <style>
                    .popup {{
                        position: fixed;
                        top: 0;
                        right: 0;
                        left: 0;
                        bottom: 0;
                        width: 100vw;
                        height: 100vh;
                        background-color: rgba(0, 0, 0, 0.5);
                        z-index: 10000;
                    }}
                    
                    .form-data {{
                        position: fixed;
                        background-color: white;
                        border-radius: 20px;
                        width: 25%;
                        height: 70%;
                        left: 40vw;
                        top: 15vh;
                    }}
                    
                    .cancel-icon{{
                        position: absolute;
                        right: 8px;
                        top: 8px;
                        color: white;
                        background: #8ca4b5;
                        padding: 5px 7px;
                        border-radius: 100%;
                    }}
                    
                    .first-container {{
                        width: 100%;
                        height: 10%;
                    }}
                    
                    .second-container {{
                        padding-left: 20px;
                        font-family: "Garamond", Times, serif;
                        font-weight: bold;
                    }}
                    
                    .third-container {{
                        width: 100%;
                        height: 30%;
                    }}
                    
                    .four-container {{
                        width: 100%;
                        height: 30%;
                        
                    }}
                    
                    .five-container {{
                        width: 100%;
                        height: 30%;
                    }}
                    
                    .required {{
                        color:red;
                    }}
                    
                    .select-label{{
                        font-family: "Times New Roman", Times, serif;
                        padding-left: 20px;
                        padding-top: 10px;
                        font-size: 20px;
                    }}
                    
                    .dropdown {{
                        width:87%;
                        height: 30%;
                        margin-left:20px;
                        outline: none;
                        border-radius: 20px;
                        font-family: "Times New Roman", Times, serif;
                    }}
                    
                    .enter-label{{
                        font-family: "Times New Roman", Times, serif;
                        padding-left: 20px;
                        padding-top: 10px;
                        font-size: 20px;
                    }}
                    
                    .input-text {{
                        width:87%;
                        height: 30%;
                        margin-left:20px;
                        border-radius: 15px;
                        font-family: "Times New Roman", Times, serif;
                        outline: none;
                    }}
                    
                    .save-btn {{
                        margin-left:20px;
                        padding: 2% 38%;
                        border-radius: 20px;
                        color: white;
                        background-color: black;
                        cursor: pointer;
                    }}
                    
                </style>
                <button type="button" onclick="popupFn()" id="button" class="btn btn-primary">
                    Action
                </button>
                <div id="form" class="popup" style="display:none;">
                     <div class="form-data" id="form-data">
                        <form action="/accept_reject_form/" method="post" id="myForm" >
                            <div class="first-container">
                                <i class="fa fa-times cancel-icon" aria-hidden="true" id="cancel"></i>
                            </div>
                            <div class="second-container">
                                <h3>Action Form</h3>
                            </div>
                            <div class="third-container">
                                <p class="p-header-2 font-family select-label">Select <span class="required">*</span> :</p>
                                <select class="dropdown" name="option" id="dropdown" style="border-color: black;">
                                    <option name="option" value="0">--------</option>
                                    <option name="option" value="1">Accept</option>
                                    <option name="option" value="2">Reject</option>
                                </select>
                            </div>
                            <div class="four-container">
                                <p class="p-header-2 font-family enter-label">Enter <span class="required">*</span>&nbsp;:</p>
                                <input type="text" id="input" name="name" placeholder="Enter..." class="input-text" style="border-color: black; border-radius: 20px;">
                            </div>
                            <div class="five-container">
                                <button type="button" onclick="getFormData('{}')" class="save-btn">save</button>
                            </div>
                        </form>
                     </div>
                </div>
                <script>
                     function popupFn() {{
                        var form = document.getElementById("form");
                        var dropdown = document.getElementById("dropdown");
                        var input = document.querySelector(".input-text");
                        var cancel = document.getElementById("cancel");

                        form.style.display = "block";

                        dropdown.addEventListener("change", function() {{
                            if (this.value === "1")
                                input.placeholder = "Enter a URL";
                            else if (this.value === "2")
                                input.placeholder = "Enter a reason";
                            else if (this.value === "0")
                                input.placeholder = "Enter..";
                        }});
                        
                    }}
                    
                    function getFormData(formUrl) {{
                        var option = document.getElementById("dropdown").value;
                        var name = document.getElementById("input").value;
                        var url = formUrl + '?option=' + option + '&name=' + name;
                        window.location.href = url;
                    }}
                    
                    document.getElementById("cancel").addEventListener("click", function()
                    {{
                        document.getElementById("form").style.display = "none";
                    }});
                    
                </script>
            </body>
        </html>
        """,form_url)

    Popup.short_description = "Action"

    list_display = ["sub_category_id", "sub_category_name", "description", "category_id", "reason", "accept", "Popup"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)

#
# <div class="demo" >
#                     <div id="form" class="popup" style="display:none;>
#                         <form action="/accept_reject_form/" method="post" id="myForm" >
#                             <div class="first-container">
#                                 <div class="first-container-1">
#                                     <p class="p-header font-family"> Accept Reject Action Form </p>
#                                 </div>
#                                 <div class="first-container-2">
#                                     <i class="fa fa-times i" id="cancel" aria-hidden="true"></i>
#                                 </div>
#                             </div>
#                             <div class="second-container">
#                                 <div class="second-container-1" >
#                                     <div class="first-div">
#                                         <div class="first">
#                                             <p class="p-header-2 font-family ">Select Accept / Reject</p>
#                                         </div>
#                                         <div class="second">
#                                             <p class="p-header-2 font-family select-label">Select <span class="required">*</span> :</p>
#                                             <select class="dropdown" name="option" id="dropdown">
#                                                 <option name="option" value="0">--------</option>
#                                                 <option name="option" value="1">Accept</option>
#                                                 <option name="option" value="2">Reject</option>
#                                             </select>
#                                         </div>
#                                         <div class="third">
#                                             <p class="p-header-2 font-family enter-label">Enter <span class="required">*</span>&nbsp;&nbsp;&nbsp;:</p>
#                                             <input type="text" name="name" id="input" class="text-input" placeholder="Enter ..">
#                                         </div>
#                                         <div class="four">
#                                             <button type="button" onclick="getFormData('{}')" class="save-btn">save</button>
#                                         </div>
#                                     </div>
#                                 </div>
#                             </div>
#                         </form>
#                     </div>
#                 </div>

#
# function popupFn() {{
#                         var form = document.getElementById("form");
#                         var dropdown = document.getElementById("dropdown");
#                         var input = document.querySelector(".text-input");
#                         var cancel = document.getElementById("cancel");
#                         var body = document.querySelector("body");
#
#                         form.style.display = "block";
#
#                         dropdown.addEventListener("change", function() {{
#                             if (this.value === "1")
#                                 input.placeholder = "Enter a URL";
#                             else if (this.value === "2")
#                                 input.placeholder = "Enter a reason";
#                             else if (this.value === "0")
#                                 input.placeholder = "Enter..";
#                         }});
#                     }}
#
#                     function getFormData(formUrl) {{
#                         var option = document.getElementById("dropdown").value;
#                         var name = document.getElementById("input").value;
#                         var url = formUrl + '?option=' + option + '&name=' + name;
#                         window.location.href = url;
#                     }}
#
                    # document.getElementById("cancel").addEventListener("click", function()
                    # {{
                    #     document.getElementById("form").style.display = "none";
                    # }});