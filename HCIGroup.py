import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Module Dashboard")
        self.geometry("1200x800")
        
        # Create the main frames
        self.sidebar_frame = tk.Frame(self, width=200, bg='#D8B384')
        self.sidebar_frame.pack(side='left', fill='y')

        self.main_frame = tk.Frame(self, bg='#D3C6B3')
        self.main_frame.pack(side='right', expand=True, fill='both')
        
        # Sidebar buttons
        self.create_sidebar()
        
        # Load default page
        self.load_dashboard_page()

    def create_sidebar(self):
        # Add sidebar buttons
        buttons = ["Dashboard", "Modules", "Students", "FAQs", "Help"]
        for button in buttons:
            b = tk.Button(self.sidebar_frame, text=button, font=('Helvetica', 14), bg='#F0E2C2', activebackground='#A48B60',
                          command=lambda btn=button: self.load_page(btn))
            b.pack(fill='x', pady=5, padx=10)

    def load_page(self, page_name):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        if page_name == "Dashboard":
            self.load_dashboard_page()
        elif page_name == "Modules":
            self.load_modules_page()
        elif page_name == "Students":
            self.load_students_page()
        elif page_name == "FAQs":
            self.load_faqs_page()
        elif page_name == "Help":
            self.load_help_page()

    def load_dashboard_page(self):
        # Placeholder for Dashboard content
        tk.Label(self.main_frame, text="Dashboard", font=('Helvetica', 24)).pack(pady=20)

    def load_modules_page(self):
        # Create a frame for the top section containing the search bar and profile circle
        top_section = tk.Frame(self.main_frame, bg='#D3C6B3')
        top_section.pack(pady=10, padx=10, fill='x')

        # Create search bar
        search_entry = tk.Entry(top_section, font=('Helvetica', 16), bg='white')
        search_entry.pack(side='left', padx=10, pady=10, fill='x', expand=True)
        search_entry.insert(0, "Search here")

        # Create profile icon (a circle placeholder)
        profile_circle = tk.Canvas(top_section, width=50, height=50, bg='#D3C6B3', highlightthickness=0)
        profile_circle.create_oval(5, 5, 45, 45, fill='lightgray')
        profile_circle.pack(side='right', padx=10, pady=10)

        # Create a grid layout for module stats and charts
        content_frame = tk.Frame(self.main_frame, bg='#D3C6B3')
        content_frame.pack(pady=20, padx=20, fill='both', expand=True)
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_rowconfigure(1, weight=1)

        # Create module stats frame with a more organized look
        module_stats_frame = tk.Frame(content_frame, bg='#D3C6B3', padx=20, pady=20)
        module_stats_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        tk.Label(module_stats_frame, text="Module stats", font=('Helvetica', 18, 'bold'), bg='#D3C6B3').grid(row=0, column=0, sticky='w', pady=(0, 10))

        # Module stats dropdown
        module_options = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG"]
        selected_module = tk.StringVar()
        selected_module.set(module_options[0])
        module_dropdown = ttk.Combobox(module_stats_frame, textvariable=selected_module, values=module_options, state='readonly')
        module_dropdown.grid(row=0, column=1, sticky='w', padx=(10, 0), pady=(0, 10))
        module_dropdown.configure(background='white')

        # Module stats details - labels and placeholders for values
        module_details = [
            ("Module ID", ""),
            ("Number of students", ""),
            ("Presentation ID", ""),
            ("Assessment type", ""),
            ("Assessment weight", ""),
            ("Date of submission", "")
        ]

        for i, (label, value) in enumerate(module_details, start=1):
            tk.Label(module_stats_frame, text=label, font=('Helvetica', 14), bg='#D3C6B3').grid(row=i, column=0, sticky='w', pady=5)
            value_label = tk.Label(module_stats_frame, text=value, font=('Helvetica', 14), bg='#E0E0E0', width=20, anchor='w')
            value_label.grid(row=i, column=1, sticky='w', pady=5, padx=(10, 0))

        # Display custom images instead of placeholder charts
        self.display_image(content_frame, "Graphs/student_performance.png", 0, 1)
        self.display_image(content_frame, "Graphs/gender_performance.png", 1, 0)
        self.display_image(content_frame, "Graphs/gender_split_modules.png", 1, 1)

    def display_image(self, parent, image_path, row, column):
        try:
            # Load the image using Pillow
            image = Image.open(image_path)
            image = image.resize((400, 300), Image.ANTIALIAS)  # Resize image as needed
            photo = ImageTk.PhotoImage(image)

            # Create label to hold the image
            label = tk.Label(parent, image=photo)
            label.image = photo  # Keep a reference!
            label.grid(row=row, column=column, padx=10, pady=10, sticky='nsew')
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")

    def load_students_page(self):
        # Placeholder for Students page content
        tk.Label(self.main_frame, text="Students Page", font=('Helvetica', 24)).pack(pady=20)

    def load_faqs_page(self):
        # Placeholder for FAQs page content
        tk.Label(self.main_frame, text="FAQs Page", font=('Helvetica', 24)).pack(pady=20)

    def load_help_page(self):
        # Placeholder for Help page content
        tk.Label(self.main_frame, text="Help Page", font=('Helvetica', 24)).pack(pady=20)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
