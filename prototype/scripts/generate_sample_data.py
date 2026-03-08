#!/usr/bin/env python3
"""
Sample Data Generation Script
Generates realistic sample product data for ShelfIQ prototype
"""

import csv
import random
import os
from datetime import datetime
from typing import List, Dict


# Product categories
CATEGORIES = ["Electronics", "Home & Kitchen", "Sports", "Books", "Toys"]

# Sample product names by category with realistic details
PRODUCT_NAMES = {
    "Electronics": [
        "boAt Rockerz 450 Wireless Bluetooth Headphones",
        "Noise ColorFit Pro 3 Smart Watch",
        "JBL Go 2 Portable Bluetooth Speaker",
        "Portronics Konnect L 1.2M USB-C Cable",
        "Portronics My Buddy Plus Adjustable Laptop Stand",
        "Logitech M235 Wireless Mouse",
        "Zebronics Zeb-K25 Wired USB Keyboard",
        "Logitech C270 HD Webcam 720p",
        "Spigen Rugged Armor Back Cover for iPhone",
        "Mi 20000mAh Power Bank 3i Fast Charging"
    ],
    "Home & Kitchen": [
        "Prestige PCMH 3.0 Electric Coffee Maker 4 Cups",
        "Philips HL7756/00 Mixer Grinder 750W 3 Jars",
        "Inalsa Air Fryer Fry-Light 1400W 4.2L",
        "Eureka Forbes Vacuum Cleaner 1400W",
        "Stainless Steel 2-Tier Dish Drainer Rack",
        "HealthSense Chef-Mate KS 33 Digital Kitchen Scale 5kg",
        "Wooden Bamboo Cutting Board Large 15x10 inch",
        "Borosil Mixing Bowl Set of 3 with Lids",
        "Milton Vitro Airtight Storage Container Set 6pc",
        "Vim Dishwash Liquid Gel Lemon 2L Refill Pack"
    ],
    "Sports": [
        "Strauss Yoga Mat 6mm Anti-Skid with Bag",
        "Boldfit Resistance Bands Set of 5 with Handles",
        "Kore PVC-DM Combo 16 Dumbbells Kit 20Kg",
        "Cello Flip Style Plastic Water Bottle 1L BPA Free",
        "Campus BATTLE Running Shoes for Men",
        "Puma Evercat Duffel Gym Bag 45L",
        "Strauss Adjustable Skipping Rope with Counter",
        "Cockatoo Foam Roller 45cm for Muscle Recovery",
        "Strauss Anti Burst Gym Ball 65cm with Pump",
        "Noise ColorFit Pro 2 Fitness Tracker Watch"
    ],
    "Books": [
        "Python Crash Course 2nd Edition by Eric Matthes",
        "Zero to One by Peter Thiel - Business Strategy",
        "Atomic Habits by James Clear - Self Help",
        "Sanjeev Kapoor's Khazana of Indian Recipes",
        "The Girl in Room 105 by Chetan Bhagat - Mystery",
        "Project Hail Mary by Andy Weir - Sci-Fi Novel",
        "Steve Jobs Biography by Walter Isaacson",
        "Sapiens: A Brief History of Humankind by Yuval Noah Harari",
        "Lonely Planet India Travel Guide 2024 Edition",
        "The Art Book: Big Ideas Simply Explained - DK"
    ],
    "Toys": [
        "Lego Classic Creative Building Blocks 484 Pieces",
        "Funskool Puzzle 1000 Pieces Jigsaw for Adults",
        "Hot Wheels Marvel Avengers Action Figure Set",
        "Hasbro Monopoly Classic Board Game Family Edition",
        "Dimpy Stuff Teddy Bear Soft Toy 60cm Brown",
        "SYMA X5C RC Drone Quadcopter with HD Camera",
        "Faber-Castell Art Set 60 Pieces Drawing Kit",
        "Fisher-Price Learning Toy for Kids 2-5 Years",
        "Little Tikes Outdoor Slide and Swing Combo",
        "Barbie Dreamhouse Dollhouse 3 Floors with Furniture"
    ]
}

