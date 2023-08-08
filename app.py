import pandas as pd
from flask import Flask, render_template, request

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load the preprocessed data
smd = pd.read_csv('preprocessed.csv')

# Calculate TF-IDF matrix
tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(smd['all_meta'])

# Calculate cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Reset index and create indices Series
smd = smd.reset_index()
titles = smd['product_name']
indices = pd.Series(smd.index, index=smd['product_name'])


def get_recommendations(title):
    idx = indices.get(title)
    if idx is None:
        return None  # Return None if product is not found
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    product_indices = [i[0] for i in sim_scores]
    return titles.iloc[product_indices]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_name = request.form['product_name']
        recommended_products = get_recommendations(product_name)
        if recommended_products is None:
            error_message = "Product not found"
            return render_template('index.html', product_name=product_name, error_message=error_message)
        else:
            recommended_products = recommended_products.head(5)
            return render_template('index.html', product_name=product_name, recommended_products=recommended_products)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
