import kagglehub

# Download latest version
path = kagglehub.dataset_download("redpen12/mtn-gh-stock-price-dataset")

print("Path to dataset files:", path)