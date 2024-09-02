# My-Zootopia

My-Zootopia is a Python-based project that generates a dynamic website showcasing information about various animals. 
Users can input the name of an animal, 
and the project will fetch and display detailed information about that animal, 
including taxonomy, characteristics, and locations, using the [API Ninjas Animals API](https://api-ninjas.com/api/animals).

## Features

- Fetches real-time animal data from an external API.
- Generates a static HTML page with detailed information.
- Simple command-line interface for user input.

## Installation
To install this project, simply clone the repository,
and install the dependencies in `requirements.txt` using `pip`

### Prerequisites

- Python 3.7+
- pip (Python package installer)
- Git 

### Steps

1. **Clone the Repository**

   Open the Terminal and run:

   ```bash
   git clone https://github.com/SangamithraMB/My-Zootopia.git
   cd My-Zootopia
   
2. Create a Virtual Environment 
   ```bash 
   python3 -m venv venv
   source venv/bin/activate

3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   
4. Set Up Environment Variables:
   ```bash
   echo "API_KEY='your_api_key_here'" > .env
   
### Usage
To use this project:

1. Run the Program
   Execute the script to fetch animal data and generate the website:
   ```bash
   python animals_web_generator.py

2.	Enter the Animal Name
When prompted, input the name of the animal you’re interested in. The program will generate an animals.html file containing the details of the animal.

3.	View the Website
Open the generated animals.html file in your web browser to see the information.

### Contributing
 Contributions to My-Zootopia is welcome! If you’d like to contribute:

	1.	Fork the repository.
	2.	Create a new branch for your feature or bug fix.
	3.	Submit a pull request with a clear description of your changes.

### Instructions:
- Replace `'your_api_key_here'` in the `.env` setup step with your actual API key.
- You can add a `LICENSE` file in your repository if you choose to use the MIT License or any other license of your choice.

This `README.md` should now provide a comprehensive guide to setting up and using the "My-Zootopia" project.