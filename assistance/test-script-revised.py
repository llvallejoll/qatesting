import json
import os
import unittest
from unittest.mock import patch, MagicMock

class TestPurchaseAssistant(unittest.TestCase):
    """Test cases for the Purchase Assistant functions."""
    
    def setUp(self):
        """Set up test environment."""
        # Check if catalog.json exists
        if not os.path.exists('catalog.json'):
            print("Warning: catalog.json not found. Creating the catalog list for testing.")
            # Create a sample catalog for testing
            self.catalog = [                
                {
                    "PRODUCT_ID": 1,
                    "Name": "Apple MacBook Pro",
                    "Description": "16-inch, 16GB RAM, 1TB SSD",
                    "Price": 2399,
                    "Stock_availabiility": 15
                },
                {
                    "PRODUCT_ID": 2,
                    "Name": "Samsung Galaxy S21",
                    "Description": "6.2-inch, 8GB RAM, 128GB Storage",
                    "Price": 799,
                    "Stock_availabiility": 30
                },
                {
                    "PRODUCT_ID": 3,
                    "Name": "Sony WH-1000XM4",
                    "Description": "Wireless Noise-Canceling Over-Ear Headphones",
                    "Price": 349,
                    "Stock_availabiility": 50
                },
                {
                    "PRODUCT_ID": 4,
                    "Name": "Dell XPS 13",
                    "Description": "13.3-inch, 16GB RAM, 512GB SSD",
                    "Price": 1299,
                    "Stock_availabiility": 20
                },
                {
                    "PRODUCT_ID": 5,
                    "Name": "Apple iPhone 13",
                    "Description": "6.1-inch, 128GB Storage",
                    "Price": 999,
                    "Stock_availabiility": 25
                },
                {
                    "PRODUCT_ID": 6,
                    "Name": "Bose QuietComfort 35 II",
                    "Description": "Wireless Bluetooth Headphones, Noise-Cancelling",
                    "Price": 299,
                    "Stock_availabiility": 40
                },
                {
                    "PRODUCT_ID": 7,
                    "Name": "Microsoft Surface Pro 7",
                    "Description": "12.3-inch, 8GB RAM, 256GB SSD",
                    "Price": 899,
                    "Stock_availabiility": 10
                },
                {
                    "PRODUCT_ID": 8,
                    "Name": "Google Pixel 6",
                    "Description": "6.4-inch, 8GB RAM, 128GB Storage",
                    "Price": 699,
                    "Stock_availabiility": 35
                },
                {
                    "PRODUCT_ID": 9,
                    "Name": "Amazon Echo Dot (4th Gen)",
                    "Description": "Smart speaker with Alexa",
                    "Price": 49,
                    "Stock_availabiility": 100
                },
                {
                    "PRODUCT_ID": 10,
                    "Name": "Fitbit Charge 5",
                    "Description": "Advanced Fitness & Health Tracker",
                    "Price": 179,
                    "Stock_availabiility": 60
                },
                {
                    "PRODUCT_ID": 11,
                    "Name": "HP Spectre x360",
                    "Description": "13.3-inch, 16GB RAM, 1TB SSD",
                    "Price": 1599,
                    "Stock_availabiility": 12
                },
                {
                    "PRODUCT_ID": 12,
                    "Name": "OnePlus 9 Pro",
                    "Description": "6.7-inch, 12GB RAM, 256GB Storage",
                    "Price": 969,
                    "Stock_availabiility": 22
                },
                {
                    "PRODUCT_ID": 13,
                    "Name": "JBL Flip 5",
                    "Description": "Portable Waterproof Bluetooth Speaker",
                    "Price": 119,
                    "Stock_availabiility": 45
                },
                {
                    "PRODUCT_ID": 14,
                    "Name": "Canon EOS R5",
                    "Description": "Full-Frame Mirrorless Camera, 45MP",
                    "Price": 3899,
                    "Stock_availabiility": 8
                },
                {
                    "PRODUCT_ID": 15,
                    "Name": "Nintendo Switch",
                    "Description": "Hybrid Game Console",
                    "Price": 299,
                    "Stock_availabiility": 50
                },
                {
                    "PRODUCT_ID": 16,
                    "Name": "Sony PlayStation 5",
                    "Description": "Next-Gen Gaming Console",
                    "Price": 499,
                    "Stock_availabiility": 20
                },
                {
                    "PRODUCT_ID": 17,
                    "Name": "Samsung QLED TV",
                    "Description": "65-inch, 4K UHD Smart TV",
                    "Price": 1499,
                    "Stock_availabiility": 15
                },
                {
                    "PRODUCT_ID": 18,
                    "Name": "Dyson V11 Vacuum",
                    "Description": "Cordless Vacuum Cleaner",
                    "Price": 599,
                    "Stock_availabiility": 25
                },
                {
                    "PRODUCT_ID": 19,
                    "Name": "GoPro HERO9",
                    "Description": "Action Camera, 5K Video",
                    "Price": 399,
                    "Stock_availabiility": 30
                },
                {
                    "PRODUCT_ID": 20,
                    "Name": "Apple AirPods Pro",
                    "Description": "Wireless Earbuds with Active Noise Cancellation",
                    "Price": 249,
                    "Stock_availabiility": 50
                }
            ]
            
            with open('catalog.json', 'w') as file:
                json.dump(self.catalog, file)
        
        # Load the catalog
        with open('catalog.json', 'r') as file:
            self.catalog = json.load(file)           
                    
        # Create an instance of EventHandler-like object for testing
        self.handler = TestEventHandler(self.catalog)
    
    def test_catalog_structure(self):
        """Test that the catalog has the correct structure."""
        print("Test 0: Catalog loading test running")        
        # We test if catalog is a list data structure
        self.assertIsInstance(self.catalog, list, "Catalog should be a list")
        # We test if catalog is not empty
        self.assertGreater(len(self.catalog), 0, "Catalog should not be empty")
        
        # Check if all required fields are in each catalog product
        required_fields = ["Name", "Description", "Price", "Stock_availabiility"]
        for product in self.catalog:            
            for i,field in enumerate(required_fields):
                self.assertIn(field, product, f"Product should have '{field}' field")
            
            
                
    
    def test_get_all_products(self):
        """Test the get_all_products functionality."""
        tool_call = MagicMock()
        tool_call.id = "test_tool_call_id"
        tool_call.function.name = "get_all_products"
        tool_call.function.arguments = "{}"
        
        print("Test 1: Get All Products")        
        data = MagicMock()
        data.required_action.submit_tool_outputs.tool_calls = [tool_call]
        
        tool_outputs = self.handler.handle_requires_action_test(data)
        
        # Check that the output contains the expected format
        output = tool_outputs[0]["output"]
        self.assertIn("The available products are:", output)
        
        
        print("Output Test 1: Get All Products \n",output)
        # Check that all product names are in the output
        for product in self.catalog:
            self.assertIn(product.get('Name', ''), output)
            
    
    def test_get_product_info_existing(self):
        """Test get_product_info with an existing product."""
        if not self.sample_product:
            self.skipTest("No sample product available for testing")
        
        tool_call = MagicMock()
        tool_call.id = "test_tool_call_id"
        tool_call.function.name = "get_product_info"
        tool_call.function.arguments = json.dumps({"Name": self.sample_product})
        
        data = MagicMock()
        data.required_action.submit_tool_outputs.tool_calls = [tool_call]
        
        tool_outputs = self.handler.handle_requires_action_test(data)
        
        # Check that the output contains the expected format
        output = tool_outputs[0]["output"]
        self.assertIn(f"The product is {self.sample_product}", output)
        self.assertIn("description:", output)
        self.assertIn("price:", output)
    
    def test_get_product_info_non_existent(self):
        """Test get_product_info with a non-existent product."""
        non_existent_product = "ThisProductDoesNotExist12345"
        
        tool_call = MagicMock()
        tool_call.id = "test_tool_call_id"
        tool_call.function.name = "get_product_info"
        tool_call.function.arguments = json.dumps({"Name": non_existent_product})
        
        data = MagicMock()
        data.required_action.submit_tool_outputs.tool_calls = [tool_call]
        
        tool_outputs = self.handler.handle_requires_action_test(data)
        
        # Check that the output contains the expected format
        output = tool_outputs[0]["output"]
        self.assertEqual("Product not found.", output)
    
    def test_get_product_stock_existing(self):
        """Test get_product_stock with an existing product."""
        if not self.sample_product:
            self.skipTest("No sample product available for testing")
        
        tool_call = MagicMock()
        tool_call.id = "test_tool_call_id"
        tool_call.function.name = "get_product_stock"
        tool_call.function.arguments = json.dumps({"Name": self.sample_product})
        
        data = MagicMock()
        data.required_action.submit_tool_outputs.tool_calls = [tool_call]
        
        tool_outputs = self.handler.handle_requires_action_test(data)
        
        # Check that the output contains the expected format
        output = tool_outputs[0]["output"]
        self.assertIn(f"The product {self.sample_product} is in stock", output)
        self.assertIn("availability:", output)
    
    def test_get_product_stock_non_existent(self):
        """Test get_product_stock with a non-existent product."""
        non_existent_product = "ThisProductDoesNotExist12345"
        
        tool_call = MagicMock()
        tool_call.id = "test_tool_call_id"
        tool_call.function.name = "get_product_stock"
        tool_call.function.arguments = json.dumps({"Name": non_existent_product})
        
        data = MagicMock()
        data.required_action.submit_tool_outputs.tool_calls = [tool_call]
        
        tool_outputs = self.handler.handle_requires_action_test(data)
        
        # Check that the output contains the expected format
        output = tool_outputs[0]["output"]
        self.assertEqual("Product not found.", output)

    def test_empty_input(self):
        """Test with empty input."""
        tool_call = MagicMock()
        tool_call.id = "test_tool_call_id"
        tool_call.function.name = "get_product_info"
        tool_call.function.arguments = json.dumps({"Name": ""})
        
        data = MagicMock()
        data.required_action.submit_tool_outputs.tool_calls = [tool_call]
        
        try:
            tool_outputs = self.handler.handle_requires_action_test(data)
            # No assertions, just checking that no exceptions are raised
        except Exception as e:
            self.fail(f"Empty input raised an exception: {e}")

    def test_special_characters(self):
        """Test with special characters."""
        special_chars = "!@#$%^&*()"
        
        tool_call = MagicMock()
        tool_call.id = "test_tool_call_id"
        tool_call.function.name = "get_product_info"
        tool_call.function.arguments = json.dumps({"Name": special_chars})
        
        data = MagicMock()
        data.required_action.submit_tool_outputs.tool_calls = [tool_call]
        
        try:
            tool_outputs = self.handler.handle_requires_action_test(data)
            # No assertions, just checking that no exceptions are raised
        except Exception as e:
            self.fail(f"Special characters input raised an exception: {e}")

    def tearDown(self):
        """Clean up after tests."""
        pass


