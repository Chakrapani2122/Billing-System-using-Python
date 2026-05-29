# Billing System using Python

A comprehensive retail billing management system built with Python and Tkinter that enables businesses to manage sales, generate professional bills, and maintain billing records. This application features a user-friendly GUI interface for efficient point-of-sale operations.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Product Catalog](#product-catalog)
- [Pricing and Taxes](#pricing-and-taxes)
- [Bill Management](#bill-management)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Billing System is a desktop application designed for retail stores to streamline their sales and billing operations. It provides an intuitive interface for cashiers to enter customer details, select products from three categories (Medical Supplies, Grocery Items, and Cold Drinks), calculate totals with automatic tax computation, and generate and store bills in a file-based system.

**Key Purpose**: Simplify retail transactions by automating bill generation, maintaining transaction records, and calculating taxes automatically.

## Features

### Core Functionality

- **Customer Details Management**: Store customer name and phone number for each transaction
- **Product Selection**: Choose from 18 different products across 3 categories
- **Automatic Price Calculation**: Real-time calculation of totals for each product category
- **Tax Calculation**: Automatic tax computation based on category-specific rates
- **Bill Generation**: Create professional, formatted bills with complete transaction details
- **Bill Storage**: Save bills to text files with unique bill numbers
- **Bill Search and Retrieval**: Retrieve previously saved bills using bill numbers
- **Clear Functionality**: Reset all fields for new transactions
- **Exit Application**: Safely close the application with confirmation dialog

### UI/UX Features

- **Clean, Color-Coded Interface**: Easy-to-navigate layout with distinct sections for each product category
- **Real-Time Updates**: Immediate calculation and display of prices and taxes
- **Scrollable Bill Area**: View complete bills even when they extend beyond the visible area
- **Input Validation**: Error messages for missing required fields or empty orders
- **Confirmation Dialogs**: Safe operations with user confirmation for critical actions

## Project Structure

```
Billing-System-using-Python/
├── README.md              # Project documentation (this file)
├── bill.py               # Main application file with GUI implementation
├── bills/                # Directory for storing generated bills
│   ├── 2152.txt         # Sample bill record (Bill #2152)
│   └── 7363.txt         # Sample bill record (Bill #7363)
└── Screenshot.png        # GUI screenshot of the application
```

### Files Description

- **bill.py**: Main Python script containing the `Bill_App` class that implements the entire billing system GUI using Tkinter. Includes all functions for price calculation, bill generation, storage, and retrieval.
- **bills/**: Directory where all generated bills are automatically saved as text files named by their bill number.

## Installation

### Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python)
- Operating System: Windows, macOS, or Linux

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Chakrapani2122/Billing-System-using-Python.git
   cd Billing-System-using-Python
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   ```
   Ensure you have Python 3.6 or higher installed.

3. **Verify Tkinter Installation**
   
   - **Windows**: Tkinter is included with Python
   - **macOS**: `python3 -m tkinter` (included with Python)
   - **Linux**: Install via package manager:
     ```bash
     sudo apt-get install python3-tk  # Ubuntu/Debian
     sudo yum install python3-tkinter  # Fedora/CentOS
     ```

4. **Prepare Bills Directory**
   
   The `bills/` directory should already exist. If not, create it:
   ```bash
   mkdir bills
   ```

5. **Run the Application**
   ```bash
   python bill.py
   ```
   Or:
   ```bash
   python3 bill.py
   ```

## Usage

### Starting the Application

Run the following command in your terminal:
```bash
python bill.py
```

The application window will open with the title "Billing Software" and display the main GUI interface.

### Step-by-Step Usage Guide

#### 1. Enter Customer Details

At the top of the application, fill in the customer information:
- **Name**: Customer's full name
- **Phone Number**: Customer's contact number
- **Bill Number**: Auto-generated unique bill number (cannot be modified)

#### 2. Add Products to Bill

The application has three product categories displayed as separate sections:

**Medical Purpose Section**
- Select quantity for required medical items
- Enter numbers in the entry fields

**Grocery Items Section**
- Add desired grocery quantities

**Cold Drinks Section**
- Add desired cold drinks quantities

#### 3. Calculate Totals

Click the **"Total"** button to:
- Calculate item prices based on quantities and unit prices
- Compute category-specific taxes
- Display totals in the respective fields

#### 4. Generate Bill

Click the **"Generate Bill"** button to:
- Validate that customer details are entered
- Validate that at least one product has been purchased
- Display formatted bill in the Bill Area
- Show all purchased items with quantities and prices
- Display all applicable taxes
- Show the grand total

#### 5. Save Bill

A dialog box will appear asking "Do you want to save the bill?"
- Click **"Yes"** to save the bill to the `bills/` directory
- Click **"No"** to discard the bill
- If saved, a confirmation message displays the bill number

#### 6. Retrieve Previous Bills

To view a previously saved bill:
1. Enter the bill number in the "Bill Number" field at the top
2. Click the **"Search"** button
3. The bill will be displayed in the Bill Area if it exists
4. If the bill number is invalid, an error message appears

#### 7. Clear Data

Click the **"Clear"** button to:
- Reset all product quantities to 0
- Clear all price and tax fields
- Clear customer details (except bill number)
- Generate a new bill number for the next transaction
- A confirmation dialog will appear before clearing

#### 8. Exit Application

Click the **"Exit"** button to:
- Close the application safely
- A confirmation dialog appears before exiting

### Example Transaction

1. Enter customer name: "John Doe"
2. Enter phone: "9876543210"
3. Add quantities:
   - Sanitizer: 2 units
   - Rice: 1 unit
   - Coke: 2 units
4. Click "Total" to calculate
5. Click "Generate Bill"
6. Review the bill in the Bill Area
7. Click "Yes" to save the bill
8. Bill is saved as `bills/XXXX.txt`

## Product Catalog

### Medical Purpose Products

| Product | Unit Price (Rs.) |
|---------|-----------------|
| Sanitizer | 30 |
| Mask | 10 |
| Hand Gloves | 20 |
| Dettol | 50 |
| Newsprin | 10 |
| Thermal Gun | 80 |

### Grocery Items

| Product | Unit Price (Rs.) |
|---------|-----------------|
| Rice | 500 |
| Food Oil | 110 |
| Wheat | 60 |
| Daal | 30 |
| Flour | 35 |
| Maggi | 20 |

### Cold Drinks

| Product | Unit Price (Rs.) |
|---------|-----------------|
| Sprite | 110 |
| Limka | 55 |
| Mazza | 45 |
| Coke | 60 |
| Fanta | 35 |
| Mountain Duo | 20 |

## Pricing and Taxes

### Tax Rates by Category

1. **Medical Products**: 5% tax on total medical items cost
   - Formula: Total Medical Price × 0.05
   
2. **Grocery Items**: 5% tax on total grocery items cost
   - Formula: Total Grocery Price × 0.05
   
3. **Cold Drinks**: 10% tax on total cold drinks cost
   - Formula: Total Cold Drinks Price × 0.10

### Bill Calculation Example

**Transaction:**
- 1 Sanitizer (Rs. 30)
- 2 Masks (Rs. 20)
- 1 Rice (Rs. 500)
- 2 Cokes (Rs. 120)

**Calculation:**
- Medical Total: 30 + 20 = Rs. 50
- Medical Tax (5%): 50 × 0.05 = Rs. 2.50
- Grocery Total: 500 = Rs. 500
- Grocery Tax (5%): 500 × 0.05 = Rs. 25.00
- Cold Drinks Total: 120 = Rs. 120
- Cold Drinks Tax (10%): 120 × 0.10 = Rs. 12.00
- **Grand Total**: 50 + 2.50 + 500 + 25.00 + 120 + 12.00 = **Rs. 709.50**

## Bill Management

### Bill Storage

- Bills are stored as text files in the `bills/` directory
- File naming convention: `{bill_number}.txt`
- Example: `bills/2152.txt`, `bills/7363.txt`

### Bill Format

Each bill contains:
```
Welcome Infinite Retail / Webcode Retail
Bill Number: XXXX
Customer Name: [Name]
Phone Number: [Number]
======================================
Products        QTY        Price
[Item Name]     [Qty]      [Price]
...
[Category] Tax                Rs. [Amount]
Total Bill:                  Rs. [Total]
======================================
```

### Bill File Structure

The `bills/` directory should be in the same location as `bill.py`. All bill files are plain text (.txt) format and can be opened with any text editor.

### Sample Bill

See `bills/2152.txt` and `bills/7363.txt` for example bill formats and transactions.

## GUI Layout

The application window is 1350x700 pixels with the following sections:

1. **Title Bar** (Top): "Billing Software" title
2. **Customer Details Frame** (Below title): Name, Phone Number, Bill Number fields with Search button
3. **Three Category Frames** (Middle):
   - Medical Purpose (left)
   - Grocery Items (center-left)
   - Cold Drinks (center)
4. **Bill Area Frame** (Right): Scrollable text area displaying generated bills
5. **Bill Information Frame** (Bottom): Shows prices and taxes for each category
6. **Button Frame** (Bottom Right): Total, Generate Bill, Clear, and Exit buttons

## Troubleshooting

### Common Issues and Solutions

#### Issue: "ModuleNotFoundError: No module named 'tkinter'"
**Solution**: Install tkinter
- **Linux**: `sudo apt-get install python3-tk`
- **macOS**: Tkinter is included. Reinstall Python if needed.
- **Windows**: Ensure Python is installed with tkinter selected

#### Issue: Application window doesn't open
**Solution**: 
- Verify Python is correctly installed
- Check that you're using Python 3.6+
- Ensure Tkinter is installed and working

#### Issue: Bill not saving to file
**Possible Causes**:
- `bills/` directory doesn't exist
- No write permissions in the project directory
- Bill number already exists (try a different number)

**Solution**:
- Create the `bills/` directory if it doesn't exist: `mkdir bills`
- Check folder permissions: `chmod 755 bills` (Linux/macOS)
- Run the application from a directory where you have write permissions

#### Issue: Cannot find previous bills
**Possible Causes**:
- Incorrect bill number entered
- Bill file was deleted
- Bills are in a different directory

**Solution**:
- Double-check the bill number
- Check the `bills/` directory for available bill files
- Ensure bills directory is in the same location as `bill.py`

#### Issue: Prices or taxes not calculating
**Solution**:
- Enter valid numeric values in quantity fields
- Click the "Total" button after entering quantities
- Check that quantities are positive integers

#### Issue: Error message "Customer Details Are Must"
**Solution**:
- Enter both customer name and phone number
- Don't leave these fields empty

#### Issue: Error message "No Product Purchased"
**Solution**:
- Add quantities for at least one product
- Click "Total" button to calculate prices
- At least one quantity field must have a value greater than 0

### Performance Tips

- Clear data after each transaction using the "Clear" button
- Periodically archive old bills from the `bills/` directory
- Keep the application window visible during transactions

### Contact for Support

For issues not covered above, please check the GitHub repository or create an issue with:
- Python version
- Operating system
- Error message (if any)
- Steps to reproduce the issue

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add YourFeature'`)
5. Push to the branch (`git push origin feature/YourFeature`)
6. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guidelines for Python code
- Add comments for complex functions
- Test your changes thoroughly
- Update documentation for new features

### Areas for Improvement

- Database integration (SQLite/MySQL) for better data management
- Additional reporting features (daily sales, inventory tracking)
- Network capability for multi-user systems
- Enhanced UI with modern frameworks
- Export bills to PDF format
- Inventory management system
- Customer loyalty program integration
- Discount application functionality

## License

This project is open source and available under the MIT License. See the LICENSE file for details.

## Project Information

- **Author**: Chakrapani2122
- **Repository**: https://github.com/Chakrapani2122/Billing-System-using-Python
- **Language**: Python 3
- **Framework**: Tkinter (GUI)
- **File-based Storage**: Text files

## Changelog

### Version 1.0 (Current)
- Basic billing functionality
- Customer details management
- Three product categories
- Automatic tax calculation
- Bill generation and storage
- Bill search functionality
- Clear and exit functions

## Acknowledgments

- Built with Python's Tkinter library for GUI
- Inspired by retail point-of-sale systems

---

**Last Updated**: May 29, 2026
**Project Status**: Active