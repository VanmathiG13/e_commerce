import pysolr
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Index products into Solr'

    def handle(self, *args, **kwargs):
        solr = pysolr.Solr('http://localhost:8983/solr/newproducts', always_commit=True)

        products = [
             {
        "product_id": 1,
        "product_name": "Smart TV",
        "description": "A 55-inch Smart TV with 4K resolution.",
        "category": 1,
        "image_url": "https://via.placeholder.com/150/FF5733/FFFFFF?text=Smart+TV",
        "mrp": "500.00",
        "discounted_price": "450.00",
        "product_count": 50
    },
    {
        "product_id": 2,
        "product_name": "Bluetooth Speaker",
        "description": "Portable Bluetooth speaker with deep bass.",
        "category": 1,
        "image_url": "https://via.placeholder.com/150/33FF57/FFFFFF?text=Bluetooth+Speaker",
        "mrp": "80.00",
        "discounted_price": "70.00",
        "product_count": 200
    },
    {
        "product_id": 3,
        "product_name": "Wireless Headphones",
        "description": "Noise-cancelling over-ear wireless headphones.",
        "category": 1,
        "image_url": "https://via.placeholder.com/150/3357FF/FFFFFF?text=Wireless+Headphones",
        "mrp": "120.00",
        "discounted_price": "100.00",
        "product_count": 150
    },
    {
        "product_id": 4,
        "product_name": "Gaming Laptop",
        "description": "High-performance laptop for gaming and productivity.",
        "category": 2,
        "image_url": "https://via.placeholder.com/150/FF33A6/FFFFFF?text=Gaming+Laptop",
        "mrp": "1200.00",
        "discounted_price": "1150.00",
        "product_count": 25
    },
    {
        "product_id": 5,
        "product_name": "Ultrabook",
        "description": "Lightweight ultrabook for work and play.",
        "category": 2,
        "image_url": "https://via.placeholder.com/150/FFDA33/FFFFFF?text=Ultrabook",
        "mrp": "900.00",
        "discounted_price": "850.00",
        "product_count": 30
    },
    {
        "product_id": 6,
        "product_name": "Business Laptop",
        "description": "Reliable laptop for business tasks.",
        "category": 2,
        "image_url": "https://via.placeholder.com/150/33A6FF/FFFFFF?text=Business+Laptop",
        "mrp": "1000.00",
        "discounted_price": "950.00",
        "product_count": 20
    },
    {
        "product_id": 7,
        "product_name": "Smartphone A",
        "description": "Latest smartphone with advanced features.",
        "category": 3,
        "image_url": "https://via.placeholder.com/150/FF8C33/FFFFFF?text=Smartphone+A",
        "mrp": "700.00",
        "discounted_price": "650.00",
        "product_count": 50
    },
    {
        "product_id": 8,
        "product_name": "Smartphone B",
        "description": "Mid-range smartphone with excellent camera.",
        "category": 3,
        "image_url": "https://via.placeholder.com/150/33FF8C/FFFFFF?text=Smartphone+B",
        "mrp": "800.00",
        "discounted_price": "750.00",
        "product_count": 40
    },
    {
        "product_id": 9,
        "product_name": "Smartphone C",
        "description": "Budget-friendly smartphone with essential features.",
        "category": 3,
        "image_url": "https://via.placeholder.com/150/8C33FF/FFFFFF?text=Smartphone+C",
        "mrp": "600.00",
        "discounted_price": "550.00",
        "product_count": 60
    },
    {
        "product_id": 10,
        "product_name": "LED TV 42\"",
        "description": "42-inch LED TV with vibrant colors.",
        "category": 4,
        "image_url": "https://via.placeholder.com/150/FF33B8/FFFFFF?text=LED+TV+42%22",
        "mrp": "400.00",
        "discounted_price": "350.00",
        "product_count": 30
    },
    {
        "product_id": 11,
        "product_name": "Smart TV 55\"",
        "description": "55-inch Smart TV with voice control.",
        "category": 4,
        "image_url": "https://via.placeholder.com/150/FF33B8/FFFFFF?text=Smart+TV+55%22",
        "mrp": "600.00",
        "discounted_price": "550.00",
        "product_count": 25
    },
    {
        "product_id": 12,
        "product_name": "4K Ultra HD TV 65\"",
        "description": "65-inch Ultra HD TV with stunning clarity.",
        "category": 4,
        "image_url": "https://via.placeholder.com/150/FF33B8/FFFFFF?text=4K+Ultra+HD+TV+65%22",
        "mrp": "800.00",
        "discounted_price": "750.00",
        "product_count": 15
    },
    {
        "product_id": 13,
        "product_name": "Refrigerator 500L",
        "description": "500L refrigerator with energy-efficient technology.",
        "category": 5,
        "image_url": "https://via.placeholder.com/150/FF5733/FFFFFF?text=Refrigerator+500L",
        "mrp": "800.00",
        "discounted_price": "750.00",
        "product_count": 20
    },
    {
        "product_id": 14,
        "product_name": "Washing Machine 8kg",
        "description": "8kg washing machine with various wash programs.",
        "category": 5,
        "image_url": "https://via.placeholder.com/150/33FF57/FFFFFF?text=Washing+Machine+8kg",
        "mrp": "500.00",
        "discounted_price": "450.00",
        "product_count": 25
    },
    {
        "product_id": 15,
        "product_name": "Microwave Oven",
        "description": "Compact microwave oven with multiple settings.",
        "category": 5,
        "image_url": "https://via.placeholder.com/150/3357FF/FFFFFF?text=Microwave+Oven",
        "mrp": "150.00",
        "discounted_price": "140.00",
        "product_count": 30
    },
    {
        "product_id": 16,
        "product_name": "Sofa Set",
        "description": "Elegant sofa set for living room comfort.",
        "category": 6,
        "image_url": "https://via.placeholder.com/150/FF33A6/FFFFFF?text=Sofa+Set",
        "mrp": "1200.00",
        "discounted_price": "1150.00",
        "product_count": 15
    },
    {
        "product_id": 17,
        "product_name": "Dining Table",
        "description": "Stylish dining table for family gatherings.",
        "category": 6,
        "image_url": "https://via.placeholder.com/150/FFDA33/FFFFFF?text=Dining+Table",
        "mrp": "800.00",
        "discounted_price": "750.00",
        "product_count": 20
    },
    {
        "product_id": 18,
        "product_name": "Office Chair",
        "description": "Ergonomic office chair for long hours.",
        "category": 6,
        "image_url": "https://via.placeholder.com/150/33A6FF/FFFFFF?text=Office+Chair",
        "mrp": "150.00",
        "discounted_price": "140.00",
        "product_count": 50
    },
    {
        "product_id": 19,
        "product_name": "Men's T-Shirt",
        "description": "Comfortable cotton t-shirt for casual wear.",
        "category": 7,
        "image_url": "https://via.placeholder.com/150/FF8C33/FFFFFF?text=Men%27s+T-Shirt",
        "mrp": "25.00",
        "discounted_price": "20.00",
        "product_count": 100
    },
    {
        "product_id": 20,
        "product_name": "Women's Dress",
        "description": "Elegant dress suitable for all occasions.",
        "category": 7,
        "image_url": "https://via.placeholder.com/150/33FF8C/FFFFFF?text=Women%27s+Dress",
        "mrp": "40.00",
        "discounted_price": "35.00",
        "product_count": 80
    },
    {
        "product_id": 21,
        "product_name": "Men's Jeans",
        "description": "Stylish jeans for everyday wear.",
        "category": 7,
        "image_url": "https://via.placeholder.com/150/8C33FF/FFFFFF?text=Men%27s+Jeans",
        "mrp": "50.00",
        "discounted_price": "45.00",
        "product_count": 70
    },
    {
        "product_id": 22,
        "product_name": "Running Shoes",
        "description": "Lightweight running shoes for fitness enthusiasts.",
        "category": 8,
        "image_url": "https://via.placeholder.com/150/FF33B8/FFFFFF?text=Running+Shoes",
        "mrp": "80.00",
        "discounted_price": "70.00",
        "product_count": 100
    },
    {
        "product_id": 23,
        "product_name": "Sandals",
        "description": "Casual sandals for summer outings.",
        "category": 8,
        "image_url": "https://via.placeholder.com/150/FF5733/FFFFFF?text=Sandals",
        "mrp": "40.00",
        "discounted_price": "35.00",
        "product_count": 200
    },
    {
        "product_id": 24,
        "product_name": "Formal Shoes",
        "description": "Stylish formal shoes for business meetings.",
        "category": 8,
        "image_url": "https://via.placeholder.com/150/33FF57/FFFFFF?text=Formal+Shoes",
        "mrp": "100.00",
        "discounted_price": "90.00",
        "product_count": 150
    },
    {
        "product_id": 25,
        "product_name": "Fiction Novel",
        "description": "Engaging fiction novel for book lovers.",
        "category": 9,
        "image_url": "https://via.placeholder.com/150/3357FF/FFFFFF?text=Fiction+Novel",
        "mrp": "15.00",
        "discounted_price": "12.00",
        "product_count": 300
    },
    {
        "product_id": 26,
        "product_name": "Science Textbook",
        "description": "Comprehensive science textbook for students.",
        "category": 9,
        "image_url": "https://via.placeholder.com/150/FF33A6/FFFFFF?text=Science+Textbook",
        "mrp": "50.00",
        "discounted_price": "45.00",
        "product_count": 100
    },
    {
        "product_id": 27,
        "product_name": "Cookbook",
        "description": "Delicious recipes for home cooking.",
        "category": 9,
        "image_url": "https://via.placeholder.com/150/FFDA33/FFFFFF?text=Cookbook",
        "mrp": "25.00",
        "discounted_price": "20.00",
        "product_count": 150
    },
    {
        "product_id": 28,
        "product_name": "Building Blocks",
        "description": "Creative building blocks for kids.",
        "category": 10,
        "image_url": "https://via.placeholder.com/150/33A6FF/FFFFFF?text=Building+Blocks",
        "mrp": "30.00",
        "discounted_price": "25.00",
        "product_count": 200
    },
    {
        "product_id": 29,
        "product_name": "Action Figure",
        "description": "Collectible action figure for enthusiasts.",
        "category": 10,
        "image_url": "https://via.placeholder.com/150/FF8C33/FFFFFF?text=Action+Figure",
        "mrp": "15.00",
        "discounted_price": "12.00",
        "product_count": 150
    },
    {
        "product_id": 30,
        "product_name": "Doll Set",
        "description": "Adorable doll set for imaginative play.",
        "category": 10,
        "image_url": "https://via.placeholder.com/150/33FF8C/FFFFFF?text=Doll+Set",
        "mrp": "20.00",
        "discounted_price": "18.00",
        "product_count": 100
    },
    {
        "product_id": 31,
        "product_name": "Lipstick",
        "description": "Long-lasting lipstick in vibrant colors.",
        "category": 11,
        "image_url": "https://via.placeholder.com/150/8C33FF/FFFFFF?text=Lipstick",
        "mrp": "20.00",
        "discounted_price": "18.00",
        "product_count": 200
    },
    {
        "product_id": 32,
        "product_name": "Face Cream",
        "description": "Moisturizing face cream for all skin types.",
        "category": 11,
        "image_url": "https://via.placeholder.com/150/FF33B8/FFFFFF?text=Face+Cream",
        "mrp": "30.00",
        "discounted_price": "25.00",
        "product_count": 150
    },
    {
        "product_id": 33,
        "product_name": "Perfume",
        "description": "Fragrance that lasts all day.",
        "category": 11,
        "image_url": "https://via.placeholder.com/150/FF5733/FFFFFF?text=Perfume",
        "mrp": "50.00",
        "discounted_price": "45.00",
        "product_count": 100
    },
    {
        "product_id": 34,
        "product_name": "Tennis Racket",
        "description": "Lightweight tennis racket for competitive play.",
        "category": 12,
        "image_url": "https://via.placeholder.com/150/33FF57/FFFFFF?text=Tennis+Racket",
        "mrp": "70.00",
        "discounted_price": "60.00",
        "product_count": 50
    },
    {
        "product_id": 35,
        "product_name": "Soccer Ball",
        "description": "Durable soccer ball for outdoor fun.",
        "category": 12,
        "image_url": "https://via.placeholder.com/150/3357FF/FFFFFF?text=Soccer+Ball",
        "mrp": "25.00",
        "discounted_price": "20.00",
        "product_count": 100
    },
    {
        "product_id": 36,
        "product_name": "Basketball",
        "description": "Official size basketball for games.",
        "category": 12,
        "image_url": "https://via.placeholder.com/150/FF33A6/FFFFFF?text=Basketball",
        "mrp": "30.00",
        "discounted_price": "28.00",
        "product_count": 80
    },
    {
        "product_id": 37,
        "product_name": "Garden Shovel",
        "description": "Heavy-duty garden shovel for digging.",
        "category": 13,
        "image_url": "https://via.placeholder.com/150/FFDA33/FFFFFF?text=Garden+Shovel",
        "mrp": "15.00",
        "discounted_price": "12.00",
        "product_count": 150
    },
    {
        "product_id": 38,
        "product_name": "Pruning Shears",
        "description": "Sharp pruning shears for garden maintenance.",
        "category": 13,
        "image_url": "https://via.placeholder.com/150/33A6FF/FFFFFF?text=Pruning+Shears",
        "mrp": "20.00",
        "discounted_price": "18.00",
        "product_count": 120
    },
    {
        "product_id": 39,
        "product_name": "Watering Can",
        "description": "Classic watering can for plants.",
        "category": 13,
        "image_url": "https://via.placeholder.com/150/FF8C33/FFFFFF?text=Watering+Can",
        "mrp": "10.00",
        "discounted_price": "9.00",
        "product_count": 200
    },
    {
        "product_id": 40,
        "product_name": "Gold Necklace",
        "description": "Elegant gold necklace for special occasions.",
        "category": 14,
        "image_url": "https://via.placeholder.com/150/8C33FF/FFFFFF?text=Gold+Necklace",
        "mrp": "500.00",
        "discounted_price": "480.00",
        "product_count": 10
    },
    {
        "product_id": 41,
        "product_name": "Silver Bracelet",
        "description": "Stylish silver bracelet for everyday wear.",
        "category": 14,
        "image_url": "https://via.placeholder.com/150/FF33B8/FFFFFF?text=Silver+Bracelet",
        "mrp": "150.00",
        "discounted_price": "140.00",
        "product_count": 30
    },
    {
        "product_id": 42,
        "product_name": "Diamond Ring",
        "description": "Beautiful diamond ring for engagements.",
        "category": 14,
        "image_url": "https://via.placeholder.com/150/FF5733/FFFFFF?text=Diamond+Ring",
        "mrp": "1000.00",
        "discounted_price": "950.00",
        "product_count": 5
    },
    {
        "product_id": 43,
        "product_name": "Vitamins",
        "description": "Essential vitamins for daily health.",
        "category": 15,
        "image_url": "https://via.placeholder.com/150/33FF57/FFFFFF?text=Vitamins",
        "mrp": "25.00",
        "discounted_price": "20.00",
        "product_count": 100
    },
    {
        "product_id": 44,
        "product_name": "Protein Powder",
        "description": "High-quality protein powder for fitness.",
        "category": 15,
        "image_url": "https://via.placeholder.com/150/3357FF/FFFFFF?text=Protein+Powder",
        "mrp": "50.00",
        "discounted_price": "45.00",
        "product_count": 75
    },
    {
        "product_id": 45,
        "product_name": "First Aid Kit",
        "description": "Complete first aid kit for emergencies.",
        "category": 15,
        "image_url": "https://via.placeholder.com/150/FF33A6/FFFFFF?text=First+Aid+Kit",
        "mrp": "30.00",
        "discounted_price": "25.00",
        "product_count": 60
    },
    {
        "product_id": 46,
        "product_name": "Car Vacuum Cleaner",
        "description": "Portable car vacuum cleaner for quick clean-ups.",
        "category": 16,
        "image_url": "https://via.placeholder.com/150/FFDA33/FFFFFF?text=Car+Vacuum+Cleaner",
        "mrp": "60.00",
        "discounted_price": "50.00",
        "product_count": 40
    },
    {
        "product_id": 47,
        "product_name": "Car Cover",
        "description": "Durable car cover for outdoor protection.",
        "category": 16,
        "image_url": "https://via.placeholder.com/150/33A6FF/FFFFFF?text=Car+Cover",
        "mrp": "40.00",
        "discounted_price": "35.00",
        "product_count": 70
    },
    {
        "product_id": 48,
        "product_name": "Tire Inflator",
        "description": "Compact tire inflator for emergencies.",
        "category": 16,
        "image_url": "https://via.placeholder.com/150/FF8C33/FFFFFF?text=Tire+Inflator",
        "mrp": "25.00",
        "discounted_price": "20.00",
        "product_count": 100
    },
    {
        "product_id": 49,
        "product_name": "Dog Food",
        "description": "Nutritious dog food for your furry friend.",
        "category": 17,
        "image_url": "https://via.placeholder.com/150/8C33FF/FFFFFF?text=Dog+Food",
        "mrp": "30.00",
        "discounted_price": "28.00",
        "product_count": 150
    },
    {
        "product_id": 50,
        "product_name": "Cat Litter",
        "description": "High-absorbency cat litter for easy cleanup.",
        "category": 17,
        "image_url": "https://via.placeholder.com/150/FF33B8/FFFFFF?text=Cat+Litter",
        "mrp": "15.00",
        "discounted_price": "12.00",
        "product_count": 200
    },
    {
        "product_id": 51,
        "product_name": "Pet Bed",
        "description": "Comfortable bed for your pet to relax.",
        "category": 17,
        "image_url": "https://via.placeholder.com/150/FF5733/FFFFFF?text=Pet+Bed",
        "mrp": "50.00",
        "discounted_price": "45.00",
        "product_count": 75
    },
    {
        "product_id": 52,
        "product_name": "Notebook",
        "description": "Quality notebook for notes and sketches.",
        "category": 18,
        "image_url": "https://via.placeholder.com/150/33FF57/FFFFFF?text=Notebook",
        "mrp": "5.00",
        "discounted_price": "4.50",
        "product_count": 300
    },
    {
        "product_id": 53,
        "product_name": "Ballpoint Pen",
        "description": "Smooth-writing ballpoint pen for daily use.",
        "category": 18,
        "image_url": "https://via.placeholder.com/150/3357FF/FFFFFF?text=Ballpoint+Pen",
        "mrp": "2.00",
        "discounted_price": "1.80",
        "product_count": 500
    },
    {
        "product_id": 54,
        "product_name": "Highlighter",
        "description": "Bright highlighter for marking important text.",
        "category": 18,
        "image_url": "https://via.placeholder.com/150/FF33A6/FFFFFF?text=Highlighter",
        "mrp": "1.00",
        "discounted_price": "0.90",
        "product_count": 600
    },
    {
        "product_id": 55,
        "product_name": "Paint Set",
        "description": "Complete paint set for artists.",
        "category": 19,
        "image_url": "https://via.placeholder.com/150/FFDA33/FFFFFF?text=Paint+Set",
        "mrp": "20.00",
        "discounted_price": "18.00",
        "product_count": 150
    },
    {
        "product_id": 56,
        "product_name": "Glue Stick",
        "description": "Mess-free glue stick for crafting.",
        "category": 19,
        "image_url": "https://via.placeholder.com/150/33A6FF/FFFFFF?text=Glue+Stick",
        "mrp": "2.00",
        "discounted_price": "1.80",
        "product_count": 200
    },
    {
        "product_id": 57,
        "product_name": "Craft Scissors",
        "description": "Sharp craft scissors for precise cutting.",
        "category": 19,
        "image_url": "https://via.placeholder.com/150/FF8C33/FFFFFF?text=Craft+Scissors",
        "mrp": "5.00",
        "discounted_price": "4.50",
        "product_count": 100
    },
    {
        "product_id": 58,
        "product_name": "Chef Knife",
        "description": "Professional chef knife for culinary tasks.",
        "category": 20,
        "image_url": "https://via.placeholder.com/150/8C33FF/FFFFFF?text=Chef+Knife",
        "mrp": "40.00",
        "discounted_price": "35.00",
        "product_count": 60
    },
    {
        "product_id": 59,
        "product_name": "Cutting Board",
        "description": "Durable cutting board for food prep.",
        "category": 20,
        "image_url": "https://via.placeholder.com/150/FF33B8/FFFFFF?text=Cutting+Board",
        "mrp": "15.00",
        "discounted_price": "12.00",
        "product_count": 100
    },
    {
        "product_id": 60,
        "product_name": "Measuring Cups",
        "description": "Measuring cups",
        "category": 20,
        "image_url": "https://newimagebase.com/200/200?random=2003",
        "mrp": "10.00",
        "discounted_price": "8.00",
        "product_count": 80
    }
        ]

        # Add products to Solr
        solr.add(products)
        self.stdout.write(self.style.SUCCESS('Successfully indexed products into Solr'))