# Competitor names
COMPETITOR_NAMES = ["CompA", "CompB", "CompC", "CompD", "CompE", "CompF", "CompG"]


def generate_product(product_id: int, category: str, name: str) -> Dict:
    """Generate a single product record with realistic Indian prices (INR)"""

    # Base price varies by category - realistic Indian market prices in INR
    price_ranges = {
        "Electronics": (299, 2999),      # ₹299 - ₹2,999 (affordable electronics)
        "Home & Kitchen": (199, 3499),   # ₹199 - ₹3,499 (kitchen appliances)
        "Sports": (149, 1499),           # ₹149 - ₹1,499 (fitness equipment)
        "Books": (199, 699),             # ₹199 - ₹699 (books)
        "Toys": (249, 2499)              # ₹249 - ₹2,499 (toys and games)
    }

    base_price = random.uniform(*price_ranges[category])

    # Generate competitor prices (3-7 competitors)
    num_competitors = random.randint(3, 7)
    competitor_prices = [
        round(base_price * random.uniform(0.85, 1.15), 2)
        for _ in range(num_competitors)
    ]

    # Select random competitor names
    competitors = random.sample(COMPETITOR_NAMES, num_competitors)

    # Generate product data
    product = {
        "product_id": f"PROD-{product_id:03d}",
        "name": name,
        "category": category,
        "current_price": round(base_price, 2),
        "cost": round(base_price * random.uniform(0.55, 0.65), 2),  # 35-45% margin
        "competitor_prices": ",".join(map(str, competitor_prices)),
        "competitor_names": ",".join(competitors),
        "sales_rank": random.randint(100, 10000),
        "rating": round(random.uniform(3.5, 5.0), 1),
        "review_count": random.randint(10, 1000),
        "last_updated": datetime.utcnow().isoformat() + "Z"
    }

    return product


def generate_sample_data(num_products: int = 50) -> List[Dict]:
    """Generate sample product dataset"""

    products = []
    product_id = 1

    # Distribute products across categories
    products_per_category = num_products // len(CATEGORIES)

    for category in CATEGORIES:
        available_names = PRODUCT_NAMES[category].copy()

        for i in range(products_per_category):
            if available_names:
                name = available_names.pop(0)
            else:
                name = f"{category} Product {i+1}"

            product = generate_product(product_id, category, name)
            products.append(product)
            product_id += 1

    # Add remaining products to random categories
    remaining = num_products - len(products)
    for _ in range(remaining):
        category = random.choice(CATEGORIES)
        name = f"{category} Product {product_id}"
        product = generate_product(product_id, category, name)
        products.append(product)
        product_id += 1

    return products


def save_to_csv(products: List[Dict], output_dir: str = "../sample-data"):
    """Save products to CSV file"""

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, "products.csv")

    # Write to CSV
    with open(output_file, 'w', newline='') as f:
        if products:
            writer = csv.DictWriter(f, fieldnames=products[0].keys())
            writer.writeheader()
            writer.writerows(products)

    print(f"✅ Generated {len(products)} products")
    print(f"📁 Saved to: {output_file}")

    # Print summary statistics
    print("\n📊 Summary by Category:")
    category_counts = {}
    for product in products:
        cat = product['category']
        category_counts[cat] = category_counts.get(cat, 0) + 1

    for category, count in sorted(category_counts.items()):
        print(f"  {category}: {count} products")

    # Print price range
    prices = [p['current_price'] for p in products]
    print(f"\n💰 Price Range: ₹{min(prices):.2f} - ₹{max(prices):.2f}")
    print(f"📈 Average Price: ₹{sum(prices)/len(prices):.2f}")


def main():
    """Main function"""
    print("🚀 ShelfIQ Sample Data Generator")
    print("=" * 50)

    # Generate 50 products
    products = generate_sample_data(num_products=50)

    # Save to CSV
    save_to_csv(products)

    print("\n✨ Sample data generation complete!")
    print("\nNext steps:")
    print("1. Upload to S3: aws s3 cp ../sample-data/products.csv s3://YOUR-BUCKET/sample-data/")
    print("2. Trigger data ingestion Lambda")
    print("3. Verify data in DynamoDB")


if __name__ == "__main__":
    main()
