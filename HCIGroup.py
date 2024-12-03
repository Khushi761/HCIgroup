import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import os 
import seaborn as sns
import matplotlib.pyplot as plt

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
        # Dashboard Header
        tk.Label(self.main_frame, text="Dashboard", font=('Helvetica', 18)).pack(pady=10)

        # Content Frame for Dashboard
        content_frame = tk.Frame(self.main_frame, bg='#D3C6B3')
        content_frame.pack(pady=10, padx=10, fill='both', expand=True)
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_rowconfigure(1, weight=1)

        # Region Graph (Static Image)
        self.display_image(content_frame, "Graphs/GPSmap.png", 0, 0)

        # Popularity Chart with Dropdown
        popularity_frame = tk.Frame(content_frame, bg='#D3C6B3')
        popularity_frame.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        tk.Label(popularity_frame, text="Select Popularity Chart:", font=('Helvetica', 12), bg='#D3C6B3').pack(pady=5)

        popularity_options = {
            "Enrollment Over Time": "Graphs/Popularity.png",
            "Withdrawal Trends": "Graphs/Popularity2.png",
            "Week-based Trends": "Graphs/Popularity3.png"
        }
        selected_popularity = tk.StringVar(value=list(popularity_options.keys())[0])

        popularity_dropdown = ttk.Combobox(popularity_frame, textvariable=selected_popularity, values=list(popularity_options.keys()), state="readonly")
        popularity_dropdown.pack(pady=5)

        popularity_image_label = tk.Label(popularity_frame, bg='#D3C6B3')
        popularity_image_label.pack(pady=5)

        def update_popularity_chart(event=None):
            chart_name = selected_popularity.get()
            selected_image = popularity_options[chart_name]
            try:
                image = Image.open(selected_image)
                image = image.resize((300, 200), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                popularity_image_label.config(image=photo)
                popularity_image_label.image = photo
            except Exception as e:
                print(f"Error loading image {selected_image}: {e}")
                popularity_image_label.config(text="Error loading image", image="")

        popularity_dropdown.bind("<<ComboboxSelected>>", update_popularity_chart)
        update_popularity_chart()

        # Heatmap Chart with Dropdown
        heatmap_frame = tk.Frame(content_frame, bg='#D3C6B3')
        heatmap_frame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        tk.Label(heatmap_frame, text="Select Heatmap:", font=('Helvetica', 12), bg='#D3C6B3').pack(pady=5)

        heatmap_options = {
            "Course Heatmap A": "Graphs/Heatmap.png",
            "Course Heatmap B": "Graphs/Heatmap2.png",
            "Course Heatmap C": "Graphs/Heatmap3.png"
        }
        selected_heatmap = tk.StringVar(value=list(heatmap_options.keys())[0])

        heatmap_dropdown = ttk.Combobox(heatmap_frame, textvariable=selected_heatmap, values=list(heatmap_options.keys()), state="readonly")
        heatmap_dropdown.pack(pady=5)

        heatmap_image_label = tk.Label(heatmap_frame, bg='#D3C6B3')
        heatmap_image_label.pack(pady=5)

        def update_heatmap(event=None):
            heatmap_name = selected_heatmap.get()
            selected_image = heatmap_options[heatmap_name]
            try:
                image = Image.open(selected_image)
                image = image.resize((300, 200), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                heatmap_image_label.config(image=photo)
                heatmap_image_label.image = photo
            except Exception as e:
                print(f"Error loading image {selected_image}: {e}")
                heatmap_image_label.config(text="Error loading image", image="")

        heatmap_dropdown.bind("<<ComboboxSelected>>", update_heatmap)
        update_heatmap()

        # Performance Chart with Dropdown
        performance_frame = tk.Frame(content_frame, bg='#D3C6B3')
        performance_frame.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')
        tk.Label(performance_frame, text="Select Performance Metric:", font=('Helvetica', 12), bg='#D3C6B3').pack(pady=5)

        performance_options = {
            "Gender Performance": "Graphs/GenderPerformance.png",
            "Age-Range Performance": "Graphs/AgeBandPerformance.png",
            "Region Performance": "Graphs/RegionPerformance.png",
            "Number of Attempts": "Graphs/PrevAttemptsPerformance.png"
        }
        selected_performance = tk.StringVar(value=list(performance_options.keys())[0])

        performance_dropdown = ttk.Combobox(performance_frame, textvariable=selected_performance, values=list(performance_options.keys()), state="readonly")
        performance_dropdown.pack(pady=5)

        performance_image_label = tk.Label(performance_frame, bg='#D3C6B3')
        performance_image_label.pack(pady=5)

        def update_performance_chart(event=None):
            metric_name = selected_performance.get()
            selected_image = performance_options[metric_name]
            try:
                image = Image.open(selected_image)
                image = image.resize((300, 200), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                performance_image_label.config(image=photo)
                performance_image_label.image = photo
            except Exception as e:
                print(f"Error loading image {selected_image}: {e}")
                performance_image_label.config(text="Error loading image", image="")

        performance_dropdown.bind("<<ComboboxSelected>>", update_performance_chart)
        update_performance_chart()




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
            image = image.resize((400, 300), Image.LANCZOS)  # Resize image as needed
            photo = ImageTk.PhotoImage(image)

            # Create label to hold the image
            label = tk.Label(parent, image=photo)
            label.image = photo  # Keep a reference!
            label.grid(row=row, column=column, padx=10, pady=10, sticky='nsew')
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")

    def load_students_page(self):
        # Load datasets
        try:
            base_dir = os.path.join(os.path.dirname(__file__), "anonymisedData")
            self.student_info = pd.read_csv(os.path.join(base_dir, "studentInfo.csv"))
        except FileNotFoundError as e:
            print(f"File not found: {e.filename}")
            self.student_info = pd.DataFrame()
        except Exception as e:
            print(f"Error loading datasets: {e}")

        # Create the UI for the students page
        container = tk.Frame(self.main_frame, bg='#D3C6B3')
        container.pack(fill='both', expand=True, padx=20, pady=20)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=2)

        # Scrollable Student Details
        stats_frame = tk.Frame(container, bg='#D3C6B3', padx=20, pady=20)
        stats_frame.grid(row=0, column=0, sticky='nsew')

        tk.Label(stats_frame, text="Student Details", font=('Helvetica', 18, 'bold'), bg='#D3C6B3').pack(anchor='w', pady=(0, 20))

        # Create a scrollable canvas for student attributes
        canvas = tk.Canvas(stats_frame, bg='#D3C6B3', highlightthickness=0)
        scrollbar = ttk.Scrollbar(stats_frame, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#D3C6B3')

        # Ensure canvas resizes properly
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Display all attributes for a randomly selected student
        if not self.student_info.empty:
            student = self.student_info.sample(1).iloc[0]  # Randomly select a student
            for column in self.student_info.columns:
                frame = tk.Frame(scrollable_frame, bg='#D3C6B3', pady=5)
                frame.pack(fill='x', pady=2)
                tk.Label(
                    frame, text=f"{column}:", font=('Helvetica', 12), bg='#D3C6B3'
                ).pack(side='left', padx=5)
                tk.Label(
                    frame, text=f"{student[column]}", font=('Helvetica', 12, 'bold'), bg='#E0E0E0', width=25, anchor='w'
                ).pack(side='left', padx=5)
        else:
            tk.Label(scrollable_frame, text="No student data available.", font=('Helvetica', 14), bg='#D3C6B3').pack(anchor='w', pady=10)

        heatmap_frame = tk.Frame(container, bg='white', padx=20, pady=20)
        heatmap_frame.grid(row=0, column=1, sticky='nsew')

        tk.Label(heatmap_frame, text="Performance Heatmap", font=('Helvetica', 18, 'bold'), bg='white').pack(pady=(0, 20))
            # Generate and display the heatmap
        self.generate_heatmap()
        self.display_heatmap(heatmap_frame)
        
    def generate_heatmap(self):
        # dataset placeholder
        heatmap_data = pd.DataFrame({
            'id_student': [1, 2, 3, 4, 5],
            'date_1': [5, 3, 6, 2, 4],
            'date_2': [3, 6, 2, 5, 1],
            'date_3': [4, 2, 5, 3, 6]
        }).set_index('id_student')

        # Generate heatmap and save it
        plt.figure(figsize=(12, 8))
        sns.heatmap(heatmap_data, cmap='coolwarm', cbar=True)
        plt.title("Student Engagement Heatmap", fontsize=16)
        plt.xlabel("Date", fontsize=12)
        plt.ylabel("Student ID", fontsize=12)
        plt.savefig("Graphs/student_heatmap.png")
        plt.close()

    def display_heatmap(self, parent):
        try:
            # Load and display the heatmap
            image_path = "Graphs/student_heatmap.png"
            image = Image.open(image_path)
            image = image.resize((550, 400), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(parent, image=photo)
            label.image = photo
            label.pack()
        except Exception as e:
            print(f"Error displaying heatmap: {e}")



    def load_faqs_page(self):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # FAQs Header
        tk.Label(self.main_frame, text="Frequently Asked Questions", font=('Helvetica', 24)).pack(pady=20)

        # FAQs Content
        faqs = [
            ("What is this application?", "This application is a module dashboard for managing and viewing module data."),
            ("How do I navigate?", "Use the sidebar to switch between different pages like Dashboard, Modules, Students, etc."),
            ("Where can I find help?", "Visit the Help page for assistance and support."),
        ]

        # Display FAQs
        for question, answer in faqs:
            frame = tk.Frame(self.main_frame, bg='#D3C6B3', pady=10)
            frame.pack(fill='x', padx=20)
            tk.Label(frame, text=f"Q: {question}", font=('Helvetica', 16, 'bold'), bg='#D3C6B3').pack(anchor='w')
            tk.Label(frame, text=f"A: {answer}", font=('Helvetica', 14), bg='#D3C6B3').pack(anchor='w', padx=20)

    def load_help_page(self):
        # Placeholder for Help page content
        tk.Label(self.main_frame, text="Help Page", font=('Helvetica', 24)).pack(pady=20)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
