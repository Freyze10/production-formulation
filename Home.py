import sys
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QSizePolicy, QTabWidget,
                             QTableWidget, QTableWidgetItem, QHeaderView, QSpacerItem,
                             QMenu, QMenuBar, QStatusBar, QCheckBox, QMessageBox,
                             QDateEdit, QAbstractItemView, QFrame, QScrollArea, QComboBox,
                             QFormLayout, QTextEdit)
from PyQt6.QtCore import Qt, QSize, QDate, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QFont, QColor, QPixmap, QIcon, QPalette
from qtawesome import icon  # QtAwesome for Font Awesome icons


class ModernButton(QPushButton):
    """Custom modern button with hover effect."""

    def __init__(self, text, primary=False):
        super().__init__(text)
        self.primary = primary
        self.setup_style()

    def setup_style(self):
        if self.primary:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #2196F3;
                    color: white;
                    border: none;
                    border-radius: 6px;
                    padding: 8px 16px;
                    font-weight: 600;
                    font-size: 9pt;
                }
                QPushButton:hover {
                    background-color: #1976D2;
                }
                QPushButton:pressed {
                    background-color: #0D47A1;
                }
            """)
        else:
            self.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    color: #424242;
                    border: 1px solid #E0E0E0;
                    border-radius: 6px;
                    padding: 8px 16px;
                    font-weight: 500;
                    font-size: 9pt;
                }
                QPushButton:hover {
                    background-color: #F5F5F5;
                    border-color: #BDBDBD;
                }
                QPushButton:pressed {
                    background-color: #EEEEEE;
                }
            """)


