# main_window.py
import sys
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QSizePolicy, QTabWidget,
                             QTableWidget, QTableWidgetItem, QHeaderView, QSpacerItem,
                             QMenu, QMenuBar, QStatusBar, QCheckBox, QMessageBox,
                             QDateEdit, QAbstractItemView)
from PyQt6.QtCore import Qt, QSize, QDate
from PyQt6.QtGui import QFont, QColor, QPixmap, QIcon
from qtawesome import icon  # QtAwesome for Font Awesome icons

from production_tab.Auto_generate import AutoGenerateTab


# Import the separate tab class

class MainApplicationWindow(QMainWindow):
    def __init__(self, username="User"):
        super().__init__()
        self.setWindowTitle("MASTERBATCH PHILIPPINES INC.")
        self.setGeometry(100, 50, 1200, 800) # Adjusted size to fit more content
        self.username = username
        self.current_date = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")  # Use current date/time
        self.production_data = self.load_production_data()  # Load sample data
        self.formulation_data = self.load_formulation_data()
        self.setup_ui()
        self.apply_styles()
        self.center_window()

    def center_window(self):
        """Center the window on the screen."""
        screen_geometry = QApplication.primaryScreen().geometry()
        window_geometry = self.geometry()
        center_x = (screen_geometry.width() - window_geometry.width()) // 2
        center_y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(center_x, center_y)

    def load_production_data(self):
        """Load sample production data from screenshot - can be replaced with DB query."""
        return [
            ["10/04/25", "Everbright & Twine", "IA17079E", "GOLDEN BROWN", "16A01", "15.000000"],
            ["10/04/25", "Everbright Plastics Industry Inc.", "KA4795E", "FUCHSIA PINK", "15B7A-15A3N", "800.000000"],
            ["10/04/25", "FILIPINAS PLASTIC CORP. COMMODITIES, INC", "DP-1234E", "VIOLET", "820X-15A3N", "500.000000"],
            ["10/04/25", "TRADSPHERE PLASTIC CONTAINERS, INC", "YP-7894E", "YELLOW", "820X A", "1.500000"],
            ["10/04/25", "TRADSPHERE INDUSTRIAL COMMODITIES, INC", "DP-1044E", "LIGHT BLUE", "820X", "1.000000"],
            ["10/04/25", "PLASTICO, INC", "PP-6307E", "PEARL GREEN", "820X", "3.000000"]
        ]

    def load_formulation_data(self):
        """Load sample formulation data from screenshot."""
        return [
            ["G38", "0.310000", "0.000000", "3.680000", "0.031800", "3.648200"],
            ["G89", "1.000000", "5.000000", "6.000000", "0.106900", "5.893100"],
            ["I89", "0.500000", "2.500000", "3.000000", "0.050000", "2.950000"]
        ]

    def setup_ui(self):
        self.create_menu_bar()
        self.create_status_bar()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0) # Remove margins for cleaner look
        main_layout.setSpacing(0)

        # --- Top Header Section (USER: and Search) ---
        header_widget = QWidget()
        header_widget.setObjectName("header_widget")  # For styling
        header_layout = QHBoxLayout(header_widget)
        header_layout.setContentsMargins(10, 5, 10, 5)
        header_layout.setSpacing(10)
        header_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        user_label = QLabel(f"USER: {self.username}")
        user_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        header_layout.addWidget(user_label)

        header_layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)) # Spacer

        search_edit = QLineEdit()
        search_edit.setPlaceholderText("ID NUMBER, SEARCH")
        search_edit.setFixedSize(200, 25)
        search_edit.setFont(QFont("Arial", 9))
        search_edit.textChanged.connect(self.on_search_changed)  # Connect search functionality
        header_layout.addWidget(search_edit)

        search_button = QPushButton("SEARCH")
        search_button.setFixedSize(80, 25)
        search_button.setFont(QFont("Arial", 9, QFont.Weight.Bold))
        search_button.clicked.connect(self.perform_search)
        header_layout.addWidget(search_button)

        main_layout.addWidget(header_widget)

        # --- Tab Widget for Main Content ---
        self.tab_widget = QTabWidget()
        self.tab_widget.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        self.tab_widget.currentChanged.connect(self.on_tab_changed)  # Handle tab switch
        self.setup_production_records_tab()
        self.setup_auto_generate_tab()
        main_layout.addWidget(self.tab_widget)

        # --- Bottom Control Panel ---
        bottom_panel = QWidget()
        bottom_layout = QVBoxLayout(bottom_panel)
        bottom_layout.setContentsMargins(10, 10, 10, 10)
        bottom_layout.setSpacing(5)

        # First row of controls
        control_row1_layout = QHBoxLayout()
        control_row1_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.footer_label_left = QLabel(f"PRODUCTION ENCODED ON {self.current_date}")
        self.footer_label_left.setFont(QFont("Arial", 8))
        control_row1_layout.addWidget(self.footer_label_left)
        control_row1_layout.addSpacing(20)

        load_encoded_chk = QCheckBox("LOAD ENCODED ITEMS (for previous data)")
        load_encoded_chk.setFont(QFont("Arial", 8))
        load_encoded_chk.stateChanged.connect(self.on_checkbox_changed)
        control_row1_layout.addWidget(load_encoded_chk)

        date_old_label = QLabel("DATE OLD:")
        control_row1_layout.addWidget(date_old_label)
        date_old_edit = QLineEdit("10/04/2025 03:18 PM")
        date_old_edit.setFixedSize(120, 20)
        date_old_edit.setFont(QFont("Arial", 8))
        control_row1_layout.addWidget(date_old_edit)

        cust_z_label = QLabel("CUST NAME Z:")
        control_row1_layout.addWidget(cust_z_label)
        cust_z_edit = QLineEdit()
        cust_z_edit.setFixedSize(80, 20)
        cust_z_edit.setFont(QFont("Arial", 8))
        control_row1_layout.addWidget(cust_z_edit)

        prod_z_label = QLabel("PROD CODE Z:")
        control_row1_layout.addWidget(prod_z_label)
        prod_z_edit = QLineEdit()
        prod_z_edit.setFixedSize(80, 20)
        prod_z_edit.setFont(QFont("Arial", 8))
        control_row1_layout.addWidget(prod_z_edit)

        export_jbwy_btn = QPushButton("EXPORT JBWY")
        export_jbwy_btn.setFixedSize(100, 25)
        export_jbwy_btn.setFont(QFont("Arial", 8, QFont.Weight.Bold))
        export_jbwy_btn.clicked.connect(lambda: self.export_data("JBWY"))
        control_row1_layout.addWidget(export_jbwy_btn)

        control_row1_layout.addStretch()

        bottom_layout.addLayout(control_row1_layout)

        # Second row of controls
        control_row2_layout = QHBoxLayout()
        control_row2_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        load_cancelled_chk = QCheckBox("LOAD CANCELLED ITEMS (for viewing only)")
        load_cancelled_chk.setFont(QFont("Arial", 8))
        load_cancelled_chk.stateChanged.connect(self.on_checkbox_changed)
        control_row2_layout.addWidget(load_cancelled_chk)

        control_row2_layout.addSpacing(20)

        # This part looks like a password input
        export_password_label = QLabel("ADMIN PASSWORD")
        export_password_label.setFont(QFont("Arial", 8))
        control_row2_layout.addWidget(export_password_label)

        self.export_password_entry = QLineEdit()
        self.export_password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        self.export_password_entry.setFixedSize(100, 20)
        control_row2_layout.addWidget(self.export_password_entry)

        control_row2_layout.addStretch()

        old_export_jbwy_btn = QPushButton("OLD EXPORT JBWY")
        old_export_jbwy_btn.setFixedSize(120, 25)
        old_export_jbwy_btn.setFont(QFont("Arial", 8, QFont.Weight.Bold))
        old_export_jbwy_btn.clicked.connect(lambda: self.export_data("OLD JBWY"))
        control_row2_layout.addWidget(old_export_jbwy_btn)

        bottom_layout.addLayout(control_row2_layout)

        # Third row of controls (Date from, date to, Export, Refresh, View, Close)
        control_row3_layout = QHBoxLayout()
        control_row3_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        date_from_label = QLabel("DATE FROM: ")
        date_from_label.setFont(QFont("Arial", 8))
        control_row3_layout.addWidget(date_from_label)

        self.date_from_edit = QDateEdit()
        self.date_from_edit.setCalendarPopup(True)
        self.date_from_edit.setDate(QDate.currentDate())
        self.date_from_edit.setFixedSize(100, 25)
        self.date_from_edit.dateChanged.connect(self.on_date_changed)
        control_row3_layout.addWidget(self.date_from_edit)

        date_to_label = QLabel("DATE To: ")
        date_to_label.setFont(QFont("Arial", 8))
        control_row3_layout.addWidget(date_to_label)

        self.date_to_edit = QDateEdit()
        self.date_to_edit.setCalendarPopup(True)
        self.date_to_edit.setDate(QDate.currentDate())
        self.date_to_edit.setFixedSize(100, 25)
        self.date_to_edit.dateChanged.connect(self.on_date_changed)
        control_row3_layout.addWidget(self.date_to_edit)

        export_button = QPushButton("EXPORT")
        export_button.setFixedSize(80, 25)
        export_button.setFont(QFont("Arial", 8, QFont.Weight.Bold))
        export_button.clicked.connect(lambda: self.export_data("STANDARD"))
        control_row3_layout.addWidget(export_button)

        export_old_button = QPushButton("EXPORT-OLD")
        export_old_button.setFixedSize(80, 25)
        export_old_button.setFont(QFont("Arial", 8, QFont.Weight.Bold))
        export_old_button.clicked.connect(lambda: self.export_data("OLD"))
        control_row3_layout.addWidget(export_old_button)

        export_esa_button = QPushButton("EXPORT ESA")
        export_esa_button.setFixedSize(80, 25)
        export_esa_button.setFont(QFont("Arial", 8, QFont.Weight.Bold))
        export_esa_button.clicked.connect(lambda: self.export_data("ESA"))
        control_row3_layout.addWidget(export_esa_button)

        control_row3_layout.addStretch()

        refresh_button = QPushButton("REFRESH")
        refresh_button.setFixedSize(80, 25)
        refresh_button.setFont(QFont("Arial", 8, QFont.Weight.Bold))
        refresh_button.clicked.connect(self.refresh_data)
        control_row3_layout.addWidget(refresh_button)

        view_button = QPushButton("VIEW")
        view_button.setFixedSize(80, 25)
        view_button.setFont(QFont("Arial", 8, QFont.Weight.Bold))
        view_button.clicked.connect(self.view_data)
        control_row3_layout.addWidget(view_button)

        close_button = QPushButton("CLOSE")
        close_button.setFixedSize(80, 25)
        close_button.setFont(QFont("Arial", 8, QFont.Weight.Bold))
        close_button.clicked.connect(self.close)
        control_row3_layout.addWidget(close_button)

        bottom_layout.addLayout(control_row3_layout)

        main_layout.addWidget(bottom_panel)

    def setup_production_records_tab(self):
        tab_widget = QWidget()
        tab_layout = QVBoxLayout(tab_widget)
        tab_layout.setContentsMargins(10, 10, 10, 10)
        tab_layout.setSpacing(10)

        # Top of the tab: LOT NO, TRADSPHERE INDUSTRIAL COMMODITIES, ID NUMBER, SEARCH
        tab_header_layout = QHBoxLayout()
        tab_header_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        lot_no_label = QLabel("LOT NO.:")
        lot_no_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        tab_header_layout.addWidget(lot_no_label)

        self.lot_no_value_label = QLabel("8024X - TRADSPHERE INDUSTRIAL COMMODITIES")
        self.lot_no_value_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        self.lot_no_value_label.setStyleSheet("color: red;") # Red color as in screenshot
        tab_header_layout.addWidget(self.lot_no_value_label)

        id_number_label = QLabel("ID NUMBER")
        id_number_label.setFont(QFont("Arial", 8))
        tab_header_layout.addWidget(id_number_label)

        self.id_number_entry = QLineEdit()
        self.id_number_entry.setFixedSize(80, 20)
        self.id_number_entry.textChanged.connect(self.on_id_search)
        tab_header_layout.addWidget(self.id_number_entry)

        search_tab_label = QLabel("SEARCH")
        search_tab_label.setFont(QFont("Arial", 8))
        tab_header_layout.addWidget(search_tab_label)

        self.search_tab_entry = QLineEdit()
        self.search_tab_entry.setPlaceholderText("SEARCH")
        self.search_tab_entry.setFixedSize(120, 20)
        self.search_tab_entry.textChanged.connect(self.on_tab_search)
        tab_header_layout.addWidget(self.search_tab_entry)

        tab_header_layout.addStretch() # Push everything to the left

        tab_layout.addLayout(tab_header_layout)

        # Main Table (Top) - Production Records
        self.main_table = QTableWidget()
        self.populate_main_table()
        self.main_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.main_table.verticalHeader().setVisible(False)
        self.main_table.setFont(QFont("Arial", 9))
        self.main_table.setSortingEnabled(True)  # Enable sorting
        self.main_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.main_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.main_table.itemSelectionChanged.connect(self.on_table_selection_changed)
        tab_layout.addWidget(self.main_table)

        # VB Material Section (Bottom Table)
        vb_layout = QHBoxLayout()

        self.vb_table = QTableWidget()
        self.populate_vb_table()
        self.vb_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.vb_table.verticalHeader().setVisible(False)
        self.vb_table.setFont(QFont("Arial", 8))
        vb_layout.addWidget(self.vb_table)

        tab_layout.addLayout(vb_layout)

        # Icon placeholder (truck image)
        icon_label = QLabel()
        # icon_label.setPixmap(QPixmap("path/to/truck.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        icon_label.setText("🚛") # Placeholder emoji for truck
        icon_label.setFont(QFont("Arial", 30))
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setFixedSize(60, 60)
        tab_layout.addWidget(icon_label, alignment=Qt.AlignmentFlag.AlignRight)

        tab_layout.addStretch() # Push content up within the tab

        # Add tab with icon
        production_icon = icon('fa5s.industry', color='darkblue')
        production_qicon = QIcon(production_icon.pixmap(16, 16))
        self.tab_widget.addTab(tab_widget, production_qicon, "PRODUCTION RECORDS")

    def setup_auto_generate_tab(self):
        """Setup the Auto-Generate tab using the separate class."""
        auto_tab = AutoGenerateTab(self.username, self.current_date)
        generate_icon = icon('fa5s.cog', color='gray')
        generate_qicon = QIcon(generate_icon.pixmap(16, 16))
        self.tab_widget.addTab(auto_tab, generate_qicon, "AUTO-GENERATE PRODUCTION ENTRY")

    def populate_main_table(self):
        """Populate the main production table with data."""
        self.main_table.setRowCount(len(self.production_data))
        self.main_table.setColumnCount(6)
        self.main_table.setHorizontalHeaderLabels(["DATE", "CUSTOMER", "PRODUCT CODE", "PRODUCT COLOR", "LOT NO.", "QTY. PRODUCED"])
        for row, row_data in enumerate(self.production_data):
            for col, item_data in enumerate(row_data):
                item = QTableWidgetItem(str(item_data))
                item.setFont(QFont("Arial", 9))
                self.main_table.setItem(row, col, item)

    def populate_vb_table(self):
        """Populate the VB material table with data, including TOTAL LOSS column."""
        self.vb_table.setRowCount(len(self.formulation_data))
        self.vb_table.setColumnCount(6)
        self.vb_table.setHorizontalHeaderLabels(["MATERIAL NAME", "LARGE SCALE (KG)", "SMALL SCALE (KG)", "TOTAL WEIGHT (KG)", "TOTAL LOSS (KG)", "TOTAL CONSUMPTION (KG)"])
        for row, row_data in enumerate(self.formulation_data):
            for col, item_data in enumerate(row_data):
                item = QTableWidgetItem(str(item_data))
                item.setFont(QFont("Arial", 8))
                self.vb_table.setItem(row, col, item)

    # Event Handlers
    def on_search_changed(self, text):
        """Handle global search."""
        if len(text) > 2:  # Debounce-like
            self.perform_search()

    def perform_search(self):
        """Perform search across tables."""
        query = "ID NUMBER SEARCH"  # Placeholder
        QMessageBox.information(self, "Search", f"Searching for: {query}")

    def on_tab_search(self, text):
        """Tab-specific search."""
        # Implement filtering on main_table
        pass

    def on_id_search(self, text):
        """ID number search."""
        # Filter by ID
        pass

    def on_table_selection_changed(self):
        """Handle table row selection."""
        selected = self.main_table.selectedItems()
        if selected:
            row = selected[0].row()
            if row < len(self.production_data):
                self.lot_no_value_label.setText(self.production_data[row][4])  # Update lot no

    def on_tab_changed(self, index):
        """Handle tab change."""
        self.statusBar().showMessage(f"Switched to tab: {self.tab_widget.tabText(index)}")

    def on_checkbox_changed(self, state):
        """Handle checkbox changes - refresh filters."""
        self.refresh_data()

    def on_date_changed(self, date):
        """Handle date changes - filter data."""
        self.refresh_data()

    def refresh_data(self):
        """Refresh tables based on filters."""
        # Simplified: repopulate
        self.populate_main_table()
        self.populate_vb_table()
        self.statusBar().showMessage("Data refreshed.")

    def view_data(self):
        """Handle VIEW button - show detailed view."""
        QMessageBox.information(self, "View", "Viewing selected data...")

    def export_data(self, export_type):
        """Handle export with password check if needed."""
        password = self.export_password_entry.text()
        if "OLD" in export_type and password != "admin":
            QMessageBox.warning(self, "Access Denied", "Invalid admin password.")
            return
        # Simulate export
        QMessageBox.information(self, "Export", f"Exported data as {export_type}")

    def create_menu_bar(self):
        menu_bar = self.menuBar()
        menu_bar.setFont(QFont("Arial", 9, QFont.Weight.Bold))
        menu_bar.setStyleSheet("QMenuBar { background-color: #f0f0f0; color: #333333; }"
                              "QMenuBar::item:selected { background-color: #d0d0d0; }"
                              "QMenu { background-color: white; border: 1px solid #cccccc; }"
                              "QMenu::item:selected { background-color: #2196F3; color: white; }")

        file_menu = menu_bar.addMenu("&FILE")
        file_icon = icon('fa5s.folder-open', color='gray')
        file_qicon = QIcon(file_icon.pixmap(16, 16))
        file_menu.setIcon(file_qicon)

        view_menu = menu_bar.addMenu("&VIEW")
        view_icon = icon('fa5s.eye', color='gray')
        view_qicon = QIcon(view_icon.pixmap(16, 16))
        view_menu.setIcon(view_qicon)

        reports_menu = menu_bar.addMenu("&REPORTS")
        reports_icon = icon('fa5s.file-alt', color='gray')
        reports_qicon = QIcon(reports_icon.pixmap(16, 16))
        reports_menu.setIcon(reports_qicon)

        utilities_menu = menu_bar.addMenu("&UTILITIES")
        utilities_icon = icon('fa5s.wrench', color='gray')
        utilities_qicon = QIcon(utilities_icon.pixmap(16, 16))
        utilities_menu.setIcon(utilities_qicon)

        archive_menu = menu_bar.addMenu("&ARCHIVE")
        archive_icon = icon('fa5s.archive', color='gray')
        archive_qicon = QIcon(archive_icon.pixmap(16, 16))
        archive_menu.setIcon(archive_qicon)

        system_menu = menu_bar.addMenu("&SYSTEM")
        system_icon = icon('fa5s.cogs', color='gray')
        system_qicon = QIcon(system_icon.pixmap(16, 16))
        system_menu.setIcon(system_qicon)

        # Add actions with icons
        production_action = view_menu.addAction("PRODUCTION RECORDS")
        production_action_icon = icon('fa5s.industry', color='darkblue')
        production_action_icon_q = QIcon(production_action_icon.pixmap(16, 16))
        production_action.setIcon(production_action_icon_q)
        production_action.triggered.connect(lambda: self.tab_widget.setCurrentIndex(0))

        auto_gen_action = view_menu.addAction("AUTO-GENERATE")
        auto_gen_icon = icon('fa5s.cog', color='gray')
        auto_gen_icon_q = QIcon(auto_gen_icon.pixmap(16, 16))
        auto_gen_action.setIcon(auto_gen_icon_q)
        auto_gen_action.triggered.connect(lambda: self.tab_widget.setCurrentIndex(1))

        reports_menu.addAction("EXPORT REPORTS")

        utilities_menu.addAction("SYSTEM UTILITIES")

        archive_menu.addAction("VIEW ARCHIVES")

        system_menu.addAction("USER SETTINGS")

        file_menu.addSeparator()
        exit_action = file_menu.addAction("EXIT")
        exit_icon = icon('fa5s.sign-out-alt', color='red')
        exit_icon_q = QIcon(exit_icon.pixmap(16, 16))
        exit_action.setIcon(exit_icon_q)
        exit_action.triggered.connect(self.close)

    def create_status_bar(self):
        self.statusBar().setFont(QFont("Arial", 8))
        self.statusBar().setStyleSheet("QStatusBar { background-color: #f0f0f0; color: #555555; border-top: 1px solid #e0e0e0; }")
        self.statusBar().showMessage("MBPI SYSTEM 2025 NUM")  # Updated year

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                            stop:0 #c7e0f2, stop:0.3 #e0f2f7, stop:0.7 #f0f8ff, stop:1 #e0f2f7);
            }
            QWidget { /* Default for all widgets, can be overridden */
                font-family: Arial;
                font-size: 9pt;
                color: #333333;
            }
            #header_widget {
                background-color: #f0f0f0;
                border-bottom: 1px solid #cccccc;
            }
            QTabWidget::pane { /* The widget area below the tabs */
                border: 1px solid #a0a0a0;
                background-color: white;
            }
            QTabBar::tab {
                background: #e0e0e0;
                border: 1px solid #a0a0a0;
                border-bottom-color: #a0a0a0; /* same as pane border */
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
                min-width: 8ex;
                padding: 5px 10px;
                font-weight: bold;
                color: #555555;
            }
            QTabBar::tab:selected {
                background: white;
                border-bottom-color: white; /* Make the selected tab 'blend' with the pane */
                color: #2196F3;
            }
            QTabBar::tab:hover:!selected {
                background: #d0d0d0;
            }
            QTableWidget {
                border: 1px solid #cccccc;
                gridline-color: #e0e0e0;
                background-color: white;
                selection-background-color: #b0e0e6; /* Light blue selection */
                selection-color: black;
                alternate-background-color: #f9f9f9;
            }
            QTableWidget::item {
                padding: 3px;
            }
            QTableWidget::item:selected {
                background-color: #b0e0e6;
            }
            QTableWidget QHeaderView::section {
                background-color: #f0f0f0;
                border: 1px solid #cccccc;
                padding: 4px;
                font-weight: bold;
                color: #555555;
            }
            QLineEdit {
                border: 1px solid #cccccc;
                border-radius: 3px;
                padding: 3px;
                background-color: #f8f8f8;
            }
            QLineEdit:focus {
                border: 1px solid #2196F3;
                background-color: #e3f2fd;
            }
            QDateEdit {
                border: 1px solid #cccccc;
                border-radius: 3px;
                padding: 3px;
                background-color: #f8f8f8;
            }
            QDateEdit:focus {
                border: 1px solid #2196F3;
                background-color: #e3f2fd;
            }
            QPushButton {
                background-color: #0078d7; /* Windows blue */
                color: white;
                border: none;
                border-radius: 4px;
                padding: 5px 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056a0;
            }
            QPushButton:pressed {
                background-color: #003d7a;
            }
            QCheckBox {
                spacing: 5px;
            }
            QCheckBox::indicator {
                width: 13px;
                height: 13px;
                border: 1px solid #808080;
                border-radius: 2px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #2196F3;
                border: 1px solid #2196F3;
                image: none;
            }
        """)

    # Event Handlers (kept in main for now, but can be moved if needed)
    def on_search_changed(self, text):
        """Handle global search."""
        if len(text) > 2:  # Debounce-like
            self.perform_search()

    def perform_search(self):
        """Perform search across tables."""
        query = "ID NUMBER SEARCH"  # Placeholder
        QMessageBox.information(self, "Search", f"Searching for: {query}")

    def on_tab_search(self, text):
        """Tab-specific search."""
        # Implement filtering on main_table
        pass

    def on_id_search(self, text):
        """ID number search."""
        # Filter by ID
        pass

    def on_table_selection_changed(self):
        """Handle table row selection."""
        selected = self.main_table.selectedItems()
        if selected:
            row = selected[0].row()
            if row < len(self.production_data):
                self.lot_no_value_label.setText(self.production_data[row][4])  # Update lot no

    def on_tab_changed(self, index):
        """Handle tab change."""
        self.statusBar().showMessage(f"Switched to tab: {self.tab_widget.tabText(index)}")

    def on_checkbox_changed(self, state):
        """Handle checkbox changes - refresh filters."""
        self.refresh_data()

    def on_date_changed(self, date):
        """Handle date changes - filter data."""
        self.refresh_data()

    def refresh_data(self):
        """Refresh tables based on filters."""
        # Simplified: repopulate
        self.populate_main_table()
        self.populate_vb_table()
        self.statusBar().showMessage("Data refreshed.")

    def view_data(self):
        """Handle VIEW button - show detailed view."""
        QMessageBox.information(self, "View", "Viewing selected data...")

    def export_data(self, export_type):
        """Handle export with password check if needed."""
        password = self.export_password_entry.text()
        if "OLD" in export_type and password != "admin":
            QMessageBox.warning(self, "Access Denied", "Invalid admin password.")
            return
        # Simulate export
        QMessageBox.information(self, "Export", f"Exported data as {export_type}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApplicationWindow(username="Admin")  # Simulate logged-in user
    window.show()
    sys.exit(app.exec())