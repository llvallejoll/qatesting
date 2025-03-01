import json
import os
import sys
import unittest
from unittest.mock import patch, MagicMock

# Adjust the path as needed to import from the project
sys.path.append('.')

# Import functions to test (adjust imports based on actual project structure)
try:
    from main import get_product_info, get_product_stock, get_all_products
except ImportError:
    print("Error: Could not import functions from main.py. Please check the file structure.")
    sys.exit(1)

class TestPurchaseAssistant(unittest.TestCase):
    """Test cases for the Purchase Assistant functions."""
    
    def setUp(self):
        """Set up test environment."""
        # Check if catalog.json exists
        if not os.path.exists('catalog.json'):
            print("Warning: catalog.json not found. Tests will likely fail.")
            self.catalog_exists = False
        else:
            self.catalog_exists = True
            try:
                with open('catalog.json', 'r') as file:
                    self.catalog = json.load(file)
                # Get a sample product name for testing
                if len(self.catalog) > 0:
                    self.sample_product = self.catalog[0].get('Name', '')
                else:
                    self.sample_product = ''
            except (json.JSONDecodeError, FileNotFoundError):
                self.catalog_exists = False
                self.catalog = []
                self.sample_product = ''
    
    def test_catalog_structure(self):
        """Test that the catalog has the correct structure."""
        if not self.catalog_exists:
            self.skipTest("catalog.json not found")
        
        self.assertIsInstance(self.catalog, list, "Catalog should be a list")
        self.assertGreater(len(self.catalog), 0, "Catalog should not be empty")
        
        required_fields = ["Name", "Description", "Price", "Stock_availabiility"]
        for product in self.catalog:
            for field in required_fields:
                self.assertIn(field, product, f"Product should have '{field}' field")
    
    def test_get_all_products(self):
        """Test the get_all_products function."""
        if not self.catalog_exists:
            self.skipTest("catalog.json not found")
        
        result = get_all_products()
        
        # Check that the result contains expected text
        self.assertIn("The available products are:", result, 
                      "get_all_products should return a formatted string with 'The available products are:'")
        
        # Check that all product names are in the result
        for product in self.catalog:
            self.assertIn(product.get('Name', ''), result, 
                          f"Product {product.get('Name', '')} should be in the result")
    
    def test_get_product_info_existing(self):
        """Test get_product_info with an existing product."""
        if not self.sample_product:
            self.skipTest("No sample product available for testing")
        
        result = get_product_info(self.sample_product)
        
        # Check that the result contains expected text
        self.assertIn(f"The product is {self.sample_product}", result, 
                      "get_product_info should return a formatted string with product name")
        self.assertIn("description:", result, 
                      "get_product_info should include description")
        self.assertIn("price:", result, 
                      "get_product_info should include price")
    
    def test_get_product_info_non_existent(self):
        """Test get_product_info with a non-existent product."""
        non_existent_product = "ThisProductDoesNotExist12345"
        
        result = get_product_info(non_existent_product)
        
        self.assertEqual(result, "Product not found.", 
                         "get_product_info should return 'Product not found.' for non-existent products")
    
    def test_get_product_stock_existing(self):
        """Test get_product_stock with an existing product."""
        if not self.sample_product:
            self.skipTest("No sample product available for testing")
        
        result = get_product_stock(self.sample_product)
        
        # Check that the result contains expected text
        self.assertIn(f"The product {self.sample_product} is in stock", result, 
                      "get_product_stock should return a formatted string with product name")
        self.assertIn("availability:", result, 
                      "get_product_stock should include availability")
    
    def test_get_product_stock_non_existent(self):
        """Test get_product_stock with a non-existent product."""
        non_existent_product = "ThisProductDoesNotExist12345"
        
        result = get_product_stock(non_existent_product)
        
        self.assertEqual(result, "Product not found.", 
                         "get_product_stock should return 'Product not found.' for non-existent products")

    def test_empty_input(self):
        """Test with empty input."""
        # This will depend on how the main script handles empty input
        # For now, we'll just test that the functions don't crash with empty input
        try:
            get_product_info("")
            get_product_stock("")
            # No assertions, just checking that no exceptions are raised
        except Exception as e:
            self.fail(f"Empty input raised an exception: {e}")

    def test_special_characters(self):
        """Test with special characters."""
        special_chars = "!@#$%^&*()"
        try:
            get_product_info(special_chars)
            get_product_stock(special_chars)
            # No assertions, just checking that no exceptions are raised
        except Exception as e:
            self.fail(f"Special characters input raised an exception: {e}")


if __name__ == '__main__':
    unittest.main()