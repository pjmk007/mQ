# src/main.py
import tkinter as tk
from tkinter import ttk

from src.controllers.logic import initialize_app

# from src.controllers.event_dispatcher import dispatch_event
from src.views.logging_utils import (
    setup_logging_frame,
)  # Import the logging setup function

from src.views.treeview_utils import *
from src.views.styles import configure_tab_styles
from src.views.notebook_tabs import (
    create_familyType_manage_tab,
    create_project_standard_tab,
    create_team_standard_tab,
    create_notebook_with_tabs,
)


def main():

    # Initialize the main Tkinter window
    root = tk.Tk()
    root.title("H_bimNote")
    root.iconbitmap("resources/favicon_io/favicon.ico")
    # root.geometry("1400x900")
    m = root.maxsize()
    # root.geometry("1400x900".format(*m))
    root.geometry(
        "{}x{}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight())
    )

    # Open the window in full screen
    # root.attributes("-fullscreen", True)
    root.state("zoomed")  # Maximizes the window while keeping window controls visible
    # root.state()

    configure_tab_styles()  # Configure the tab style
    # Set up the logging area and get the logging text widget
    logging_text_widget = setup_logging_frame(root)

    # Log the start of loading
    logging_text_widget.write("Configuring system...\n")

    # state
    app_state, wm_group_manager = initialize_app(logging_text_widget)

    # app_state.current_loaded_pjt = tk.StringVar()
    app_state["current_loaded_pjt"] = tk.StringVar()
    app_state["current_loaded_pjt"].set("project file not loaded yet")
    app_state.root = root

    # Create the notebook (tab container)
    main_notebook = create_notebook_with_tabs(root, app_state)
    main_notebook.pack(fill="both", expand=True)

    # Create upper-level tabs: Team Standard and Project Standard
    create_team_standard_tab(root, main_notebook, app_state, wm_group_manager)
    create_project_standard_tab(main_notebook, app_state)
    create_familyType_manage_tab(main_notebook, app_state)

    # # Debugging: Print statement to confirm main function is running
    logging_text_widget.write("안녕하세요. 어플리케이션이 시작 되었습니다.\n")
    main_notebook.select(1)

    # Start the main loop
    root.mainloop()


if __name__ == "__main__":
    main()
