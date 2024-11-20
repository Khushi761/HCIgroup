import tkinter as tk


def create_main_window():
    root = tk.Tk()
    root.title("Learning Analytics Dashboard")
    root.geometry("1000x600")
    root.configure(bg="lightgray")

    # Configure the grid layout
    root.grid_rowconfigure(1, weight=1)  # Make the content area row expandable
    root.grid_columnconfigure(1, weight=1)  # Make the content area column expandable

    # Top bar
    topbar = tk.Frame(root, bg="white", height=50)
    topbar.grid(row=0, column=0, columnspan=2, sticky="new")  # Topbar spans both columns

    # Search bar
    search_entry = tk.Entry(topbar, width=40, relief="flat", font=("Arial", 14))
    search_entry.pack(pady=10, padx=10, side=tk.LEFT)

    # Profile icon
    profile_icon = tk.Canvas(topbar, width=30, height=30, bg="white", highlightthickness=0)
    profile_icon.create_oval(5, 5, 25, 25, fill="gray")
    profile_icon.pack(side=tk.RIGHT, padx=20, pady=10)

    # Sidebar
    sidebar = tk.Frame(root, bg="#D2B48C", width=200)
    sidebar.grid(row=1, column=0, sticky="ns")

    # Content area
    content_area = tk.Frame(root, bg="#F5F5DC")
    content_area.grid(row=1, column=1, sticky="nsew")

    def clear_content():
        """Clears the content area for new content."""
        for widget in content_area.winfo_children():
            widget.destroy()

    def load_dashboard():
        """Loads the dashboard page."""
        clear_content()
        tk.Label(content_area, text="Student Regions Map", bg="#F5F5DC", relief="groove", height=3).pack(
            fill=tk.X, pady=10, padx=10
        )

        frame = tk.Frame(content_area, bg="#F5F5DC")
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(frame, text="Student Performance Heatmap", bg="#F5F5DC", relief="groove").pack(
            side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5
        )
        tk.Label(frame, text="Factors Affecting Performance", bg="#F5F5DC", relief="groove").pack(
            side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5
        )

    def load_students():
        """Loads the students page."""
        clear_content()
        stats_frame = tk.Frame(content_area, bg="#F5F5DC", padx=10, pady=10)
        stats_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        tk.Label(stats_frame, text="Student Stats", bg="white", fg="black", font=("Arial", 14, "bold"), relief="groove").pack(
            fill=tk.X, pady=5
        )

        # Student stats fields
        stats_fields = [
            "Age Band: 18-25",
            "Gender: Female",
            "Region: Europe",
            "Number of Credits: 60",
            "Highest Qualification: Bachelor's Degree",
            "Disability: None",
            "No. of Attempts: 1",
            "Final Result: Pass",
            "Presentation Code: AAA-2024",
        ]

        for field in stats_fields:
            tk.Label(stats_frame, text=field, bg="#F5F5DC", anchor="w", padx=10, font=("Arial", 12)).pack(
                fill=tk.X, pady=2
            )

    def load_modules():
        """Loads the modules page."""
        clear_content()
        tk.Label(content_area, text="Module Stats", bg="#F5F5DC", relief="groove", height=3).pack(
            fill=tk.X, pady=10, padx=10
        )

        frame = tk.Frame(content_area, bg="#F5F5DC")
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(frame, text="Student Performance Chart", bg="#F5F5DC", relief="groove").pack(
            side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5
        )
        tk.Label(frame, text="Gender Split in Modules", bg="#F5F5DC", relief="groove").pack(
            side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5
        )

    def load_faqs():
        """Loads the FAQs page."""
        clear_content()
        tk.Label(content_area, text="FAQs", bg="#F5F5DC", relief="groove", height=20).pack(
            fill=tk.BOTH, expand=True, padx=10, pady=10
        )

    def load_help():
        """Loads the Help page."""
        clear_content()
        tk.Label(content_area, text="Help Page", bg="#F5F5DC", relief="groove", height=20).pack(
            fill=tk.BOTH, expand=True, padx=10, pady=10
        )

    # Sidebar buttons with commands
    buttons = [
        ("Dashboard", load_dashboard),
        ("Modules", load_modules),
        ("Students", load_students),
        ("FAQs", load_faqs),
        ("Help", load_help),
    ]

    for text, command in buttons:
        button = tk.Button(sidebar, text=text, bg="#D2B48C", relief="flat", anchor="w", padx=20, command=command)
        button.pack(fill=tk.X, pady=2)

    # Load default section
    load_dashboard()

    root.mainloop()


if __name__ == "__main__":
    create_main_window()


