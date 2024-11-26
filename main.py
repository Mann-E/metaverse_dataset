import os

daily_objects = [
    # Vehicles
    "car", "bicycle", "motorcycle", "bus", "train", "airplane", "boat", "scooter", "truck", "subway",
    "helicopter", "skateboard", "rollerblades", "canoe", "yacht", "tractor", "ambulance", "fire truck", "police car", "RV",

    # Appliances
    "smartphone", "laptop", "desktop", "tablet", "smartwatch", "television", "radio", "camera", "headphones", "speaker",
    "refrigerator", "microwave", "oven", "toaster", "blender", "kettle", "coffee maker", "dishwasher", "washing machine", "dryer",
    "vacuum cleaner", "iron", "air conditioner", "heater", "fan", "water heater", "electric stove", "pressure cooker", "hair dryer", "humidifier",

    # Furniture
    "desk", "chair", "sofa", "bed", "wardrobe", "bookshelf", "table", "cabinet", "mirror", "lamp",
    "dining table", "stool", "bench", "nightstand", "cupboard", "coffee table", "ottoman", "TV stand", "vanity", "hammock",

    # Office Supplies
    "pen", "pencil", "notebook", "calendar", "ruler", "eraser", "scissors", "stapler", "highlighter", "clipboard",
    "sticky notes", "hole puncher", "paper clips", "push pins", "whiteboard", "marker", "envelope", "tape dispenser", "file folder", "printer",

    # Foods
    "bread", "rice", "pasta", "cheese", "butter", "milk", "egg", "chicken", "beef", "fish",
    "potato", "onion", "garlic", "carrot", "tomato", "lettuce", "cucumber", "bell pepper", "broccoli", "spinach",
    "apple", "banana", "grape", "orange", "watermelon", "pineapple", "mango", "strawberry", "blueberry", "kiwi",
    "chocolate", "cookies", "chips", "cake", "ice cream", "yogurt", "pizza", "burger", "sandwich", "hotdog",

    # Tools
    "hammer", "screwdriver", "wrench", "pliers", "drill", "saw", "measuring tape", "level", "utility knife", "chisel",
    "ladder", "shovel", "rake", "hoe", "garden shears", "paintbrush", "roller", "bucket", "toolbox", "anvil",

    # Jobs
    "police officer", "firefighter", "teacher", "doctor", "nurse", "engineer", "mechanic", "electrician", "plumber", "chef",
    "barista", "cashier", "accountant", "architect", "programmer", "graphic designer", "writer", "editor", "pilot", "flight attendant",
    "gardener", "carpenter", "construction worker", "painter", "cleaner", "driver", "scientist", "pharmacist", "lawyer", "judge",
    "dentist", "veterinarian", "therapist", "personal trainer", "coach", "artist", "musician", "actor", "director", "producer",

    # Miscellaneous
    "book", "magazine", "newspaper", "umbrella", "wallet", "key", "watch", "bag", "sunglasses", "hat",
    "water bottle", "backpack", "phone charger", "flashlight", "batteries", "calculator", "laundry basket", "trash can", "remote control", "shoe",
    "gloves", "belt", "scarf", "ring", "necklace", "earrings", "toothbrush", "toothpaste", "soap", "shampoo",
    "towel", "blanket", "pillow", "curtain", "mat", "rug", "clock", "fan", "binoculars", "first aid kit",
    "camera tripod", "mouse", "keyboard", "router", "extension cord", "power bank", "gaming console", "hairbrush", "nail clipper", "comb"
]

prompts = []

for object in daily_objects:
    print(f"{object}, lowpoly, 3d illustration, dark background, isometric camera angle")