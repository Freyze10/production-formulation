from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox,
                             QTableWidget, QTableWidgetItem, QHeaderView, QFrame, QFormLayout, QTextEdit)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class AutoGenerateTab(QWidget):
    def __init__(self, username, current_date):
        super().__init__()
        self.username = username
        self.current_date = current_date
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)

        # Title
        title = QLabel("PRODUCTION - AUTO GENERATE RECORDS - WITH CONSUMPTION BY WH")
        title.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("background-color: lightblue; padding: 5px;")
        layout.addWidget(title)

        # User and Tab Section
        user_tab_layout = QHBoxLayout()
        user_label = QLabel(f"👤 USER : {self.username}")
        user_label.setFont(QFont("Arial", 9))
        user_tab_layout.addWidget(user_label)

        prod_records_btn = QPushButton("PRODUCTION RECORDS")
        prod_records_btn.setFont(QFont("Arial", 9))
        user_tab_layout.addWidget(prod_records_btn)

        auto_gen_btn = QPushButton("AUTO-GENERATE PRODUCTION ENTRY")
        auto_gen_btn.setFont(QFont("Arial", 9))
        user_tab_layout.addWidget(auto_gen_btn)

        user_tab_layout.addStretch()
        layout.addLayout(user_tab_layout)

        # Main Content Layout
        main_content = QHBoxLayout()
        main_content.setSpacing(10)

        # Left Side: Icon and Label
        left_side = QVBoxLayout()
        left_side.setAlignment(Qt.AlignmentFlag.AlignTop)

        icon_label = QLabel("🏭\n📦")  # Placeholder for production icon
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setFont(QFont("Arial", 24))
        left_side.addWidget(icon_label)

        prod_auto_label = QLabel("PRODUCTION AUTO")
        prod_auto_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        prod_auto_label.setFont(QFont("Arial", 8, QFont.Weight.Bold))
        left_side.addWidget(prod_auto_label)

        left_side.addStretch()
        main_content.addLayout(left_side, 1)

        # Middle: Form Fields
        middle_layout = QVBoxLayout()
        middle_layout.setSpacing(2)

        form_widget = QWidget()
        form_layout = QFormLayout(form_widget)
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form_layout.setHorizontalSpacing(5)
        form_layout.setVerticalSpacing(2)
        form_layout.setContentsMargins(0, 0, 0, 0)

        # Field styling
        field_style = "background-color: yellow; border: 1px solid black;"
        white_field_style = "background-color: white; border: 1px solid black;"
        field_width = 200
        field_height = 22

        # Product Code (with asterisk for required field)
        product_code_layout = QHBoxLayout()
        self.product_code_combo = QComboBox()
        self.product_code_combo.setEditable(True)
        self.product_code_combo.setCurrentText("BA0830E")
        self.product_code_combo.setFixedSize(field_width, field_height)
        self.product_code_combo.setStyleSheet(field_style)
        product_code_layout.addWidget(self.product_code_combo)
        product_code_layout.addStretch()
        form_layout.addRow("PRODUCT CODE      *", product_code_layout)

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
        dosage_layout.addWidget(ld_label)

        self.ld_edit = QLineEdit("0.40000")
        self.ld_edit.setFixedSize(80, field_height)
        self.ld_edit.setStyleSheet(white_field_style)
        dosage_layout.addWidget(self.ld_edit)
        dosage_layout.addStretch()
        form_layout.addRow("DOSAGE      *", dosage_layout)

        # Customer
        self.customer_combo = QComboBox()
        self.customer_combo.setEditable(True)
        self.customer_combo.setCurrentText("Una Internationale")
        self.customer_combo.setFixedSize(field_width, field_height)
        self.customer_combo.setStyleSheet(field_style)
        form_layout.addRow("CUSTOMER      *", self.customer_combo)

        # Lot No.
        self.lot_no_combo = QComboBox()
        self.lot_no_combo.setEditable(True)
        self.lot_no_combo.setFixedSize(field_width, field_height)
        self.lot_no_combo.setStyleSheet(field_style)
        form_layout.addRow("LOT NO.      *", self.lot_no_combo)

        # Tentative Production Date
        self.tentative_date_edit = QLineEdit("  /  /")
        self.tentative_date_edit.setFixedSize(field_width, field_height)
        self.tentative_date_edit.setStyleSheet(field_style)
        form_layout.addRow("TENTATIVE\nPRODUCTION DATE      *", self.tentative_date_edit)

        # Confirmation Date for Inventory Only
        self.confirm_date_edit = QLineEdit("  /  /")
        self.confirm_date_edit.setFixedSize(field_width, field_height)
        self.confirm_date_edit.setStyleSheet(white_field_style)
        form_layout.addRow("CONFIRMATION DATE\nFOR INVENTORY ONLY      *", self.confirm_date_edit)

        # Order Form No.
        self.order_form_combo = QComboBox()
        self.order_form_combo.setEditable(True)
        self.order_form_combo.setFixedSize(field_width, field_height)
        self.order_form_combo.setStyleSheet(field_style)
        form_layout.addRow("ORDER FORM NO.      *", self.order_form_combo)

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
        form_layout.addRow("QTY. REQ.      *", self.qty_req_edit)

        # QTY. PER BATCH
        self.qty_per_batch_edit = QLineEdit("0.0000000")
        self.qty_per_batch_edit.setFixedSize(field_width, field_height)
        self.qty_per_batch_edit.setStyleSheet(field_style)
        form_layout.addRow("QTY. PER BATCH      *", self.qty_per_batch_edit)

        # Prepared By
        self.prepared_by_combo = QComboBox()
        self.prepared_by_combo.setEditable(True)
        self.prepared_by_combo.setFixedSize(field_width, field_height)
        self.prepared_by_combo.setStyleSheet(field_style)
        form_layout.addRow("PREPARED BY      *", self.prepared_by_combo)

        # Notes
        self.notes_edit = QTextEdit()
        self.notes_edit.setFixedSize(field_width, 50)
        self.notes_edit.setStyleSheet(white_field_style)
        form_layout.addRow("NOTES", self.notes_edit)

        middle_layout.addWidget(form_widget)
        main_content.addLayout(middle_layout, 3)

        # Right Side: Form Type, Production ID, and Materials Table
        right_layout = QVBoxLayout()
        right_layout.setSpacing(5)

        # Form Type Row
        form_type_layout = QHBoxLayout()
        form_type_label = QLabel("FORM TYPE")
        form_type_label.setFont(QFont("Arial", 9))
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
        prod_id_label.setFont(QFont("Arial", 9))
        prod_id_layout.addWidget(prod_id_label)

        self.production_id_label = QLabel("0098744")
        self.production_id_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.production_id_label.setStyleSheet("color: blue;")
        prod_id_layout.addWidget(self.production_id_label)
        prod_id_layout.addStretch()
        right_layout.addLayout(prod_id_layout)

        # Materials Table Header
        table_header_widget = QWidget()
        table_header_widget.setStyleSheet("background-color: darkblue;")
        table_header_layout = QHBoxLayout(table_header_widget)
        table_header_layout.setContentsMargins(0, 0, 0, 0)
        table_header_layout.setSpacing(0)

        headers = ["TOTAL WEIGHT (KG.)", "TOTAL LOSS (KG.)", "TOTAL CONSUMPTION (KG.)"]
        for header in headers:
            header_label = QLabel(header)
            header_label.setFont(QFont("Arial", 8, QFont.Weight.Bold))
            header_label.setStyleSheet("color: white; background-color: darkblue; padding: 3px;")
            header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            table_header_layout.addWidget(header_label)

        right_layout.addWidget(table_header_widget)

        # Large empty area for materials (simplified as empty space)
        materials_area = QWidget()
        materials_area.setMinimumHeight(300)
        materials_area.setStyleSheet("background-color: white; border: 1px solid gray;")
        right_layout.addWidget(materials_area)

        # Bottom stats section
        stats_layout = QVBoxLayout()
        stats_layout.setSpacing(2)

        items_label = QLabel("NO. OF ITEMS :  0")
        items_label.setFont(QFont("Arial", 9, QFont.Weight.Bold))
        stats_layout.addWidget(items_label)

        weight_label = QLabel("TOTAL WEIGHT  : 0.000000")
        weight_label.setFont(QFont("Arial", 9, QFont.Weight.Bold))
        stats_layout.addWidget(weight_label)

        fg_label = QLabel("FG in 1D (FOR WH) ONLY")
        fg_label.setFont(QFont("Arial", 8))
        stats_layout.addWidget(fg_label)

        right_layout.addLayout(stats_layout)

        main_content.addLayout(right_layout, 4)

        layout.addLayout(main_content)

        # Cancel link
        cancel_btn = QPushButton("CLICK HERE TO CANCEL THIS PRODUCTION")
        cancel_btn.setStyleSheet(
            "QPushButton { text-decoration: underline; color: blue; background: transparent; border: none; }")
        cancel_btn.setFont(QFont("Arial", 8))
        layout.addWidget(cancel_btn, alignment=Qt.AlignmentFlag.AlignRight)

        # Encoded By Section
        encoded_layout = QHBoxLayout()

        encoded_by_label = QLabel("ENCODED BY")
        encoded_by_label.setFont(QFont("Arial", 9))
        encoded_layout.addWidget(encoded_by_label)

        prod_confirm_label = QLabel("PRODUCTION CONFIRMATION ENCODED ON")
        prod_confirm_label.setFont(QFont("Arial", 9))
        encoded_layout.addWidget(prod_confirm_label)

        self.confirm_encoded_edit = QLineEdit("0000000")
        self.confirm_encoded_edit.setFixedSize(120, field_height)
        self.confirm_encoded_edit.setStyleSheet(field_style)
        encoded_layout.addWidget(self.confirm_encoded_edit)

        encoded_layout.addStretch()
        layout.addLayout(encoded_layout)

        # Bottom Section with Date and Buttons
        bottom_layout = QHBoxLayout()

        date_prod_layout = QVBoxLayout()
        date_label = QLabel("10/07/2025 09:49:35 AM")
        date_label.setFont(QFont("Arial", 8))
        date_prod_layout.addWidget(date_label)

        prod_encoded_layout = QHBoxLayout()
        prod_encoded_label = QLabel("PRODUCTION ENCODED ON")
        prod_encoded_label.setFont(QFont("Arial", 8))
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
        btn_layout.setSpacing(5)

        buttons = [
            ("GENERATE", 90),
            ("TUMBLER", 90),
            ("GENERATE ADVANCE", 140),
            ("PRINT", 70),
            ("NEW", 70),
            ("CLOSE", 70)
        ]

        for btn_text, btn_width in buttons:
            btn = QPushButton(btn_text)
            btn.setFixedSize(btn_width, 25)
            btn.setFont(QFont("Arial", 8, QFont.Weight.Bold))
            btn.setStyleSheet("background-color: lightgray; border: 1px solid black;")
            if btn_text == "CLOSE":
                btn.clicked.connect(self.close)
            btn_layout.addWidget(btn)

        bottom_layout.addLayout(btn_layout)
        layout.addLayout(bottom_layout)

        # Footer
        footer_layout = QHBoxLayout()
        footer_left = QLabel("MBPI SYSTEM 2022")
        footer_left.setFont(QFont("Arial", 8))
        footer_layout.addWidget(footer_left)

        footer_layout.addStretch()

        footer_right = QLabel("NUM")
        footer_right.setFont(QFont("Arial", 8))
        footer_layout.addWidget(footer_right)

        layout.addLayout(footer_layout)