class AutoGenerateTab(QWidget):
    def __init__(self, username, current_date, main_window):
        super().__init__()
        self.username = username
        self.current_date = current_date
        self.main_window = main_window
        self.formulation_data = self.load_formulation_data()
        self.setup_ui()

    def load_formulation_data(self):
        """Load sample formulation data."""
        return [
            ["B107", "2.500000", "0.000000", "2.5000000", "0.025000", "2.475000"],
            ["B37", "4.000000", "0.000000", "1.5000000", "0.015000", "1.485000"],
            ["L28", "5.000000", "0.000000", "1.0000000", "0.010000", "0.990000"]
        ]

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 10, 20, 10)
        layout.setSpacing(8)

        # Title Card
        title_card = QFrame()
        title_card.setObjectName("card")
        title_layout = QHBoxLayout(title_card)
        title_layout.setContentsMargins(20, 8, 20, 8)

        # Main Content Layout
        main_content = QHBoxLayout()
        main_content.setSpacing(10)

        # Middle: Form Fields Card
        middle_card = QFrame()
        middle_card.setObjectName("card")
        middle_layout = QVBoxLayout(middle_card)
        middle_layout.setContentsMargins(15, 15, 15, 15)
        middle_layout.setSpacing(5)

        form_title = QLabel("Form Details")
        form_title.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        form_title.setStyleSheet("color: #1976D2;")
        middle_layout.addWidget(form_title, 2)

        form_widget = QWidget()
        form_layout = QFormLayout(form_widget)
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form_layout.setHorizontalSpacing(8)
        form_layout.setVerticalSpacing(3)
        form_layout.setContentsMargins(0, 0, 0, 0)

        # Field styling adjusted to match theme
        field_style = "background-color: #FFF3E0; border: 1px solid #FF9800; border-radius: 4px; padding: 4px;"
        white_field_style = "background-color: #FAFAFA; border: 1px solid #E0E0E0; border-radius: 4px; padding: 4px;"
        field_width = 180
        field_height = 24

        # Product Code
        product_code_layout = QHBoxLayout()
        self.product_code_combo = QComboBox()
        self.product_code_combo.setEditable(True)
        self.product_code_combo.setCurrentText("BA0830E")
        self.product_code_combo.setFixedSize(field_width, field_height)
        self.product_code_combo.setStyleSheet(field_style)
        product_code_layout.addWidget(self.product_code_combo)
        product_code_layout.addStretch()
        form_layout.addRow("PRODUCT CODE *", product_code_layout)

        # Product Color
        self.product_color_edit = QLineEdit("BLUE")
        self.product_color_edit.setFixedSize(field_width, field_height)
        self.product_color_edit.setStyleSheet(white_field_style)
        form_layout.addRow("PRODUCT COLOR", self.product_color_edit)

        # Dosage and LD(%)
        dosage_layout = QHBoxLayout()
        dosage_layout.setSpacing(5)
        self.dosage_edit = QLineEdit("100.00000")
        self.dosage_edit.setFixedSize(100, field_height)
        self.dosage_edit.setStyleSheet(field_style)
        dosage_layout.addWidget(self.dosage_edit)

        ld_label = QLabel("LD (%)")
        ld_label.setFont(QFont("Segoe UI", 8))
        dosage_layout.addWidget(ld_label)

        self.ld_edit = QLineEdit("0.40000")
        self.ld_edit.setFixedSize(80, field_height)
        self.ld_edit.setStyleSheet(white_field_style)
        dosage_layout.addWidget(self.ld_edit)
        dosage_layout.addStretch()
        form_layout.addRow("DOSAGE *", dosage_layout)

        # Customer
        self.customer_combo = QComboBox()
        self.customer_combo.setEditable(True)
        self.customer_combo.setCurrentText("Una Internationale")
        self.customer_combo.setFixedSize(field_width, field_height)
        self.customer_combo.setStyleSheet(field_style)
        form_layout.addRow("CUSTOMER *", self.customer_combo)

        # Lot No.
        self.lot_no_combo = QComboBox()
        self.lot_no_combo.setEditable(True)
        self.lot_no_combo.setFixedSize(field_width, field_height)
        self.lot_no_combo.setStyleSheet(field_style)
        form_layout.addRow("LOT NO. *", self.lot_no_combo)

        # Tentative Production Date
        self.tentative_date_edit = QLineEdit("  /  /")
        self.tentative_date_edit.setFixedSize(field_width, field_height)
        self.tentative_date_edit.setStyleSheet(field_style)
        form_layout.addRow("TENTATIVE PRODUCTION DATE *", self.tentative_date_edit)

        # Confirmation Date for Inventory Only
        self.confirm_date_edit = QLineEdit("  /  /")
        self.confirm_date_edit.setFixedSize(field_width, field_height)
        self.confirm_date_edit.setStyleSheet(white_field_style)
        form_layout.addRow("CONFIRMATION DATE FOR INVENTORY ONLY *", self.confirm_date_edit)

        # Order Form No.
        self.order_form_combo = QComboBox()
        self.order_form_combo.setEditable(True)
        self.order_form_combo.setFixedSize(field_width, field_height)
        self.order_form_combo.setStyleSheet(field_style)
        form_layout.addRow("ORDER FORM NO. *", self.order_form_combo)

        # Colormatch No.
        self.colormatch_no_edit = QLineEdit("-")
        self.colormatch_no_edit.setFixedSize(field_width, field_height)
        self.colormatch_no_edit.setStyleSheet(white_field_style)
        form_layout.addRow("COLORMATCH NO.", self.colormatch_no_edit)

        # Matched Date
        self.matched_date_edit = QLineEdit("02/14/2025")
        self.matched_date_edit.setFixedSize(field_width, field_height)
        self.matched_date_edit.setStyleSheet(white_field_style)
        form_layout.addRow("MATCHED DATE", self.matched_date_edit)

        # Formulation ID
        self.formulation_id_edit = QLineEdit("16026")
        self.formulation_id_edit.setFixedSize(field_width, field_height)
        self.formulation_id_edit.setStyleSheet(white_field_style)
        form_layout.addRow("FORMULATION ID", self.formulation_id_edit)

        # Mixing Time
        self.mixing_time_edit = QLineEdit("-")
        self.mixing_time_edit.setFixedSize(field_width, field_height)
        self.mixing_time_edit.setStyleSheet(white_field_style)
        form_layout.addRow("MIXING TIME", self.mixing_time_edit)

        # Machine No.
        self.machine_no_edit = QLineEdit()
        self.machine_no_edit.setFixedSize(field_width, field_height)
        self.machine_no_edit.setStyleSheet(white_field_style)
        form_layout.addRow("MACHINE NO.", self.machine_no_edit)

        # QTY. REQ.
        self.qty_req_edit = QLineEdit("0.0000000")
        self.qty_req_edit.setFixedSize(field_width, field_height)
        self.qty_req_edit.setStyleSheet(field_style)
        form_layout.addRow("QTY. REQ. *", self.qty_req_edit)

        # QTY. PER BATCH
        self.qty_per_batch_edit = QLineEdit("0.0000000")
        self.qty_per_batch_edit.setFixedSize(field_width, field_height)
        self.qty_per_batch_edit.setStyleSheet(field_style)
        form_layout.addRow("QTY. PER BATCH *", self.qty_per_batch_edit)

        # Prepared By
        self.prepared_by_combo = QComboBox()
        self.prepared_by_combo.setEditable(True)
        self.prepared_by_combo.setFixedSize(field_width, field_height)
        self.prepared_by_combo.setStyleSheet(field_style)
        form_layout.addRow("PREPARED BY *", self.prepared_by_combo)

        # Notes
        self.notes_edit = QTextEdit()
        self.notes_edit.setFixedHeight(40)
        self.notes_edit.setStyleSheet(white_field_style)
        form_layout.addRow("NOTES", self.notes_edit)

        middle_layout.addWidget(form_widget)
        main_content.addWidget(middle_card, 3)

        # Right Side: Form Type, Production ID, and Materials Card
        right_card = QFrame()
        right_card.setObjectName("card")
        right_layout = QVBoxLayout(right_card)
        right_layout.setContentsMargins(15, 15, 15, 15)
        right_layout.setSpacing(8)

        # Form Type Row
        form_type_layout = QHBoxLayout()
        form_type_label = QLabel("FORM TYPE")
        form_type_label.setFont(QFont("Segoe UI", 9))
        form_type_layout.addWidget(form_type_label)

        self.form_type_combo = QComboBox()
        self.form_type_combo.setFixedSize(150, field_height)
        self.form_type_combo.setStyleSheet(field_style)
        form_type_layout.addWidget(self.form_type_combo)
        form_type_layout.addStretch()
        right_layout.addLayout(form_type_layout)

        # Production ID
        prod_id_layout = QHBoxLayout()
        prod_id_label = QLabel("PRODUCTION ID")
        prod_id_label.setFont(QFont("Segoe UI", 9))
        prod_id_layout.addWidget(prod_id_label)

        self.production_id_label = QLabel("0098744")
        self.production_id_label.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        self.production_id_label.setStyleSheet("color: #2196F3;")
        prod_id_layout.addWidget(self.production_id_label)
        prod_id_layout.addStretch()
        right_layout.addLayout(prod_id_layout)

        # Materials Table
        headers = ["Material Name", "Large Scale (KG.)", "Small Scale (G.)", "Total Weight (KG.)", "Total Loss (KG.)", "Total Consumption (KG.)"]
        self.materials_table = QTableWidget()
        self.materials_table.setRowCount(len(self.formulation_data))
        self.materials_table.setColumnCount(6)
        self.materials_table.setHorizontalHeaderLabels(headers)

        # Modern table styling
        self.materials_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.materials_table.verticalHeader().setVisible(False)
        self.materials_table.setAlternatingRowColors(True)
        self.materials_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.materials_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.materials_table.setFont(QFont("Segoe UI", 9))
        self.materials_table.horizontalHeader().setFont(QFont("Segoe UI", 7, QFont.Weight.Bold))
        self.materials_table.setMinimumHeight(250)
        self.materials_table.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #1976D2;
                color: white;
                padding: 4px;
                border: none;
                font-weight: bold;
            }
        """)

        # Populate table
        for row, row_data in enumerate(self.formulation_data):
            for col, item_data in enumerate(row_data):
                item = QTableWidgetItem(str(item_data))
                item.setFont(QFont("Segoe UI", 9))
                self.materials_table.setItem(row, col, item)

        right_layout.addWidget(self.materials_table)

        # Bottom stats section
        stats_layout = QVBoxLayout()
        stats_layout.setSpacing(3)

        items_label = QLabel("NO. OF ITEMS :  0")
        items_label.setFont(QFont("Segoe UI", 8, QFont.Weight.Bold))
        stats_layout.addWidget(items_label)

        weight_label = QLabel("TOTAL WEIGHT  : 0.000000")
        weight_label.setFont(QFont("Segoe UI", 8, QFont.Weight.Bold))
        stats_layout.addWidget(weight_label)

        fg_label = QLabel("FG in 1D (FOR WH) ONLY")
        fg_label.setFont(QFont("Segoe UI", 7))
        stats_layout.addWidget(fg_label)

        right_layout.addLayout(stats_layout)
        right_layout.addStretch()

        main_content.addWidget(right_card, 7)

        layout.addLayout(main_content)

        # Cancel Button
        cancel_btn = ModernButton("CLICK HERE TO CANCEL THIS PRODUCTION")
        cancel_btn.setStyleSheet("QPushButton { color: #2196F3; background: transparent; border: none; text-decoration: underline; }")
        layout.addWidget(cancel_btn, alignment=Qt.AlignmentFlag.AlignRight)

        # Encoded By Section Card
        encoded_card = QFrame()
        encoded_card.setObjectName("card")
        encoded_layout = QHBoxLayout(encoded_card)
        encoded_layout.setContentsMargins(20, 8, 20, 8)

        encoded_by_label = QLabel("ENCODED BY")
        encoded_by_label.setFont(QFont("Segoe UI", 9))
        encoded_layout.addWidget(encoded_by_label)

        prod_confirm_label = QLabel("PRODUCTION CONFIRMATION ENCODED ON")
        prod_confirm_label.setFont(QFont("Segoe UI", 9))
        encoded_layout.addWidget(prod_confirm_label)

        self.confirm_encoded_edit = QLineEdit("0000000")
        self.confirm_encoded_edit.setFixedSize(120, field_height)
        self.confirm_encoded_edit.setStyleSheet(field_style)
        encoded_layout.addWidget(self.confirm_encoded_edit)

        encoded_layout.addStretch()
        layout.addWidget(encoded_card)

        # Bottom Section with Date and Buttons Card
        bottom_card = QFrame()
        bottom_card.setObjectName("card")
        bottom_layout = QHBoxLayout(bottom_card)
        bottom_layout.setContentsMargins(20, 8, 20, 8)

        date_prod_layout = QVBoxLayout()
        date_label = QLabel(self.current_date)
        date_label.setFont(QFont("Segoe UI", 8))
        date_prod_layout.addWidget(date_label)

        prod_encoded_layout = QHBoxLayout()
        prod_encoded_label = QLabel("PRODUCTION ENCODED ON")
        prod_encoded_label.setFont(QFont("Segoe UI", 8))
        prod_encoded_layout.addWidget(prod_encoded_label)

        self.prod_encoded_edit = QLineEdit("  /  /")
        self.prod_encoded_edit.setFixedSize(100, field_height)
        self.prod_encoded_edit.setStyleSheet(white_field_style)
        prod_encoded_layout.addWidget(self.prod_encoded_edit)
        prod_encoded_layout.addStretch()

        date_prod_layout.addLayout(prod_encoded_layout)
        bottom_layout.addLayout(date_prod_layout, 3)

        bottom_layout.addStretch()

        # Action Buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(3)

        buttons = [
            ("GENERATE", True),
            ("TUMBLER", False),
            ("GENERATE ADVANCE", False),
            ("PRINT", False),
            ("NEW", False),
            ("CLOSE", False)
        ]

        for btn_text, is_primary in buttons:
            btn_width = 120 if btn_text == "GENERATE ADVANCE" else 80 if btn_text == "GENERATE" or btn_text == "TUMBLER" else 60
            btn = ModernButton(btn_text, primary=is_primary)
            btn.setFixedSize(btn_width, 25)
            if btn_text == "CLOSE":
                btn.clicked.connect(self.main_window.close)
            btn_layout.addWidget(btn)

        bottom_layout.addLayout(btn_layout)
        layout.addWidget(bottom_card)


class MainApplicationWindow(QMainWindow):
    def __init__(self, username="User"):
        super().__init__()
        self.setWindowTitle("MASTERBATCH PHILIPPINES INC. - Production Management System")
        self.setGeometry(100, 50, 1600, 900)
        self.username = username
        self.current_date = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
        self.production_data = self.load_production_data()
        self.formulation_data = self.load_formulation_data()
        self.setup_ui()
        self.apply_styles()
        self.center_window()

    def switch_to_tab(self, index):
        if hasattr(self, 'tab_widget'):
            self.tab_widget.setCurrentIndex(index)

    def center_window(self):
        """Center the window on the screen."""
        screen_geometry = QApplication.primaryScreen().geometry()
        window_geometry = self.geometry()
        center_x = (screen_geometry.width() - window_geometry.width()) // 2
        center_y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(center_x, center_y)

    def load_production_data(self):
        """Load sample production data."""
        return [
            ["10/06/25", "TRADESPHERE INDUSTRIAL COMMODITIES, INC.", "PP-W9845E", "White", "8211X", "2.5000000"],
            ["10/06/25", "PLACEL MFG. CO., INC.", "PP-V0669E", "PEARL VIOLET", "8210X", "1.0200000"],
            ["10/06/25", "In House", "VA4086E", "VIOLET", "1619AN", "125.0000000"],
            ["10/03/25", "ROWELL LITHOGRAPHY & METAL CLOSURE, INC.", "DE-B17719E", "BLUE", "8196X", "5.0000000"],
            ["10/06/25", "In House", "VA4086E", "VIOLET", "1618AN", "70.6200000"],
            ["10/06/25", "In House", "VA4086E", "VIOLET", "1617AN", "50.0000000"],
            ["10/06/25", "TRADESPHERE INDUSTRIAL COMMODITIES, INC.", "DP-K16339E", "PINK", "8209X", "1.0400000"],
            ["10/04/25", "Everbright Net & Twine", "IA1770E", "GOLDEN BROWN", "1616AN", "15.0000000"],
            ["10/04/25", "Everbright Net & Twine", "IA1770E", "GOLDEN BROWN", "1584AN-1615AN", "800.0000000"],
            ["10/04/25", "EVERGOOD PLASTIC INDUSTRY INC.", "KA4595E", "FUCHSIA PINK", "1574AN-1583AN", "500.0000000"],
            ["10/04/25", "FILIPINAS PLASTIC CORP.", "DU-B12434E", "BLUE", "8208X", "40.0000000"]
        ]

    def load_formulation_data(self):
        """Load sample formulation data."""
        return [
            ["B107", "2.500000", "0.000000", "2.5000000", "0.025000", "2.475000"],
            ["B37", "4.000000", "0.000000", "1.5000000", "0.015000", "1.485000"],
            ["L28", "5.000000", "0.000000", "1.0000000", "0.010000", "0.990000"]
        ]

    def setup_ui(self):
        self.create_menu_bar()
        self.create_status_bar()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Modern Header
        header = self.create_header()
        main_layout.addWidget(header)

        # Tab Widget
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.TabPosition.North)

        # First Tab: Production Overview
        tab1 = QWidget()
        tab1_layout = QVBoxLayout(tab1)
        tab1_layout.setContentsMargins(20, 10, 20, 10)
        tab1_layout.setSpacing(10)

        # Search and Filter Card
        search_card = self.create_search_card()
        tab1_layout.addWidget(search_card)

        # Main Content Area
        main_content = QHBoxLayout()
        main_content.setSpacing(10)

        # Production Table Card
        prod_card = self.create_production_card()
        main_content.addWidget(prod_card, 8)

        # Side Panel
        side_panel = self.create_side_panel()
        main_content.addWidget(side_panel, 2)

        tab1_layout.addLayout(main_content)

        # Materials Section
        materials_card = self.create_materials_card()
        tab1_layout.addWidget(materials_card)

        # Bottom Controls
        bottom_controls = self.create_bottom_controls()
        tab1_layout.addWidget(bottom_controls)

        self.tab_widget.addTab(tab1, "Production Records")

        # Second Tab: Auto Generate
        tab2 = AutoGenerateTab(self.username, self.current_date, self)
        self.tab_widget.addTab(tab2, "Auto Generate")

        main_layout.addWidget(self.tab_widget)

    def create_header(self):
        """Create modern header with gradient."""
        header = QFrame()
        header.setObjectName("headerFrame")
        header.setFixedHeight(80)

        layout = QHBoxLayout(header)
        layout.setContentsMargins(30, 10, 30, 10)

        # Left: Logo and Title
        left_layout = QVBoxLayout()
        title = QLabel("Production Management")
        title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        title.setStyleSheet("color: white;")
        left_layout.addWidget(title)

        subtitle = QLabel("Auto Generate Records - With Consumption")
        subtitle.setFont(QFont("Segoe UI", 10))
        subtitle.setStyleSheet("color: rgba(255, 255, 255, 0.8);")
        left_layout.addWidget(subtitle)

        layout.addLayout(left_layout)
        layout.addStretch()

        # Right: User info
        user_frame = QFrame()
        user_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.15);
                border-radius: 8px;
                padding: 5px 15px;
            }
        """)
        user_layout = QHBoxLayout(user_frame)
        user_layout.setSpacing(10)

        user_icon = QLabel("👤")
        user_icon.setFont(QFont("Segoe UI", 16))
        user_layout.addWidget(user_icon)

        user_info = QVBoxLayout()
        user_name = QLabel(self.username)
        user_name.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        user_name.setStyleSheet("color: white;")
        user_info.addWidget(user_name)

        user_date = QLabel(self.current_date)
        user_date.setFont(QFont("Segoe UI", 8))
        user_date.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
        user_info.addWidget(user_date)

        user_layout.addLayout(user_info)
        layout.addWidget(user_frame)

        return header

    def create_search_card(self):
        """Create search and filter card."""
        card = QFrame()
        card.setObjectName("card")
        layout = QHBoxLayout(card)
        layout.setContentsMargins(20, 12, 20, 12)
        layout.setSpacing(15)

        # LOT NO Display
        lot_label = QLabel("LOT NO:")
        lot_label.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        layout.addWidget(lot_label)

        self.lot_no_value = QLabel("8196X - ROWELL LITHOGRAPHY & METAL CLOSURE")
        self.lot_no_value.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        self.lot_no_value.setStyleSheet("color: #2196F3;")
        layout.addWidget(self.lot_no_value)

        layout.addStretch()

        # Search Fields
        search_layout = QHBoxLayout()
        search_layout.setSpacing(10)

        self.lot_number_edit = QLineEdit()
        self.lot_number_edit.setPlaceholderText("🔍 Search by Lot Number...")
        self.lot_number_edit.setFixedWidth(200)
        self.lot_number_edit.setFixedHeight(36)
        search_layout.addWidget(self.lot_number_edit)

        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("🔍 Search anything...")
        self.search_edit.setFixedWidth(200)
        self.search_edit.setFixedHeight(36)
        search_layout.addWidget(self.search_edit)

        search_btn = ModernButton("Search", primary=True)
        search_btn.setFixedHeight(36)
        search_layout.addWidget(search_btn)

        layout.addLayout(search_layout)

        return card

    def create_production_card(self):
        """Create production records table card."""
        card = QFrame()
        card.setObjectName("card")
        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setSpacing(10)

        # Header
        header_layout = QHBoxLayout()
        title = QLabel("📊 Production Records")
        title.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        header_layout.addWidget(title)

        header_layout.addStretch()

        layout.addLayout(header_layout)

        # Table
        self.production_table = QTableWidget()
        self.production_table.setRowCount(len(self.production_data))
        self.production_table.setColumnCount(6)
        self.production_table.setHorizontalHeaderLabels([
            "Date", "Customer", "Product Code", "Color", "Lot No.", "Qty Produced"
        ])

        # Modern table styling
        self.production_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.production_table.verticalHeader().setVisible(False)
        self.production_table.setAlternatingRowColors(True)
        self.production_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.production_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.production_table.setFont(QFont("Segoe UI", 9))
        self.production_table.horizontalHeader().setFont(QFont("Segoe UI", 8, QFont.Weight.Bold))
        self.production_table.setMaximumHeight(250)

        # Populate table
        for row, row_data in enumerate(self.production_data):
            for col, item_data in enumerate(row_data):
                item = QTableWidgetItem(str(item_data))
                item.setFont(QFont("Segoe UI", 9))
                self.production_table.setItem(row, col, item)
                if row == 3:  # Highlight selected row
                    item.setBackground(QColor("#E3F2FD"))

        layout.addWidget(self.production_table)

        return card

    def create_side_panel(self):
        """Create side panel with stats and actions."""
        panel = QFrame()
        panel.setObjectName("sidePanel")
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(15, 10, 15, 10)
        layout.setSpacing(10)

        # Stats Card
        stats_card = QFrame()
        stats_card.setObjectName("statsCard")
        stats_layout = QVBoxLayout(stats_card)
        stats_layout.setContentsMargins(15, 10, 15, 10)
        stats_layout.setSpacing(5)

        stats_title = QLabel("📈 Statistics")
        stats_title.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        stats_layout.addWidget(stats_title)

        # Total records
        total_label = QLabel("Total Records")
        total_label.setFont(QFont("Segoe UI", 8))
        total_label.setStyleSheet("color: #757575;")
        stats_layout.addWidget(total_label)

        total_value = QLabel(str(len(self.production_data)))
        total_value.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        total_value.setStyleSheet("color: #2196F3;")
        stats_layout.addWidget(total_value)

        stats_layout.addSpacing(5)

        # Total materials
        mat_label = QLabel("Materials Used")
        mat_label.setFont(QFont("Segoe UI", 8))
        mat_label.setStyleSheet("color: #757575;")
        stats_layout.addWidget(mat_label)

        mat_value = QLabel(str(len(self.formulation_data)))
        mat_value.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        mat_value.setStyleSheet("color: #4CAF50;")
        stats_layout.addWidget(mat_value)

        stats_layout.addStretch()
        layout.addWidget(stats_card)

        # Quick Actions
        actions_card = QFrame()
        actions_card.setObjectName("card")
        actions_layout = QVBoxLayout(actions_card)
        actions_layout.setContentsMargins(15, 10, 15, 10)
        actions_layout.setSpacing(8)

        actions_title = QLabel("⚡ Quick Actions")
        actions_title.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        actions_layout.addWidget(actions_title)

        new_btn = ModernButton("➕ New Entry", primary=True)
        actions_layout.addWidget(new_btn)

        export_btn = ModernButton("📤 Export Data")
        actions_layout.addWidget(export_btn)

        refresh_btn = ModernButton("🔄 Refresh")
        refresh_btn.clicked.connect(self.refresh_data)
        actions_layout.addWidget(refresh_btn)

        layout.addWidget(actions_card)

        return panel

    def create_materials_card(self):
        """Create materials section."""
        card = QFrame()
        card.setObjectName("card")
        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setSpacing(10)

        # Header
        title = QLabel("🧪 Material Composition")
        title.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        layout.addWidget(title)

        # Table
        self.material_table = QTableWidget()
        self.material_table.setRowCount(len(self.formulation_data))
        self.material_table.setColumnCount(6)
        self.material_table.setHorizontalHeaderLabels([
            "Material", "Large Scale (KG)", "Small Scale (G)",
            "Total Weight (KG)", "Total Loss (KG)", "Total Consumption (KG)"
        ])

        self.material_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.material_table.verticalHeader().setVisible(False)
        self.material_table.setMaximumHeight(200)
        self.material_table.setFont(QFont("Segoe UI", 9))
        self.material_table.horizontalHeader().setFont(QFont("Segoe UI", 8, QFont.Weight.Bold))

        # Populate material table
        for row, row_data in enumerate(self.formulation_data):
            for col, item_data in enumerate(row_data):
                item = QTableWidgetItem(str(item_data))
                item.setFont(QFont("Segoe UI", 9))
                self.material_table.setItem(row, col, item)

        layout.addWidget(self.material_table)

        return card

    def create_bottom_controls(self):
        """Create bottom control panel."""
        panel = QFrame()
        panel.setObjectName("card")
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 12, 20, 12)
        layout.setSpacing(8)

        # Filters Row
        filters_layout = QHBoxLayout()
        filters_layout.setSpacing(15)

        self.all_data_chk = QCheckBox("All Data")
        filters_layout.addWidget(self.all_data_chk)

        self.date_old_chk = QCheckBox("Date Old")
        filters_layout.addWidget(self.date_old_chk)

        self.date_new_chk = QCheckBox("Date New")
        filters_layout.addWidget(self.date_new_chk)

        self.cust_name_chk = QCheckBox("Customer A-Z")
        filters_layout.addWidget(self.cust_name_chk)

        self.prodcode_chk = QCheckBox("Product Code A-Z")
        filters_layout.addWidget(self.prodcode_chk)

        filters_layout.addStretch()

        layout.addLayout(filters_layout)

        # Date Range and Actions
        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(10)

        date_from_label = QLabel("From:")
        date_from_label.setFont(QFont("Segoe UI", 9))
        actions_layout.addWidget(date_from_label)

        self.date_from_edit = QDateEdit()
        self.date_from_edit.setCalendarPopup(True)
        self.date_from_edit.setDate(QDate.currentDate())
        self.date_from_edit.setFixedWidth(120)
        actions_layout.addWidget(self.date_from_edit)

        date_to_label = QLabel("To:")
        date_to_label.setFont(QFont("Segoe UI", 9))
        actions_layout.addWidget(date_to_label)

        self.date_to_edit = QDateEdit()
        self.date_to_edit.setCalendarPopup(True)
        self.date_to_edit.setDate(QDate.currentDate())
        self.date_to_edit.setFixedWidth(120)
        actions_layout.addWidget(self.date_to_edit)

        actions_layout.addStretch()

        # Admin Access
        admin_label = QLabel("🔐 Admin:")
        admin_label.setFont(QFont("Segoe UI", 9))
        actions_layout.addWidget(admin_label)

        self.admin_pwd_edit = QLineEdit()
        self.admin_pwd_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.admin_pwd_edit.setPlaceholderText("Password")
        self.admin_pwd_edit.setFixedWidth(100)
        actions_layout.addWidget(self.admin_pwd_edit)

        # Export Buttons
        export_btn = ModernButton("📤 Export", primary=True)
        actions_layout.addWidget(export_btn)

        export_old_btn = ModernButton("📂 Export Old")
        actions_layout.addWidget(export_old_btn)

        view_btn = ModernButton("👁 View")
        view_btn.clicked.connect(self.view_data)
        actions_layout.addWidget(view_btn)

        close_btn = ModernButton("✖ Close")
        close_btn.clicked.connect(self.close)
        actions_layout.addWidget(close_btn)

        layout.addLayout(actions_layout)

        return panel

    def refresh_data(self):
        """Refresh tables."""
        QMessageBox.information(self, "Refresh", "✅ Data refreshed successfully!")

    def view_data(self):
        """Handle VIEW button."""
        QMessageBox.information(self, "View", "👁 Viewing selected production record...")

    def create_menu_bar(self):
        menu_bar = self.menuBar()
        menu_bar.setFont(QFont("Segoe UI", 9))

        file_menu = menu_bar.addMenu("📁 File")
        view_menu = menu_bar.addMenu("👁 View")
        reports_menu = menu_bar.addMenu("📊 Reports")
        utilities_menu = menu_bar.addMenu("🔧 Utilities")
        archive_menu = menu_bar.addMenu("📦 Archive")
        system_menu = menu_bar.addMenu("⚙ System")

        # File menu actions
        file_menu.addAction("New Production Entry")
        file_menu.addAction("Open...")
        file_menu.addSeparator()
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)

        # View menu actions
        view_menu.addAction("Production Records")
        view_menu.addAction("Auto-Generate")
        view_menu.addSeparator()
        view_menu.addAction("Dashboard")

        reports_menu.addAction("Export Reports")
        reports_menu.addAction("Generate Summary")

        utilities_menu.addAction("System Utilities")
        utilities_menu.addAction("Data Management")

        archive_menu.addAction("View Archives")
        archive_menu.addAction("Restore Data")

        system_menu.addAction("User Settings")
        system_menu.addAction("Preferences")

    def create_status_bar(self):
        status = self.statusBar()
        status.setFont(QFont("Segoe UI", 9))
        status.showMessage("✅ Ready | MBPI System 2025")

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F5F7FA;
            }

            #headerFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #1976D2, stop:0.5 #2196F3, stop:1 #42A5F5);
                border: none;
            }

            #card {
                background-color: white;
                border-radius: 12px;
                border: 1px solid #E0E0E0;
            }

            #sidePanel {
                background-color: transparent;
            }

            #statsCard {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #E3F2FD, stop:1 #BBDEFB);
                border-radius: 12px;
                border: none;
            }

            QLineEdit {
                background-color: #F5F5F5;
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 9pt;
                font-family: 'Segoe UI';
            }

            QLineEdit:focus {
                border: 2px solid #2196F3;
                background-color: white;
            }

            QDateEdit {
                background-color: #F5F5F5;
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                padding: 6px 10px;
                font-size: 9pt;
                font-family: 'Segoe UI';
            }

            QDateEdit:focus {
                border: 2px solid #2196F3;
                background-color: white;
            }

            QDateEdit::drop-down {
                border: none;
                padding-right: 5px;
            }

            QCheckBox {
                font-size: 9pt;
                font-family: 'Segoe UI';
                spacing: 8px;
                color: #424242;
            }

            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 4px;
                border: 2px solid #BDBDBD;
                background-color: white;
            }

            QCheckBox::indicator:hover {
                border-color: #2196F3;
            }

            QCheckBox::indicator:checked {
                background-color: #2196F3;
                border-color: #2196F3;
                image: none;
            }

            QTableWidget {
                background-color: white;
                gridline-color: #F0F0F0;
                border: none;
                border-radius: 8px;
            }

            QTableWidget::item {
                padding: 8px;
                border: none;
            }

            QTableWidget::item:selected {
                background-color: #E3F2FD;
                color: #1976D2;
            }

            QTableWidget::item:alternate {
                background-color: #FAFAFA;
            }

            QHeaderView::section {
                background-color: #F5F5F5;
                color: #616161;
                padding: 8px;
                border: none;
                border-bottom: 2px solid #E0E0E0;
                font-weight: bold;
            }

            QMenuBar {
                background-color: white;
                border-bottom: 1px solid #E0E0E0;
                padding: 4px;
                font-family: 'Segoe UI';
            }

            QMenuBar::item {
                padding: 6px 12px;
                background-color: transparent;
                border-radius: 4px;
            }

            QMenuBar::item:selected {
                background-color: #E3F2FD;
                color: #1976D2;
            }

            QMenu {
                background-color: white;
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                padding: 5px;
            }

            QMenu::item {
                padding: 8px 25px;
                border-radius: 4px;
            }

            QMenu::item:selected {
                background-color: #E3F2FD;
                color: #1976D2;
            }

            QStatusBar {
                background-color: white;
                border-top: 1px solid #E0E0E0;
                color: #757575;
            }

            QScrollBar:vertical {
                background-color: #F5F5F5;
                width: 12px;
                border-radius: 6px;
            }

            QScrollBar::handle:vertical {
                background-color: #BDBDBD;
                border-radius: 6px;
                min-height: 20px;
            }

            QScrollBar::handle:vertical:hover {
                background-color: #9E9E9E;
            }

            QTabWidget::pane {
                border: 1px solid #E0E0E0;
                background-color: #F5F7FA;
            }

            QTabBar::tab {
                background-color: #F5F5F5;
                padding: 8px 16px;
                border: 1px solid #E0E0E0;
                border-bottom: none;
                font-family: 'Segoe UI';
                font-size: 9pt;
            }

            QTabBar::tab:selected {
                background-color: white;
                border-top: 2px solid #2196F3;
            }

            QTabBar::tab:hover {
                background-color: #E3F2FD;
            }

            QComboBox {
                background-color: #F5F5F5;
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                padding: 6px 10px;
                font-size: 9pt;
                font-family: 'Segoe UI';
                min-height: 24px;
            }

            QComboBox:focus {
                border: 2px solid #2196F3;
                background-color: white;
            }

            QComboBox::drop-down {
                border: none;
                width: 20px;
            }

            QTextEdit {
                background-color: #FAFAFA;
                border: 1px solid #E0E0E0;
                border-radius: 4px;
                padding: 4px;
                font-size: 9pt;
                font-family: 'Segoe UI';
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set application-wide font
    app.setFont(QFont("Segoe UI", 9))

    window = MainApplicationWindow(username="Admin")
    window.show()
    sys.exit(app.exec())