# 20BCE2004 - Hrithik Purwar - SWYM Round 2 BUILD
## Chosen Task - Product Recommender System

## Project Overview

This project aims to create a product recommendation system using a content-based approach. The system recommends products to users based on the similarity between product names, with optional filters for price and discount.

It has been integrated with frontend using Flask routes.

## Table of Contents

- [Screenshots](#screenshots)
- [Choice of Recommender System](#choice-of-recommender-system)
- [Process Flow](#process-flow)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Notebook Link](#notebook-link)
- [How to Run](#how-to-run)

## Screenshots

<b>I) Flask Deployed (Content based recommendation based on Product Name)</b>
![Screenshot 2023-08-08 at 9 16 48 PM](https://github.com/hrithikpurwar/SWYMtask/assets/72293452/b7246171-cf86-4d96-8362-dd0a1129ce72)

<b>II) Jupyter Notebook (Content based recommendation based on Product Name with Min Price and Max price Filter)</b><br>
![Screenshot 2023-08-08 at 9 17 06 PM](https://github.com/hrithikpurwar/SWYMtask/assets/72293452/38c3e43c-6613-4183-8b15-d77f79e87c7a)

<b>III) Jupyter Notebook (Content based recommendation based on Product Name with Min Price, Max price, and Min discount Filter)</b><br>
![Screenshot 2023-08-08 at 9 17 32 PM](https://github.com/hrithikpurwar/SWYMtask/assets/72293452/a47eb65d-451b-474f-b1fe-fbc5b20eeeca)

<b>IV) Jupyter Notebook (Content based recommendation based on Product Name)</b><br>
![Screenshot 2023-08-08 at 9 17 48 PM](https://github.com/hrithikpurwar/SWYMtask/assets/72293452/1de36a39-63c2-487b-92d1-ef9b7e4f37fa)

<b>V) Error Handling (when product name is not present)</b><br>
![Screenshot 2023-08-08 at 9 18 07 PM](https://github.com/hrithikpurwar/SWYMtask/assets/72293452/ec7a226f-f45c-414e-9d38-bb26363b46ae)


## Choice of Recommender System

I had 3 choices of recommender system

1. Content Based - Recommends products based on Product Similarity
2. Collaborative Filtering - Recommends products based on User Preferences Similarities
3. Reinforcement Learning - Recommends product by going through purchase history of user by exploration and exploitation of different item recommendations and develops its learning.

Based on the given problem statement, we need to see user's preference / product and recommend similar products.

So the most suitable one here would be <b>Content Based Recommender system</b>

## Process Flow

## Technologies Used

### Jupyter Notebook
- Numpy
- Pandas
- NLTK (Natural Language ToolKit)
- TfidfVectorizer
- Cosine Similarity

### Web App
- Flask
- HTML
- CSS


## Dataset

The project utilizes the [Flipkart Products Dataset](https://www.kaggle.com/datasets/PromptCloudHQ/flipkart-products) from Kaggle.

## Notebook Link

The detailed implementation and analysis can be found in the [Jupyter Notebook](https://www.kaggle.com/hrithikpurwar/swym-task).

## How to Run

1. Clone the repository.
2. Navigate to the project directory in your terminal.
3. Install required dependencies with `pip install -r requirements.txt`.
4. Run the Flask app with `flask run`.
5. Access the web app in your browser at `http://localhost:5000`.


## Acknowledgments

Special thanks to the [SWYM](https://swym.it) team for the opportunity to work on this task.





