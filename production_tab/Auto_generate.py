# auto_generate_tab.py
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox,
                             QTableWidget, QTableWidgetItem, QHeaderView, QFrame, QFormLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class AutoGenerateTab(QWidget):
    def __init__(self, username, current_date):
        super().__init__()
        self.username = username
        self.current_date = current_date
        self.material_data = [
            ["", "", "", "", "", ""],  # Material name, large scale, small scale, total weight, total loss, total consumption
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""]
        ]
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(8)  # Reduced spacing for compactness

        # Title
        title = QLabel("PRODUCTION - AUTO GENERATE RECORDS - WITH CONSUMPTION BY WH")
        title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Main Form Layout - Split into left (form fields) and right (materials table)
        main_form_layout = QHBoxLayout()
        main_form_layout.setSpacing(15)  # Moderate spacing between sides

        # Left Side: Form Fields using QFormLayout for clean alignment
        left_widget = QWidget()
        left_layout = QFormLayout(left_widget)
        left_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)  # Labels right-aligned
        left_layout.setFormAlignment(Qt.AlignmentFlag.AlignLeft)
        left_layout.setHorizontalSpacing(10)
        left_layout.setVerticalSpacing(4)  # Tight vertical spacing

        # Define uniform field width (slightly wider)
        field_width = 140

        # Product Code
        self.product_code_edit = QLineEdit("BA803E")
        self.product_code_edit.setFixedSize(field_width, 25)
        left_layout.addRow("PRODUCT CODE", self.product_code_edit)

        # Form Type
        self.form_type_combo = QComboBox()
        self.form_type_combo.addItems(["", "Type 1", "Type 2"])  # Sample
        self.form_type_combo.setFixedSize(field_width, 25)
        left_layout.addRow("FORM TYPE", self.form_type_combo)

        # Production ID
        self.production_id_edit = QLineEdit("0098744")
        self.production_id_edit.setFixedSize(field_width, 25)
        left_layout.addRow("PRODUCTION ID", self.production_id_edit)

        # Product Color
        self.product_color_edit = QLineEdit("BLUE")
        self.product_color_edit.setFixedSize(field_width, 25)
        left_layout.addRow("PRODUCT COLOR", self.product_color_edit)

        # Dosage
        self.dosage_edit = QLineEdit("100.00000")
        self.dosage_edit.setFixedSize(field_width, 25)
        left_layout.addRow("DOSAGE", self.dosage_edit)

        # LD(%)
        self.ld_edit = QLineEdit("0.4000")
        self.ld_edit.setFixedSize(field_width, 25)
        left_layout.addRow("LD(%)", self.ld_edit)

        # Customer
        self.customer_edit = QLineEdit("UNITED INTERNATIONAL")
        self.customer_edit.setFixedSize(field_width, 25)
        left_layout.addRow("CUSTOMER", self.customer_edit)

        # Lot No.
        self.lot_no_edit = QLineEdit("8204X")
        self.lot_no_edit.setFixedSize(field_width, 25)
        left_layout.addRow("LOT NO.", self.lot_no_edit)

        # Tentative Date
        self.tentative_date_edit = QLineEdit(" / /")
        self.tentative_date_edit.setFixedSize(field_width, 25)
        left_layout.addRow("TENTATIVE DATE", self.tentative_date_edit)

        # Confirm Inventory Date
        self.confirm_date_edit = QLineEdit(" / /")
        self.confirm_date_edit.setFixedSize(field_width, 25)
        left_layout.addRow("CONFIRM INVENTORY DATE", self.confirm_date_edit)

        # Order Form No.
        self.order_form_edit = QLineEdit()
        self.order_form_edit.setFixedSize(field_width, 25)
        left_layout.addRow("ORDER FORM NO.", self.order_form_edit)

        # Colormatch Date
        self.colormatch_date_edit = QLineEdit("02/14/25")
        self.colormatch_date_edit.setFixedSize(field_width, 25)
        left_layout.addRow("COLORMATCH DATE", self.colormatch_date_edit)

        # Formulation ID
        self.formulation_id_edit = QLineEdit("16025")
        self.formulation_id_edit.setFixedSize(field_width, 25)
        left_layout.addRow("FORMULATION ID", self.formulation_id_edit)

        # Mixing Time
        self.mixing_time_edit = QLineEdit()
        self.mixing_time_edit.setFixedSize(field_width, 25)
        left_layout.addRow("MIXING TIME", self.mixing_time_edit)

        # QTY. REQ.
        self.qty_req_edit = QLineEdit("0.000000")
        self.qty_req_edit.setFixedSize(field_width, 25)
        left_layout.addRow("QTY. REQ.", self.qty_req_edit)

        # QTY. PER BATCH
        self.qty_per_batch_edit = QLineEdit("0.000000")
        self.qty_per_batch_edit.setFixedSize(field_width, 25)
        left_layout.addRow("QTY. PER BATCH", self.qty_per_batch_edit)

        # Prepared By
        self.prepared_by_edit = QLineEdit()
        self.prepared_by_edit.setFixedSize(field_width, 25)
        left_layout.addRow("PREPARED BY", self.prepared_by_edit)

        # Notes
        self.notes_edit = QLineEdit()
        self.notes_edit.setFixedSize(field_width, 25)
        left_layout.addRow("NOTES", self.notes_edit)

        main_form_layout.addWidget(left_widget, 3)

        # Right Side: Materials Table
        right_layout = QVBoxLayout()
        right_layout.setSpacing(5)

        table_title = QLabel("MATERIAL NAME")
        table_title.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        right_layout.addWidget(table_title)

        self.materials_table = QTableWidget(5, 6)  # 5 rows, 6 columns
        self.materials_table.setHorizontalHeaderLabels(["MATERIAL NAME", "LARGE SCALE (KG)", "SMALL SCALE (G)", "TOTAL WEIGHT (KG)", "TOTAL LOSS (KG)", "TOTAL CONSUMPTION (KG)"])
        self.materials_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.materials_table.verticalHeader().setVisible(False)
        self.materials_table.setFont(QFont("Arial", 9))
        self.materials_table.horizontalHeader().setFont(QFont("Arial", 9, QFont.Weight.Bold))  # Bold headers
        self.populate_materials_table()
        right_layout.addWidget(self.materials_table)

        main_form_layout.addLayout(right_layout, 7)
        layout.addLayout(main_form_layout)

        # Bottom Section: No. of Items, Encoded By, Confirmation
        bottom_layout = QHBoxLayout()
        bottom_layout.setSpacing(10)
        bottom_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # No. of Items
        items_label = QLabel("NO. OF ITEMS: 0")
        items_label.setFont(QFont("Arial", 9))
        bottom_layout.addWidget(items_label)

        # Cancel Link
        cancel_btn = QPushButton("Click here to cancel this production")
        cancel_btn.setStyleSheet("QPushButton { text-decoration: underline; color: blue; background: transparent; border: none; }")
        cancel_btn.setFont(QFont("Arial", 9))
        bottom_layout.addWidget(cancel_btn)

        bottom_layout.addStretch()

        # Encoded By and Confirmation
        encoded_frame = QFrame()
        encoded_frame.setFrameStyle(QFrame.Shape.Box)
        encoded_frame.setLineWidth(1)
        encoded_layout = QHBoxLayout(encoded_frame)
        encoded_layout.setContentsMargins(5, 2, 5, 2)
        encoded_layout.setSpacing(5)

        encoded_by_label = QLabel("ENCODED BY")
        encoded_by_label.setFont(QFont("Arial", 9))
        encoded_layout.addWidget(encoded_by_label)

        production_confirm_label = QLabel("PRODUCTION CONFIRMATION ENCODED ON")
        production_confirm_label.setFont(QFont("Arial", 9))
        encoded_layout.addWidget(production_confirm_label)

        self.confirm_encoded_edit = QLineEdit("00000000")
        self.confirm_encoded_edit.setFixedSize(100, 25)
        encoded_layout.addWidget(self.confirm_encoded_edit)

        bottom_layout.addWidget(encoded_frame)

        layout.addLayout(bottom_layout)

        # Very Bottom: Date, Production Encoded On, Buttons
        very_bottom_layout = QHBoxLayout()
        very_bottom_layout.setSpacing(10)
        very_bottom_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        encoded_date_label = QLabel("10/07/2025 08:34 AM")  # Static from screenshot, or dynamic
        encoded_date_label.setFont(QFont("Arial", 8))
        very_bottom_layout.addWidget(encoded_date_label)

        very_bottom_layout.addStretch()

        # Buttons - Compact and aligned right
        btn_frame = QFrame()
        btn_layout = QHBoxLayout(btn_frame)
        btn_layout.setContentsMargins(0, 0, 0, 0)
        btn_layout.setSpacing(5)

        generate_tumbler_btn = QPushButton("GENERATE TUMBLER")
        generate_tumbler_btn.setFixedSize(120, 25)
        generate_tumbler_btn.setFont(QFont("Arial", 8, QFont.Weight.Bold))
        btn_layout.addWidget(generate_tumbler_btn)

        generate_advance_btn = QPushButton("GENERATE ADVANCE")
        generate_advance_btn.setFixedSize(120, 25)
        generate_advance_btn.setFont(QFont("Arial", 8, QFont.Weight.Bold))
        btn_layout.addWidget(generate_advance_btn)

        print_btn = QPushButton("PRINT")
        print_btn.setFixedSize(80, 25)
        print_btn.setFont(QFont("Arial", 8, QFont.Weight.Bold))
        btn_layout.addWidget(print_btn)

        new_btn = QPushButton("NEW")
        new_btn.setFixedSize(80, 25)
        new_btn.setFont(QFont("Arial", 8, QFont.Weight.Bold))
        btn_layout.addWidget(new_btn)

        close_btn = QPushButton("CLOSE")
        close_btn.setFixedSize(80, 25)
        close_btn.setFont(QFont("Arial", 8, QFont.Weight.Bold))
        close_btn.clicked.connect(self.close)  # Or parent close
        btn_layout.addWidget(close_btn)

        very_bottom_layout.addWidget(btn_frame)

        layout.addLayout(very_bottom_layout)

        # Footer
        footer = QLabel("MBPI SYSTEM 2025 NUM")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer.setFont(QFont("Arial", 8))
        layout.addWidget(footer)

    def populate_materials_table(self):
        """Populate the materials table with 6 columns."""
        self.materials_table.setRowCount(len(self.material_data))
        for row, row_data in enumerate(self.material_data):
            for col, item_data in enumerate(row_data):
                item = QTableWidgetItem(str(item_data))
                item.setFont(QFont("Arial", 9))
                self.materials_table.setItem(row, col, item)