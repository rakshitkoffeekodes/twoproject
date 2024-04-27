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
                        margin-top: 60px;
                        position: fixed;
                        top: 13vh;
                        left: 37vw;
                        bottom: 10px;
                        right: 0;
                        width: 40vw;
                        height: 50vh;
                        box-shadow: 5px 5px 2px #7e7e7e;
                        border-radius: 3px;
                        background-color: white;
                    }}

                     .first-container{{
                            width:100%;
                            height: 12%;
                            border-bottom: 2px solid #e8e8e8;
                            display: flex;
                        }}

                     .font-family{{
                            font-family: "Source Sans Pro",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"
                        }}

                     .p-header{{
                            padding-left: 10px;
                            padding-top: 5px;
                            padding-bottom: 10px;
                        }}

                     .p-header-2 {{
                            padding-left: 10px;
                            padding-top: 5px;
                            padding-bottom: 5px;
                        }}

                     .first-container-1 {{
                            width: 97%;
                        }}

                     .i {{
                            font-size:20px;
                            margin-right: 15px;
                            margin-top:10px;
                            color: #7e7e7e;
                        }}

                     .second-container {{
                            width:100%;
                            height: 88%;
                            padding: 15px;
                        }}

                     .second-container-1 {{
                            background-color: #e8e8e8;
                            width: 100%;
                            height: 100%;
                            padding:10px;
                        }}

                     .first-div {{
                            width: 100%;
                            height: 100%;
                            background-color: white;
                            margin-bottom:10px;
                            border-top: 2px solid #007bff;
                            border-radius: 3px;
                        }}

                     .second-div {{
                            width: 100%;
                            height: 37%;
                            background-color: white;
                            margin: 0px 10px 10px 10px;
                            border-top: 2px solid #328ff4;
                            border-radius: 3px;
                        }}

                     .first {{
                            width: 100%;
                            height: 15%;
                            border-bottom: 1px solid #e8e8e8;
                        }}

                     .second {{
                            display:flex;
                            width: 100%;
                            height: 20%;
                        }}

                     .select-label{{
                            font-size: 15px;
                            margin-top: 10px;
                            margin-right:20px;
                        }}

                     .required {{
                            color: red;
                        }}

                     .dropdown {{
                            width: 40%;
                            height: 90%;
                            margin-top: 10px;
                            outline: none;
                            border: 1px solid #ced4da;
                            border-radius: 3px;
                        }}

                     .third{{
                            display: flex;
                            width: 100%;
                            height: 20%;
                            margin-bottom: 5%;
                        }}

                     .enter-label{{
                            font-size: 15px;
                            margin-top: 25px;
                            margin-right:19px;
                        }}

                     .text-input{{
                            width:70%;
                            margin-top: 25px;
                            outline: none;
                            height: 15%;
                        }}

                     .four {{
                            height: 10%;
                        }}

                     .save-btn{{
                            margin-top: 5%;
                            margin-left: 7%;
                            padding-left: 40%;
                            padding-right: 40%;
                            border: 0px;
                            background-color: #28a745;
                            color: white;
                            border-radius: 3px;
                        }}
                </style>
                <button type="button" onclick="popupFn()" id="button" class="button">
                    Action
                </button>
                <div id="form" class="popup" style="display:none;>
                    <form action="/accept_reject_form/" method="post" id="myForm" >
                        <div class="first-container">
                            <div class="first-container-1">
                                <p class="p-header font-family"> Accept Reject Action Form </p> 
                            </div>
                            <div class="first-container-2">
                                <i class="fa fa-times i" id="cancel" aria-hidden="true"></i>
                            </div>
                        </div>
                        <div class="second-container">
                            <div class="second-container-1" >
                                <div class="first-div">
                                    <div class="first">
                                        <p class="p-header-2 font-family ">Select Accept / Reject</p>
                                    </div>
                                    <div class="second">
                                        <p class="p-header-2 font-family select-label">Select <span class="required">*</span> :</p>
                                        <select class="dropdown" name="option" id="dropdown">
                                            <option name="option" value="0">--------</option>
                                            <option name="option" value="1">Accept</option>
                                            <option name="option" value="2">Reject</option>
                                        </select>
                                    </div>
                                    <div class="third">
                                        <p class="p-header-2 font-family enter-label">Enter <span class="required">*</span>&nbsp;&nbsp;&nbsp;:</p>
                                        <input type="text" name="name" id="input" class="text-input" placeholder="Enter ..">
                                    </div>
                                    <div class="four">
                                        <button type="button" onclick="getFormData('{}')" class="save-btn">save</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
                <script>
                    
                    function popupFn() {{
                        var form = document.getElementById("form");
                        var dropdown = document.getElementById("dropdown");
                        var input = document.querySelector(".text-input");
                        var cancel = document.getElementById("cancel");
                        var body = document.querySelector("body");
                    
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
                        document.querySelector("body").style.opacity = "1";
                    }});
                </script>
            </body>
        </html>
        """,form_url)

    Popup.short_description = "Action"

    list_display = ["sub_category_id", "sub_category_name", "description", "category_id", "reason", "accept", "Popup"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
