# David Richard Steinmetz
# davidsteinmetz@gmail.com

# Supervisor function which calls functions to:
# 1. Get data about businesses on the map from Yelp API
# 2. Assign the businesses to clusters using KNN based on the pre-run K-means model
# 3. Sort the businesses by cluster and rating to be able to rec good restaurants
# 4. Get the recommendations from the graphlab model
# 5. Extract the cluster data from the graphlab model recommendations
# 6. Generate a list of recommended restaurants based on knowledge of model recs

from Cluster import *
import numpy as np


def cluster():
    # Test structures
    test_biz_cluster = pd.Series(np.random.randint(1, 25, 20))
    test_model_recs = pd.DataFrame({'cluster': np.random.randint(1, 25, 10)})

    biz = get_businesses_on_map()  # Get businesses on map
    # biz['cluster'] = get_map_clusters(biz)                # Get clusters for biz on map
    biz['cluster'] = test_biz_cluster  # Get clusters for biz on map
    sorted_biz = cluster_rating_sort(biz)  # Sort biz by cluster and rating
    # model_recs = load_model('graphlab_model.pkl')           # Get model recommendations
    model_recs = test_model_recs  # Get model recommendations
    model_clusters = get_model_clusters(model_recs)  # Get clusters for model recs
    map_recs = gen_map_recs(sorted_biz, model_clusters)  # Generate recs from biz on map

    return map_recs