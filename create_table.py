def create_table(titles, cols, name="table"):
    with open((name + ".md"), "w") as f:
        # if (len(titles) != len(img_urls)):
        #     print(f"\033[91mThe length of all provided lists must match.\033[0m")
        #     return
        if (cols > len(titles)):
            print(f"\033[91mThe value of the column should not exceed the length of the provided lists.\033[0m")
            return
        for idx, ttl in enumerate(titles):
            if (idx % cols == 0):
                if (idx != 0):
                    f.write("\n")
                f.write('|')
                if (idx == cols):
                    for _ in range(cols):
                        f.write(" - |")
                    f.write('\n|')            
            f.write(f"<div align='center'><a href='backend/day-{idx+1}'><img src='assets/table-assets/{idx+1}.png' alt='{ttl}' width='140px'/></a><h4 align='center'><a href='backend/day-{idx+1}'>{ttl}</a></h4></div> |")

    print(f"\033[92mMarkdown file '{name+'.md'}' created. \033[0m")

titles = [
    "Introduction to Python", 
    "Data Types", 
    "Conditionals", 
    "Logical Operators", 
    "random", 
    "Loops", 
    "Lists and Dicts (MINI PROJECT)", 
    "Functions", 
    "Modules and Packages", 
    "Exception Handling", 
    "File Handling", 
    "Classes and Objects", 
    "Pillars of OOP", 
    "Pillars of OOP (cont)", 
    "MINI PROJECT", 
    "Virtual Environmnent", 
    "HTTP Methods", 
    "Query Parameters",
    "Request and <br>Response Handling", 
    "Server and Routing", 
    "Blueprints",
    "Jinja", 
    "REST APIs", 
    "Introduction to SQLite",
    "Setting up SQLite in Flask", 
    "Defining Databases", 
    "CRUD", 
    "FINAL PROJECT" 
    ]

# img_urls = [
#     "/assets/table-assets/1.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png",
#     "/assets/test.png"
#     ]

COL = 4

if __name__ == '__main__':
    create_table(titles, COL)

    