class TestEventHandler:
    """A test version of the EventHandler class with just the needed functionality."""
    
    def __init__(self, catalog):
        self.catalog = catalog
        self.current_run = MagicMock()
        self.current_run.thread_id = "test_thread_id"
        self.current_run.id = "test_run_id"
    
    def handle_requires_action_test(self, data):
        """Test version of handle_requires_action that returns tool_outputs instead of submitting them."""
        tool_outputs = []
        
        for tool in data.required_action.submit_tool_outputs.tool_calls:           
            arguments = json.loads(tool.function.arguments)  # Convert to dictionary
            if tool.function.name == "get_product_info":
                product_name = arguments.get("Name", "").lower()
                product_info = next((item for item in self.catalog if item["Name"].lower() == product_name), None)
                if product_info:
                    tool_outputs.append({"tool_call_id": tool.id, "output": f"The product is {product_info['Name']} with description: {product_info['Description']} and price: {product_info['Price']}."})
                else:
                    tool_outputs.append({"tool_call_id": tool.id, "output": "Product not found."})
            elif tool.function.name == "get_product_stock":
                product_name = arguments.get("Name", "").lower()
                product_stock = next((item for item in self.catalog if item["Name"].lower() == product_name), None)
                if product_stock:
                    tool_outputs.append({"tool_call_id": tool.id, "output": f"The product {product_stock['Name']} is in stock with availability: {product_stock['Stock_availabiility']}."})
                else:
                    tool_outputs.append({"tool_call_id": tool.id, "output": "Product not found."})
            elif tool.function.name == "get_all_products":
                products = [product["Name"] for product in self.catalog]
                tool_outputs.append({"tool_call_id": tool.id, "output": f"The available products are: {', '.join(products)}."})
        
        return tool_outputs


if __name__ == '__main__':
    unittest.main(buffer=False)
